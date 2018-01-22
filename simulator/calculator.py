# modifies data for automating conjoint simulator

import numpy as np
import pandas as pd

df = pd.read_csv("HB_Utilities.csv")

factors = df.columns.as