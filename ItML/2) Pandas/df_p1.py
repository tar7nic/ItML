import numpy  as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z']) # randn - 5 rows, 4 columns, abcde - 5 rows , wxyz - 4 columns
print(df)
print(df['W']) #or use print(df.W) # print a paticular column of the dataframe
print(type(df['W'])) # datatype of printed dataframe

print(df[['W','Z']]) # use list form for printing two columns

df['new'] = df['W'] + df['Y'] # for creating a new column w the values as sum of columns W and Y
print(df)

print(df.drop('new', axis = 1)) # deletion (axis = 0 for rows and axis = 1 for columns)
# the above statement doesnt delete the column in df if we call df separately, therefore we use inplace argument

(df.drop('new', axis = 1, inplace= True)) # inplace = true dalne se hum verify kar rahe hai ki data lose nahi hora and we are intentionally doing it  
print(df)

print((df.drop('E',axis=0))) # doesnt change df
print((df.drop('E',axis=0,inplace=True))) # inplace = True changes df permanently
print(df) 

print(df.shape) # df ka row and column size 

print(df.loc['A']) # A row ke saare elements in all columns using row name
print(df.iloc[2]) # row 2 ke saare elements in all columns using index val of rows

print(df.loc['B','Y']) # element in row b and column y

print(df.loc[['A','B'],['W','Y']]) # A and B row ke elements in column W and Y

