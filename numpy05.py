
import numpy as np
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))

arr1=np.array([(1,2,3),(4,5,6)])
print(arr1)

arr[0]
arr[1]
print(arr1)


arr=np.array([1,2022,3,4],dtype=np.int32)
print(arr)

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape)
print(arr2.size)
print(arr2.dtype)
print(arr2)

x=[[1,2,3],[4,5,6]]
y=(1,2,3)
z={1,2,3}
a={1:2,3:4}
np.array(a)

v=np.array(x)
print(v)
print(v[1])
print(v[:2,1:3])
print(v)