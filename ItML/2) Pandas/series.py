import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
dicti = {'a':10, 'b':20, 'c':30}

# print(pd.Series(data = my_data)) # data printing with index
# print(pd.Series(my_data, labels)) # data printing with index as label values

# print(pd.Series(arr))  # normal numpy array jaise ayega
# print(pd.Series(arr, labels)) # isme bhi np array ke index ko labels se replace kar diya

# print(dicti) # dict humesha apne key values ke sath hi print hoti hai
# print(pd.Series(dicti)) # pandas use karte hue ek baar mei without using index as labels hi dict print hogayi

# print(pd.Series(data = labels))

ser1 = pd.Series([1,2,3,4],[['usa','germany','ussr','japan']])
ser2 = pd.Series([1,2,5,4],[['usa','germany','italy','japan']])

# print(ser1)
# print(ser2)

# print(ser1['japan'])
# print(ser2['italy'])

# ser3 = pd.Series(data=labels)
# print(ser3) 
# print(ser3[0]) 
# print([ser1 + ser2])

