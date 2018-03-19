# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:47:08 2018

@author: ianad

This script was used to extract data from the EyeLink native RESULTS_FILE.txt
and convert it into BIDS format .xlsx files for inclusion in the full dataset

Directory paths as written represent the structure in which the data was 
originally found, raw from the EyeLink. There were 2 separate versions of the 
experiment, containing different sets of subject-number-specific trial lists
(300-322 && 323-345).

The script was run from just outside these directories, and converted and
wrote the BIDS-standard output at the same level.
This output was then copy-pasted into the dataset/sourcedata/

"""

import os
import pandas as pd
dirlist=[os.path.join('iecondec300_322','results'),os.path.join('iecondecpart323_345','results')]
subjs=[]
Files=[]
for d in dirlist:
    for s in os.listdir(d):
        if s.startswith('3'):
            subjs.append(s)
            spath=os.path.join(d,s)
            for f in os.listdir(spath):
                if f.endswith('.txt'):
                    fpath=os.path.join(spath,f)
                    print fpath
                    file=pd.read_csv(fpath, delimiter='\t')
                    Files.append(file)
                    outdir='sub-'+s
                    if not os.path.isdir(outdir):
                        os.mkdir(outdir)
                    outpath=os.path.join('sub-'+s,'sub-'+s+'_task-eye_beh.xlsx')                    
                    file.to_excel(outpath)
Frame=pd.concat(Files)
Frame.to_excel('sub-all_task-eye_beh.xlsx')