# Move utility functions for data cleaning here

import os

def clean_paths(row):
    return os.path.basename(row['oldfractal'])

def normalize(row):
    study = row['study']
    val = row[key]
    group_mean = df.groupby('study').mean().loc[study,key]
    group_std = df.groupby('study').std().loc[study,key]
    zval = (val - group_mean) / group_std
    return zval

def exclude_3sd(row):
    ssid,val = row['ssid'],row['val_estdiff_valid']
    mean,bound = subj_means[ssid],subj_3sd[ssid]
    diff = abs(val - mean)
    if diff < bound:
        return(val)
    else: return(np.nan)
    
def normalize_frame(row):
    ssid,val = row.name,row['valError_3sd']
    ssid = str(ssid)
    if ssid.startswith('2'):
        val = val * -1
    return(val)

def __init__(self):
    pass