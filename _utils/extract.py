# Move utility functions for data extraction here

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