
# coding: utf-8

# collects raw EyeLink results dumped in ../sourcedata/.staging and converts to BIDS-spec for downstream processing

import os
from utils import clean_crlf
from shutil import copyfile
import pandas as pd

sourcedir = os.path.join('..','sourcedata','.staging')
outputdir = os.path.join('..','sourcedata','ds3')

def raw2bids(sourcedir,outputdir):
    Files = []
    subjs = []
    for s in os.listdir(sourcedir):
        spath = os.path.join(sourcedir,s)
        if s.startswith('3') and os.path.isdir(spath):
            subjs.append(s)
            for f in os.listdir(spath):
                fpath = os.path.join(spath,f)
                outdir = os.path.join(outputdir,'sub-'+s)
                outpath = os.path.join(outdir,f)
                if not os.path.isdir(outdir):
                    os.mkdir(outdir)
                if not os.path.isfile(outpath):
                    print(f,'\t=>\t',outpath)
                    copyfile(fpath,outpath)
                if f == 'RESULTS_FILE.txt':
                    file = clean_crlf(fpath)
                    print(fpath)
                    Files.append(file)
                    outpath = os.path.join(outdir,'sub-'+s+'_task-all_beh.csv')
                    if not os.path.isfile(outpath):
                        print(f,'\t=>\t',outpath)
                        file.to_csv(outpath)
                    else:
                        print('Already converted\n')
                        
    return('Done')

if __name__ == "__main__":
    raw2bids(sourcedir,outputdir)