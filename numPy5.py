import numpy as np
arr=np.array([1,2,3,4])
print(arr)

arr=np.array([1, 7862, 3,4], dtype=np.int32)
print(arr)
arr[0]=2
arr[1]=3
arr[2]=4
arr[3]=5
print(arr)
arr=np.array([2,3,4,5], dtype=np.int8)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.size)
print(arr.dtype)

darr1=np.array([[1,2,3,5],[4,6,7,8]])
print(darr1)
print(darr1.shape)
print(darr1.size)
print(darr1.dtype)

