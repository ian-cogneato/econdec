# Move utility functions for data extraction here

from pathlib import Path
import pandas as pd

def main():
    pass

def concat(dataset, task = 'all'):
    
    dataframes_list = []
    
    if dataset.name == 'ds1' or dataset.name == 'ds2':
        
        if task == 'all':
            raise ValueError('You must specify a task string.')
        
        for sub in dataset.glob('sub-*'):
            filename = sub / (sub.name + '_task-' + task + '_beh.xlsx')
            
            try:
                dataframes_list.append(pd.read_excel(filename))
            except FileNotFoundError as e:
                print(e)
        
    if dataset.name == 'ds3':
        
        for sub in dataset.glob('sub-*'):
            filename = sub / 'RESULTS_FILE.txt'
            
            try:
                results = clean_crlf(filename)
                dataframes_list.append(results)
            except FileNotFoundError as e:
                print(e)
    
    dataframe = pd.concat(dataframes_list)
    return(dataframe)
    


def clean_crlf(fpath):
    """
    Reads an EyeLink RESULTS_FILE as binary string, writes a TSV file with all carriage return characters removed, then returns the result of reading that TSV file as a pandas.DataFrame.

    A better version of this function would simply return the DataFrame object without writing the TSV file literally.
    """
    sub = fpath.parent
    
    with open(fpath, 'rb') as f:
        raw_content = f.read()
        lfnull_content = raw_content.replace(b'\r',b'')
        
    outpath = sub / ('sub-' + sub.name + '_task-all_beh.tsv')
    with open(outpath, 'w') as f:
        f.write(lfnull_content.decode("utf-8"))

    return(pd.read_csv(outpath, delimiter='\t'))

def score_financial_literacy(row):
    resp = row[2]
    if resp == 3:
        return 3
    if resp == 4 or resp == 5 or resp == 7:
        return 2
    if resp == 1 or resp == 2 or resp == 8:
        return 1
    if resp == 6:
        return 0

def __init__(self):
    pass

if __name__ == '__main__':
    main()