import pandas as pd

def nstack_score_label(fpath,outpath):
    df = pd.read_excel(fpath)
    
    # Hierarchicalize the column index
    df.columns=pd.MultiIndex.from_tuples([
        (df.columns[0].split('.')[0],df.columns[0].split('.')[1]),
        (df.columns[1].split('.')[0],df.columns[1].split('.')[1]),
        (df.columns[2].split('.')[0],df.columns[2].split('.')[1]),
        (df.columns[3].split('.')[0],df.columns[3].split('.')[1]),
        (df.columns[4].split('.')[0],df.columns[4].split('.')[1]),
        (df.columns[5].split('.')[0],df.columns[5].split('.')[1]),
    ])
    
    # Stack blocks, Reset trial row index, and Rename columns to be descriptive
    df = df.stack(0).reset_index().rename(
        columns={'level_0':'trial','level_1':'block'}
    ).sort_values(['block','trial'])
    df['sub'] = os.path.basename(fpath).split('_')[0].split('-')[1]
    df['block'] = df['block'].str[1]
    df['trial'] = df['trial'] + 1
    df = df.set_index(['sub','block','trial'])
    
    # Determine Hits, CRs, FAs
    cr_mask = (df['Rsp'] == 0) & (df['CRsp'] == 0)
    ms_mask = (df['Rsp'] == 0) & (df['CRsp'] == 1)
    fa_mask = (df['Rsp'] == 1) & (df['CRsp'] == 0)
    ht_mask = (df['Rsp'] == 1) & (df['CRsp'] == 1)
    df['CR']   = cr_mask.astype(int)
    df['MISS'] = ms_mask.astype(int)
    df['FA']   = fa_mask.astype(int)
    df['HIT']  = ht_mask.astype(int)
    
    # Convert RT 0 to RT NaN
    df['RT'] = df['RT'].replace(0,np.NaN)
    
    # Output to new CSV datafile
    df.to_csv(outpath)
    print('Output file successfully created- ',outpath)