
# coding: utf-8

# collects raw EyeLink results dumped in ../sourcedata/.old and converts to BIDS-spec for downstream processing

import os
from shutil import copyfile
import pandas as pd

sourcedir = os.path.join('..','sourcedata','.old')
outputdir = os.path.join('..','sourcedata','ds3')

dirlist=[os.path.join('ED3_300','results'),os.path.join('ED3_323','results'),os.path.join('ED3_329','results')]
Files=[]

subjs=[]
for d in dirlist:
    dpath = os.path.join(sourcedir,d)
    for s in os.listdir(dpath):
        if s.startswith('3'):
            subjs.append(s)
            spath = os.path.join(dpath,s)
            for f in os.listdir(spath):
                fpath = os.path.join(spath,f)
                outdir = os.path.join(outputdir,'sub-'+s)
                outpath = os.path.join(outdir,f)
                print(fpath)
                if not os.path.isfile(outpath):
                    print('Copying...')
                    copyfile(fpath,outpath)
                    print(outpath)
                if f.endswith('.txt'):
                    file = pd.read_csv(fpath, delimiter='\t')
                    Files.append(file)
                    if not os.path.isdir(outdir):
                        os.mkdir(outdir)
                    outpath = os.path.join(outdir,'sub-'+s+'_task-eye_beh.xlsx')
                    if not os.path.isfile(outpath):
                        print('Converting to... ')
                        #file.to_excel(outpath)
                        print(outpath+'\n')
                    else:
                        print('Already converted\n')