import numpy as np

arr = np.zeros(10)
print(arr)

arr1 = np.ones(10)
print(arr1)

print(arr1*5)
print(arr+5)

print(np.arange(10,51))

print(np.arange(10,51,2))

arr_2d = np.arange(9).reshape(3,3)
print(arr_2d)

ar_2d = np.eye(3,3)
print(ar_2d)

print(np.random.rand(1))
print(np.random.randn(25))

arr_3 = np.arange(1,101).reshape(10,10)
print(arr_3/100)

print(np.linspace(0,1,20))

mat = np.arange(1,26).reshape(5,5)
print(mat)

print(mat[2:5,1:5])
print(mat[2:,:])
print(mat[3,4,])

print(mat[0:3,1:2])
print(mat[4:,:])

print(mat[3:,:])

print(np.sum(mat))
print(mat.sum())

print(mat.std())
print(np.std(mat))

print(mat.sum(axis=0))
print(mat.sum(axis=1))
