import numpy as np
arr=np.arange(10)
print(arr)

arr1=np.zeros((2,3))
print(arr1)

arr2=np.ones((2,3))
print(arr2)

arr2=np.empty([2,3])
print(arr2)

arr4=np.linspace(1,5,12)
print(arr4)

n=np.arange(9)
print(n)
p=n.reshape(3,3)
print(p)

res=p.ravel()
print(res)