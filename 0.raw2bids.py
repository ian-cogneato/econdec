 
# coding: utf-8

# collects raw EyeLink results dumped in ../sourcedata/.old and converts to BIDS-spec for downstream processing

import os
from shutil import copyfile
import pandas as pd

sourcedir = os.path.join('..','sourcedata','.staging')
outputdir = os.path.join('..','sourcedata','ds3')

Files = []
subjs = []
for s in os.listdir(sourcedir):
    if s.startswith('3'):
        subjs.append(s)
        spath = os.path.join(sourcedir,s)
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
                file = pd.read_csv(fpath, delimiter='\t')
                Files.append(file)
                outpath = os.path.join(outdir,'sub-'+s+'_task-eye_beh.csv')
                if not os.path.isfile(outpath):
                    print(f,'\t=>\t',outpath)
                    file.to_csv(outpath)
                else:
                    print('Already converted\n')
                    
input('Done')