import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def check_data_variance(df,tol=.5):
    """
    Returns the rows of a dataframe if the variance is less than tol.
    INPUT:
        df (dataframe)
        tol (float) return a row if its variance is less than tol, default=.5

    """
    rows = df.var(axis=1) < tol
    return df[rows]
    
def check_data_uniqueness(df,tol=3):
    """
    Returns the rows of a dataframe if the number of unique row entries is less than tol.
    INPUT:
        df (dataframe)
        tol (int) return a row if the number of unique entries in a row is less than tol, default=3
        
    """
    rows = df.apply(lambda x: len(np.unique(x)) < tol, axis=1)
    return df[rows]

def check_data_for_extreme_responses(df,J=None,tol=.85):
    """
    Returns the rows of a dataframe if the percentage of values outside an interval is greater than tol.
    INPUT:
        df (dataframe)
        J (listlike) the interval specifying a min value and max value, default is the min and max over the dataframe
        tol (float) return a row if the proportion of extreme values in the row exceeds tol, default=.85
        
    """
    if J is None:
        J = [df.min().min(), df.max().max()]
    ex_vals = lambda x: np.logical_or(x<=J[0], x>=J[1])
    rows = df.apply(lambda x: sum(ex_vals(x))/len(x) > tol, axis=1)
    return df[rows]

def check_data(df,**kwargs):
    pass
    
    
### UNIT TESTS ###

def gen_test_df():
    D = np.ones((10,10))
    # D[0] is a row of ones
    D[1] = [1,2,1,2,1,2,1,2,1,2]
    D[2] = [1,2,3,1,2,3,1,2,3,1]
    D[3] = [1,4,1,4,1,4,1,4,1,4]
    D[4] = [1,2,3,4,1,2,3,4,1,2]
    D[5] = [1,1,1,1,1,2,2,2,2,2]
    D[6] = [1,1,1,1,1,1,1,1,1,2]
    D[7] = [1,4,1,4,1,4,3,4,1,4]
    D[8] = [1,2,3,2,3,4,4,3,2,1]
    D[9] *= 4
    return pd.DataFrame(D)

def test_check_data_variance(test_df):
    assert np.allclose(test_df.iloc[[0,1,5,6,9]].index,check_data_variance(test_df).index)
    
def test_check_data_uniqueness(test_df):
    assert np.allclose(test_df.iloc[[0,1,3,5,6,9]].index,check_data_uniqueness(test_df).index)
    
def test_check_data_for_extreme_responses(test_df):
    assert np.allclose(test_df.iloc[[0,3,6,7,9]].index,check_data_for_extreme_responses(test_df).index)
    
def run_tests():
    test_df = gen_test_df()
    test_check_data_variance(test_df)
    test_check_data_uniqueness(test_df)
    test_check_data_for_extreme_responses(test_df)