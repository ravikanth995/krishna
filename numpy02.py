import numpy as np
a=np.array([1,2,3,4])
print(a)
a[0]
a[1]=99
print(a)
a[1]=2
print(a)

a=np.array([1,2234,3],dtype=np.int32)
print(a)
a1=np.array([[1,2,3],[4,5,6]])
print(a1)
print(type(a1))

print(a1.shape)
print(a1.size)
print(a1.dtype)


x=[[1,2,3],[4,5,6]]
y=(1,2,3)
z={1,2,3}
a={1:2,3:4}

 
v=np.array(x)
print(v[0])
print(v[1:2,3:4])
print(v[0,1])
b=np.array(y)
print(b[2:1])