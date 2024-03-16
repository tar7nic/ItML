import numpy as np

# arr = np.arange(0,11) # for creating an array from 1 to 10
# print(arr)

# print(arr[6])    # for printing ele at index 6 in array  
# print(arr[1:6])  # for printing elements from index 1 to 6 -> includes 1 but not 6
# print(arr[:5])   # for printing elements from beginning to index 5 but dusnt include 5
# print(arr[5:])   # for printing elements from index 5 to the end of the list but includes 5
# print(arr[::-1]) # for printing the array in reversed form

# arr[:5] = 100
# print(arr) 

# slice_arr = arr[0:6] # array ko slice kar diya from 1 to 5
# print(slice_arr) 
 
# slice_arr[:] = 99 # saari values ko 99 mei convert kar diya 
# print(slice_arr)

# print(arr) # isme jo original array thi uske first 5 sliced elements turn into 99 whereas all others remain the same

# arr_copy = arr.copy() # created a copy of the array 
# arr_copy[:]=100 # saare elements ko 100 ki value assign kar di
# arr_copy[:5]=100 # index 0 to 4 ke saare ele ki val hogayi 100 
# arr_copy[5:]=500 # index 5 to 10 ke saare ele ki val hogayi 500


# print(arr) # ab jo og  array hai woh same rahega, ie starting 5 ele = 99 and other 5 as they were
# print(arr_copy) # ye wale array mei humne 100 ki value de di saare ele ko isliye sab 100 print honge

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# print(arr_2d)

# print(arr_2d[0, 0]) # ele at row 0 and column 0 = 5
# print(arr_2d[0])    # all eles in row 0 = 5, 10, 15
# print(arr_2d[1, 1]) # ele in row 1 and column 1 = 25
# print(arr_2d[2, 2]) # ele in row 2 and column 2 = 45

# print(arr_2d[:2, 1:]) # iska matlab row mei 2nd row ko chhodke sab lo and column mei 1st column ke baad sab lo
# print(arr_2d[:2, 0:])

# print(arr_2d[:2, 2:]) # 

# print(arr_2d[:2]) # row 2 ko chhodke sab kuch lelo  

# print(arr_2d[2])
# print(arr_2d[:,2])
# print(arr_2d[0:3,1:2])

# print(arr_2d[0:2,2:3])

# arr_a = np.arange(1,11)
# print(arr_a)
# boool = arr_a > 5
# print(arr_a[boool])
# print(arr_a[arr_a<8])
