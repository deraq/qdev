import pytest
import numpy as np
import pandas as pd
# from qdev.Qpy import dataset

def test_check_data_variance():

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
    df_test = pd.DataFrame(D)
    return dataset.check_data_variance(df_test)