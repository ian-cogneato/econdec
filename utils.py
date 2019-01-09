
# coding: utf-8

import os
import pandas as pd
import operator

def dfsplit(input_frame, column_criterion, value_criterion, operation_flag = '=='):
    ops = {'>' : operator.gt, '<' : operator.lt, '==': operator.eq,
           '!=': operator.ne, '<=': operator.le, '>=': operator.ge}
    op = ops[operation_flag]
    output_frame = input_frame[op(input_frame[column_criterion],value_criterion)]
    return output_frame

def smooth_columns(input_frame):
    column_labels = list(input_frame.columns)
    input_frame.columns = [c.lower().replace('_','') for c in column_labels]
    return input_frame

def eye_cleanup(input_frame):
    f=input_frame
    f=f[f['facekeypressed']!='.']
    f=f[f['practice'].astype(int)>2]
    return f

def label_study(row):
    study_label = str(row['subjnum'])[0]
    return study_label

def clean_choicert(row):
    if int(row['study']) >= 3:
        return float(row['choicert'] * .001)
    else:
        return row['choicert']

def clean_outcomert(row):
    if int(row['study']) >= 3:
        return float(row['outcomert'] * .001)
    else:
        return row['outcomert']

def clean_esttaskrt(row):
    if int(row['study']) >= 3:
        return float(row['esttaskrt'] * .001)
    else:
        return row['esttaskrt']

def clean_stockchosen(row):
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
    return os.path.split(row['bondpic'])[1]

def clean_stockpic(row):
    return os.path.split(row['stockpic'])[1]

def clean_selection(row):
    if row['correctfractallocation'] == '(1355, 540)':
        # correct fractal was on right
        return int(row['selection'])-4
    elif row['correctfractallocation'] == '(565, 540)':
        # correct fractal was on left
        return -int(row['selection'])+5

