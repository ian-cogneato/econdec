# Move utility functions for data transformation here

def group_exclude(df, group_col, value_col, upper_Q = 0.99865, lower_Q = 0.00135):
    """ Takes a DataFrame, column name to group on, and a value column name.
    
    Performs outlier exclusion based on quantile thresholds and returns a Series."""

    # Create Series of upper and lower bounds within-groups with respect to `group_col`
    value_upper = value_col + 'upper'
    value_lower = value_col + 'lower'
    upper_bounds = (df.groupby(group_col)
                        .quantile(upper_Q)[value_col]
                        .rename(value_upper)
                        .reset_index())
    lower_bounds = (df.groupby(group_col)
                        .quantile(lower_Q)[value_col]
                        .rename(value_lower)
                        .reset_index())
    
    # Merge `df` with upper and lower bounds, into `df_bounds`
    df_bounds = (df.merge(upper_bounds,'left')
                    .merge(lower_bounds,'left'))

    # Return a Series with values only where the value in `value_col`
    # is between the corresponding upper and lower bounds
    value_bound = value_col + '_bound'
    return(df_bounds[value_col].where(
                (df_bounds[value_col] > df_bounds[value_lower]) &
                (df_bounds[value_col] < df_bounds[value_upper]))
            .rename(value_bound))

def sum_oscillations(row):
    if row['ia-id'] in (1,24,26):
        return sum([row['fsa-ia-02'],row['fsa-ia-25'],row['fsa-ia-27']])
    elif row['ia-id'] in (2,25,27):
        return sum([row['fsa-ia-01'],row['fsa-ia-24'],row['fsa-ia-26']])

def oscillation_rate(row):
    return float(row['oscillations'] / row['choicert'])

def score_relative_stress(row):
    if row[4] < 5: return -1
    if row[4] > 5: return 1
    if row[4] == 5: return 0
    
def numeralize_sleep(row):
    try:
        if isinstance(row[2],basestring) and '-' in row[2]:
            values = row[2].split('-')
            return np.average([float(values[0]),float(values[1])])
        else:
            return float(row[2])
    except ValueError as e:
        print(e)
        return(row[2])
    
def score_relative_sleep(row):
    try:
        if float(row[1]) < float(row[2]): return -1
        if float(row[1]) > float(row[2]): return 1
        if float(row[1]) == float(row[2]): return 0
    except ValueError as e:
        print(e)
        return('NaN')

def __init__(self):
    pass