#Creating a 1-D Numpy Array
# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

#Creating 2-D Array
# arr=np.array([(1,2,3),(4,5,6)])
# print(arr)

# arr=np.array([(1,2,3),(4,5,6)])
# print(arr)

# arr=np.array([(1,2,3),(4,6,5)])
# print(arr)

# arr=np.array([(1,2,3),(4,5,6)])
# print(arr)

# arr=np.array([(1,2,3),(4,5,6)])
# print(arr)

# arr=np.array([(1,2,3),(5,6,7)])
# print(arr)

#Array Creation using methods(empty, zeroes, ones)
# import numpy as np
#Creating a 1-D Numpy Array
# arr=np.array([(1,2,3,4,5)])
# print("Creating of 1-D Array")
# print(arr)
# print(type(arr))

# arr1=np.array([(1,2,3),(5,6,7)])
# print(arr1)
# print(type(arr1))
# print("\n")

#1. empty() function created array with random garbage values
# arr2=np.empty([3,2], dtype=int) #empty array
# print("creating Numpy array with empty method and Zeroes method")
# print(arr2)
# print("\n")

# arr2=np.empty([2,3],dtype=int)
# print(arr2)

# arr2=np.empty([3,3],dtype=int)
# print(arr2)

# arr3=np.zeros((2,3))
# print(arr3)

# arr3=np.zeros((2,4))
# print(arr3)

#Feature of Numpy Array
#Important Feature of Numpy:
#1. High-Perfomance N-Dimensional Array Object
#a. 1-D Array
#b. 2-D array
#2. It Contains tools for Integrating code from C/C++ and Fotran
#3. It Contains a Multi-Dimensional container for Generic Data
#4. Additional Linear Algebra, Fourier Transformation and Random Numbers capabilities
#5. It Contains of Broadcasting Functions

#We use python numpy array instead of list because of the three reasons
#1. Less Memory
#2. Fast
#3. Convenient

#1. Less Memory :
# import numpy as np
# import time
# import sys
# S=range(1000)
# print(type(S))
# print(sys.getsizeof(S)*len(S))
# D=np.arange(1000)
# print(type(D))
# print(D.size*D.itemsize)

# import numpy as np
# import time 
# import sys
# S=range(1000)
# print(type(S))
# print(sys.getsizeof(S)*len(S))

# D=np.arange(1000)
# print(type(D))
# print(D.size*D.itemsize)

# import numpy as np
# import time
# import sys
# S=range(1000)
# print(type(S))
# print(sys.getsizeof(S)*len(S))

# import numpy as np
# import sys
# import time
# S=range(1000)
# print(type(S))
# print(sys.getsizeof(S)*len(S))

# import numpy as np
# import sys
# import time
# s=range(1000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))

# d=np.arange(1000)
# print(type(s))
# print(d.size*d.itemsize)

# import numpy as np
# import sys
# import time
# s=range(1000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))
# d=np.arange(1000)
# print(type(s))
# print(d.size*d.itemsize)

# import numpy as np
# import time
# import sys
# s=range(10000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))

# d=np.arange(10000)
# print(type(d))
# print(d.size*d.itemsize)

#2. Faster
import numpy as np
import time
import sys
SIZE=1000000
l1=range(SIZE)
l2=range(SIZE)
a1=np.arange(SIZE)
a2=np.arange(SIZE)

start=time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start=time.time()
result=a1+a2
print((time.time()-start)*1000)

#Difference
#1. Once a Numpy array is created, we cannot change its size, but list size can be changed
#2. Numpy array contains elements of homogenuous type, Python list elements contains Homogenuous as well as Heterogenuous types
#3. Numpy array occupies much less space and memory consumption than a python list

#Ndarray(Numpy array data) N-Dimensional array. 
#an Ndarray is a(usually fixed-size) multidimensional container of items of the same data types and size
#An array object in Numpy is called ndarray.
#syntax : numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
#parameter and Description
#1. 1-D array
# import numpy as np
# a=np.array([10,20,30])
# print(a)

