import numpy  as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z']) # randn - 5 rows, 4 columns, abcde - 5 rows , wxyz - 4 columns
print(df)
# print(df>0) # for boolean vals in the given dataframe
# print(df[df>0]) # values > 0 will remain, and vals < 0 -> NaN

# print(df['W']>0) # same operation for W column
# print(df[df['W']>0]) # will print only the rows in which the value > 0



