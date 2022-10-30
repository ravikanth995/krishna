import numpy as np
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))

arr=np.array([1,9801,3], dtype=np.int8)
print(arr)
print(type(arr))


arr[0]
arr[1]=0
print(arr)

arr[0]
arr[2]=0
print(arr)

darr1=np.array([[1,2,3,4],[5,6,7,8]])
print(darr1)
print(darr1.shape)
print(darr1.size)
print(darr1.dtype)