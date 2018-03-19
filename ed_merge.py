# -*- coding: utf-8 -*-
"""
Created on 2018-02-26

@author: ianad

This script is written to realign and merge converted data from eye-tracking
into the concatenated data from studies 1 and 2.

Eye-tracking data converted using Visual EDF2ASC utility, packaged with DataViewer

"""


import os
import pandas as pd

def dfsplit(input_frame, column_criterion, value_criterion, operation_flag = '=='):
    import operator
    ops = {'>' : operator.gt, '<' : operator.lt, '==': operator.eq,
           '!=': operator.ne, '<=': operator.le, '>=': operator.ge}
    op = ops[operation_flag]
    output_frame = input_frame[op(input_frame[column_criterion],value_criterion)]
    return output_frame

def smooth_columns(input_frame):
    column_labels = list(input_frame.columns)
    input_frame.columns = [x.lower().replace('_','') for x in column_labels]
    return input_frame

def eye_cleanup(input_frame):
    f=input_frame
    f=f[f['facekeypressed']!='.']
    f=f[f['practice']>2]
    return f

source_dir = os.path.abspath('../sourcedata')

eye_fpath = os.path.join(source_dir,'sub-all_task-eye_beh.xlsx')
main_fpath = os.path.join(source_dir,'sub-all_task-main_beh.xlsx')
frac_fpath = os.path.join(source_dir,'sub-all_task-frac_beh.xlsx')
face_fpath = os.path.join(source_dir,'sub-all_task-face_beh.xlsx')

eye_frame = pd.read_excel(eye_fpath)
main_eye_frame = smooth_columns(dfsplit(eye_frame, 'Phase', 'Main Task'))
frac_eye_frame = smooth_columns(dfsplit(eye_frame, 'Phase', 'Fract'))
face_eye_frame = smooth_columns(dfsplit(eye_frame, 'Phase', 'Face'))

main_frame = smooth_columns(pd.read_excel(main_fpath))
frac_frame = smooth_columns(pd.read_excel(frac_fpath))
face_frame = smooth_columns(pd.read_excel(face_fpath))

