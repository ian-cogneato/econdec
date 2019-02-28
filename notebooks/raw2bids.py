
# coding: utf-8

# collects raw EyeLink results dumped in ../sourcedata/.staging and converts to BIDS-spec for downstream processing
from pathlib import Path
import pandas as pd

from _utils.extract import clean_crlf

from config import sourcedata_dir as sourcedata
staging_dir = sourcedata / '.staging'
ds3_dir = sourcedata / 'ds3'

def raw2bids(input_dir, output_dir):
    for sub_dir in input_dir.glob('3*'):
        new_sub_name = 'sub-' + sub_dir.name
        new_sub_dir = output_dir / new_sub_name
        
        for file_path in sub_dir.glob('RESULTS_FILE.txt'):
            new_file_name = new_sub_name +'_task-all_beh.csv'
            new_file_path = new_sub_dir / new_file_name

            print('{0} => {1}'.format(
                file_path.relative_to(sourcedata),
                new_file_path.relative_to(sourcedata)
            ))

            if not new_sub_dir.is_dir():
                Path.mkdir(new_sub_dir)
            if not new_file_path.is_file():
                clean_crlf(file_path).to_csv(new_file_path, index=False)
            


   #print([f for f in Files])
"""    
import os
from _utils.extract import clean_crlf
from shutil import copyfile
import pandas as pd

sourcedir = os.path.join('..','..','sourcedata','.staging')
outputdir = os.path.join('..','..','sourcedata','ds3')

 def _raw2bids(sourcedir,outputdir):
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
 """
if __name__ == "__main__":
    raw2bids(staging_dir, ds3_dir)