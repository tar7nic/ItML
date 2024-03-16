import numpy as np

# ye ek normal list hai, isko array ke form mei dala using np
my_list = [1,2,3]
print(my_list)
arr = np.array(my_list)
print(arr)

# ye ek normal matrix hai jisko np use karke 2d mei print kiya, wdut using np ye ek single line mei aata
my_mat = ([1,2,3], [4,5,6] ,[7,8,9])
print(my_mat)
print(np.array(my_mat))

# arange function tumko specified range mei numbers print karke dega including step count just like python ka range function
print(np.arange(0,10))
print(np.arange(0,10,3))

# np ka zeros func is used to make an array or matrix consisting of zeros only
print(np.zeros(3))

# isme func brackets ke beech mei tuple format mei dalna hai
print(np.zeros((3,3)))

# np ka ones func is used to make an array or matrix consisting of ones only
print(np.ones((5,5)))

# np ka linspace func is used to find equidistant numbers specified within a given range
print(np.linspace(0,5,5))

# for creating an identity matrix, use the np func called 'eye'
print(np.eye(4))

# arr2 ko numpy ke random func ko use karte hue 25 random numbers ka array banaya
arr2 = (np.random.rand((25)))
print(arr2)
# as we know arr2 consists of 25 elements, and woh array form mei hai, toh we can also reshape it in form of a 2d 5x5 matrix. 
print(arr2.reshape(5,5))

# arr1 is an array of 10 random integers between 0 and 20 
arr1 = (np.random.randint(0,20,10))
print(arr1)

# arr is a random 5x5 matrix
arr = np.random.randn(5,5)
print(arr)

# next line is used for having a random integer val bw 0 and 100
print(np.random.randint(1,100))

# next line is used for having 5 random integers bw 0 to 100
print(np.random.randint(1,100,5))

# next line is used for finding the max value of the random integers in the array
print(arr1.max())   

# next line is used for finding the min value of the random integers in the array
print(arr1.min())

# next line is used for finding the index posn of the min value in the array of random inttegers
print(arr1.argmin())

# next line is used for finding the index posn of the max value in the array of random inttegers
print(arr1.argmax())

# next line is used for finding the datatype of the numbers in the array
print(arr1.dtype)
