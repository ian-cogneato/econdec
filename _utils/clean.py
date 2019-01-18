"""
@ianad
This submodule contains all function definitions required for this pipeline's data cleaning.

Some of these function definitions are duplicates from _utils.utils, the legacy module. In other cases, the function definitions in _utils.utils may be deprecated.
"""

import os
from os import path
import numpy as np
import pandas as pd

def clean_crlf(fpath):
    """
    Reads an EyeLink RESULTS_FILE as binary string, writes a TSV file with all carriage return characters removed, then returns the result of reading that TSV file as a pandas.DataFrame.

    A better version of this function would simply return the DataFrame object without writing the TSV file literally.
    """
    sub = path.basename(path.dirname(fpath))
    
    with open(fpath, 'rb') as f:
        raw_content = f.read()
        lfnull_content = raw_content.replace(b'\r',b'')
        
    outpath = path.join('..','sourcedata','ds3','sub-'+sub,'sub-'+sub+'_task-all_beh.tsv')
    with open(outpath, 'w') as f:
        f.write(lfnull_content.decode("utf-8"))

    return(pd.read_csv(outpath, delimiter='\t'))

def split_phases(df):
    """
    Separates DataFrame into groups by unique values of a column 'Phase', and returns a tuple of DataFrames.
    """
    return(
        tuple([df.groupby('Phase').get_group(p) for p in df.Phase.unique()])
    )

def eye_cleanup(input_frame):
    """
    Removes rows from a DataFrame based on predetermined indicators of extraneous data, or an indicator that the row represents unwanted practice data.
    """
    f=input_frame
    f=f[f['facekeypressed']!='.']
    f=f[f['practice'].astype(int)>2]
    return f

def label_study(row):
    """
    Intended for use with DataFrame.apply()

    Reads the 'subjnum' index of a row Series and returns the first digit, in order to label the study series.

    e.g.: Subjects with 'subjnum' in the 100-series, 200-series, etc., are labelled in the return value as '1', '2', etc., respectively.
    """
    study_label = str(row['subjnum'])[0]
    return study_label

def clean_choicert(row):
    """
    Intended for use with DataFrame.apply()

    Returns an array with 'choicert' converted from milliseconds to seconds if the 'study' variable is '3'
    """
    if int(row['study']) >= 3:
        return float(row['choicert'] * .001)
    else:
        return row['choicert']

def clean_outcomert(row):
    """
    Intended for use with DataFrame.apply()

    Returns an array with 'outcomert' converted from milliseconds to seconds if the 'study' variable is '3'
    """
    if int(row['study']) >= 3:
        return float(row['outcomert'] * .001)
    else:
        return row['outcomert']

def clean_esttaskrt(row):
    """
    Intended for use with DataFrame.apply()

    Returns an array with 'esttaskrt' converted from milliseconds to seconds if the 'study' variable is '3'
    """
    if int(row['study']) >= 3:
        return float(row['esttaskrt'] * .001)
    else:
        return row['esttaskrt']

def clean_stockchosen(row):
    """
    INtended for use with DataFrame.apply()

    Composes a boolean 'stockchosen' column from atomic indicators:

    - Whether the stock was on the left or right side of the screen
    - Which button was pressed at selection (left or right)
    """
    if int(row['study']) >= 3:
        if row['selection'] == 1:
            # chose option left
            if row['stockfractallocationtype'] == 'L':
                # stock was on left 
                # row['stockchosen'] = 1
                return 1
            elif row['stockfractallocationtype'] == 'R':
                # stock was on right
                # row['stockchosen'] = 0
                return 0
        elif row['selection'] == 0:
            # chose option right
            if row['stockfractallocationtype'] == 'R':
                # stock was on right
                # row['stockchosen'] = 1
                return 1
            elif row['stockfractallocationtype'] == 'L':
                # stock was on left
                # row['stockchosen'] = 0
                return 0
    else:
        if row['stockchosen'] == 'stock':
            return 1
        elif row['stockchosen'] == 'bond':
            return 0

def clean_bondpic(row):
    """
    Intended for use with DataFrame.apply()

    Calls the split function from os.path on the 'bondpic' element
    """
    return os.path.split(row['bondpic'])[1]

def clean_stockpic(row):
    """
    Intended for use with DataFrame.apply()

    Calls the split function from os.path on the 'stockpic' element
    """
    return os.path.split(row['stockpic'])[1]

def clean_selection(row):
    """
    Intended for use with DataFrame.apply()

    Composes fractal memory score based on 'selection' and 'correctfractallocation'
    """
    if row['correctfractallocation'] == '(1355, 540)':
        # correct fractal was on right
        return int(float(row['selection'])) - 4
    elif row['correctfractallocation'] == '(565, 540)':
        # correct fractal was on left
        return -int(float(row['selection'])) + 5
    
def smooth_columns(input_frame):
    """
    Returns an argued DataFrame with columns names made lowercase and with underscores removed.
    """
    column_labels = list(input_frame.columns)
    input_frame.columns = [c.lower().replace('_','') for c in column_labels]
    return input_frame

def clean_paths(row):
    """
    Intended for use with DataFrame.apply()

    Returns the basename of an 'oldfractal' element using basename() from os.path
    """
    return os.path.basename(row['oldfractal'])

def normalize(row):
    """
    Intended for use with DataFrame.apply()

    'key' and 'df' are not function args, therefore undefined locally
    """
    study = row['study']
    val = row[key]
    group_mean = df.groupby('study').mean().loc[study,key]
    group_std = df.groupby('study').std().loc[study,key]
    zval = (val - group_mean) / group_std
    return zval

def exclude_3sd(row):
    """
    Intended for use with DataFrame.apply()
    
    'subj_means' and 'subj_3sd' are not function args, therefore undefined locally
    """
    ssid,val = row['ssid'],row['val_estdiff_valid']
    mean,bound = subj_means[ssid],subj_3sd[ssid]
    diff = abs(val - mean)
    if diff < bound:
        return(val)
    else: return(np.nan)
    
def normalize_frame(row):
    """
    Intended for use with DataFrame.apply()

    Returns an array with 'valError_3sd' inverted if the 'study' label was 2 , because the framing of the question was inverted in study 2.
    """
    ssid,val = row.name,row['valError_3sd']
    ssid = str(ssid)
    if ssid.startswith('2'):
        val = val * -1
    return(val)

def __init__(self):
    pass