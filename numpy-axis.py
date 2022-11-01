import numpy as np
#axis
x=[[1,2,3],[4,5,6]]
ar=np.array(x)
# print(ar)
# ar.shape
# print(ar)

# ar=ar.sum(axis=0)
# ar=ar.sum(axis=1)
# print(ar)

#transpose
# ar=ar.T
# print(ar)

#iteration
# ar=ar.flat
# print(ar)

# for i in ar.flat:
#     print(i)

# ar=ar.dim
# print(ar)

#number of elemnts
# ar.size


#matrix
t=x=[[1,2,4],[7,1,6],[3,10,6]]
mnt=ar=np.array(t)
print(mnt)
mnt.argmax(axis=0)
print(ar)
print(mnt)

# ar=ar.ndim
# print(ar)

# ar.size

#matrix
print(ar)
print(mnt)
print('MAtrix add operation')
print(ar+mnt)
print(ar*mnt)

#square 
print(ar)
np.sqrt(ar)


#square
print(ar)
# ar.max()
# ar.sum()
# ar.min()


np.where(ar>5)
np.count_nonzero(ar)