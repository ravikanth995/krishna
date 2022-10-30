import numpy as np
#creating a 1D array in numpy
arr=np.array([1,2,3,4])
print('Creating 1D array in NumPy')
print(arr)
print(type(arr))


#creating 2D array in NumPy

arr1=np.array([(1,2,3,4),(5,6,7,8)])
print('Creating 2D array in NumPy')
print(arr1)
print(type(arr1))

#method to create numpy array
#1. empty() function created array with random garbage values

arr2=np.array([100000000,27666666], dtype=int)
print('Creating NumPy array with empty method and Zeros method')
print(arr2)
print('\n')

#2. zeros() function created array with specifies size and type with zero.default 
#dtype is float

arr3=np.zeros([2,3])
print('\n an array initialized with all zeros\n',arr3)