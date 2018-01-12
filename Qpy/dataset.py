import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def check_data_variance(df,tol=.5):
    rows = df.var(axis=1) < tol
    return df[rows]

def check_data_pattern(df,pattern,tol):
    raise NotImplementedError("under development")
    
def check_data_uniqueness(df,tol=3):
    rows = df.apply(lambda x: len(np.unique(x)) < tol, axis=1)
    return df[rows]
    
    
    
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
    D[7] = [5,6,7,8,5,6,7,8,5,6]
    D[8] = [9,8,7,6,5,4,3,2,1,0]
    D[9] *= 5
    return pd.DataFrame(D)

def test_check_data_variance(test_df):
    assert np.allclose(test_df.iloc[[0,1,5,6,9]].index,check_data_variance(test_df).index)

def test_check_data_pattern(test_df):
    print("test_check_data_pattern(): under development")
    
def test_check_data_uniqueness(test_df):
    #print("test_check_data_uniqueness(): under development")
    assert np.allclose(test_df.iloc[[0,1,3,5,6,9]].index,check_data_uniqueness(test_df).index)
    
def run_tests():
    test_df = gen_test_df()
    test_check_data_variance(test_df)
    test_check_data_pattern(test_df)
    test_check_data_uniqueness(test_df)