#2. 2-D array
# a=np.array(([1,2,3],[3,4,5]))
# print(a)

#3. 3-D Array
# a=np.array((([1,2,3],[4,5,6],[6,7,8])))
# print(a)

#4. using dtype parameter
# a=np.array([1,2,3,4,5],dtype=complex)
# print(a)

#Creating Arrays from Scratch
#for larger arrays, it is more effiecient to create arrays from scratch using routines built into NumpY
import numpy as np
# print("Create a length-10 integer array titled with zeroes...")
# a=np.zeros(10, dtype=int)
# print(a)

# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.ones((3,2), dtype=int)
# print(a)
# a=np.ones((2,3), dtype=int)
# print(a)

# a=np.ones((3,4),dtype=int)
# print(a)
# a=np.ones((2,3), dtype=int)
# print(a)
# a=np.ones((2,3),dtype=int)
# print(a)
# a=np.ones((2,1), dtype=int)
# print(a)
# a=np.ones((3,2), dtype=int)
# print(a)

# a=np.full((3,4),9.82)
# print(a)
# a=np.full((3,2), 9.90)
# print(a)
# a=np.full((4,3), 6.07)
# print(a)
# a=np.full((2,3), 9.99)
# print(a)

# import numpy as np
# print("Create an array filled with a linear sequence, \nStarting at 0, ending at 20, stepping by 3 \n(this is similar to the built-in range() function)")
# d=np.arange(0,20,3)
# print(d)

# print("Create an array of five values evenly spaced between 1 and 2")
# e=np.linspace(1,2,5)
# print(e)

# import numpy as np
# print("Create an array filled with a linear sequence, \nStarting at 0, ending at 20, stepping by 3 \n(this is similar to the built-in range() function)")
# d=np.arange(0,20,3)
# print(d)

# import numpy as np
# d=np.arange(0,23,3)
# print(d)

# import numpy as np
# d=np.arange(0,24,3)
# print(d)

# import numpy as np
# d=np.arange(0,21,3)
# print(d)

# import numpy as np
# e=np.linspace(1,2,5)
# print(e)
# import numpy as np
# e=np.linspace(0,20,5)
# print(e)
# import numpy as np
# e=np.linspace(0,18,4)
# print(e)

# #random
# print("Create a 3*3 array of uniformly distributred random values between 0 and 1")
# f=np.random.random((3,3))
# print(f)
# f=np.random.random((2,3))
# print(f)
# f=np.random.random((4,4))
# print(f)
# a=np.random.random((1,2))
# print(a)

# print("Create a 3*3 array of normally distributed random values\nWith mean 1 and Standard deviation 2")
# g=np.random.normal(1,2,(3,3))
# print(g)
# g=np.random.normal(1,2,(3,3))
# print(g)
# g=np.random.normal(1,2,(3,4))
# print(g)

# print("Create a 3*3 array of random integers in the interval[1,10]")
# h=np.random.randint(1,10,(3,3))
# print(h)
# h=np.random.randint(1,10,(3,4))
# print(h)
# h=np.random.randint(1,8,(3,4))
# print(h)
# h=np.random.randint(1,5,(1,2))
# print(h)
# h=np.random.randint(1,9,(2,3))
# print(h)

# print("Create a 3*3 identity matrix:")
# i=np.eye(3)
# print(i)
# d=np.eye(3)
# print(d)
# d=np.eye(3)
# print(d)
# d=np.eye(4)
# print(d)
# s=np.eye(3,3)
# print(s)
# s=np.eye(4)
# print(s)
# s=np.eye(2)
# print(s)

# print("Create an uninitialized array of three integers:\nThe values will be whatever happens to already exist at that memory location")
# j=np.empty(3)
# print(j)
# j=np.empty(3)
# print(j)
# j=np.empty(4)
# print(j)
# j=np.empty(4)
# print(j)
# a=np.empty(3)
# print(a)
# b=np.empty(5)
# print(b)

