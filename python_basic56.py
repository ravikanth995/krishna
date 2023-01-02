#NumPy is an open source module of python that offers functions and routines for fast mathematical computation on array and matrices.
#NumPy was created in 2005 by Travis Oliphant.
#The Array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy
#NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficientky

#Creation of NumPy Array
#1. 1-D array
import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)
# print(type(arr))

#2. 2-D array
# arr=np.array(([1,2,3,4],[5,6,7,8]))
# print(arr)
# print(type(arr))

#3. empty method
# arr=np.empty([1,2,3],dtype=int)
# print(arr)
# arr=np.empty([4,3],dtype=int)
# print(arr)
# arr=np.empty([3,3],dtype=int)
# print(arr)
# arr=np.empty([2,3], dtype=int)
# print(arr)
# arr=np.empty([2,4], dtype=int)
# print(arr)
# arr=np.empty([3,2],dtype=int)
# print(arr)

#zeroes method
# arr=np.zeros([2,3])
# print(arr)
# arr=np.zeros([2,3])
# print(arr)
# arr=np.zeros([9,7])
# print(arr)
# arr=np.zeros([4,3])
# print(arr)

#Feature of NumPy Array
#1. High-Performance N-Dimensional array Object: It is a Homo-genuous array object.
      #a. : single row*column.
      #b. : Multi-dimensional we consider each column as dimension. Homogenuous

#2. It Contains tools for integrating code from C/C++ and fotran: It helps in implement inter-platform functions
#3. It Contains Multi-dimensional container for generic data: genetic data refers to the parameterized data type of arrays, parameters help in increase the diverisity of the arrays.
#4. It contains of broadcasting functions.: useful concept when we work with arrays of uneven shapes. 
    #rules: for broacasting one of the arrays needs to be one-dimensional or both the arrays are supposed to be of the same shape.


# val=[23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5]
# c=np.array(val)
# print(c)
# print(c*9/5+32) : converting arrays of temperature celsius into farhenheit

# val=[1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.0]
# c=np.array(val)
# print(c)
# print(c*9/5+32)
# print(c)
# print(type(c))

#Python NumPy Array v/s List.
#1. Less Memory
#2. Fast 
#3. Convenient
 
#The very first reason to choose python NumPy array is that it(NumPy) occupies less memory as compared to list.
#Fast in term of execution and at the same time 
#It is very convenient to work with numpy

#1. Less Memory
# import numpy as np
# import sys
# import time
# print("For List")
# S=range(1000)
# print(S)
# print(type(S))
# print("It Occupies more memory:",sys.getsizeof(S)*len(S))

# print("let\'s see how NumPy array occupies less memory as compared to List")
# A=np.arange(1000)
# print(type(S))
# print("It Occupies Less Memory as Compared to List:",A.size*A.itemsize)
# import numpy as np
# import sys
# S=range(600)
# print(sys.getsizeof(S)*len(S))
# print(type(S))

# A=np.arange(600)
# print(A.size*A.itemsize)
# print(type(A))

#2. Fast and 3. Convenient
# import numpy as np
# import time
# import sys
# SIZE=1000000
# l1=range(SIZE)
# l2=range(SIZE)
# a1=np.arange(SIZE)
# a2=np.arange(SIZE)

# start=time.time()
# result=[(x,y) for x,y in zip(l1,l2)]
# print((time.time()-start)*1000)

# start=time.time()
# result=a1+a2
# print((time.time()-start)*1000)

# import sys
# import time
# import numpy as np
# Size=10000000
# l1=range(Size)
# l2=range(Size)
# a1=np.arange(Size)
# a2=np.arange(Size)

# start=time.time()
# result=[(x,y) for x,y in zip(l1,l2)]
# print((time.time()-start)*1000)

# start=time.time()
# result=a1+a2
# print((time.time()-start)*1000)

#1. Once a NumPy array is created, we cannot change its size, but list can be changed.
#2. NumPy array contains elements of homogeneous types. List Contains different data types or hetetogeneous or homogenous types
#3. NumPy array occupies much less space and memory consumption than a python list.


#Ndarray
#NumPy array data structure is also called ndarray.Ndarray means N-Dimensional array. 
#An ndarray is a(fixed-size) multi-dimensional container of items of the same data type and size
#An array object in NumPy is called ndarray. 
#Scalar Types
#Syntax. 
#numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
#Parameters and Description
#1. dtype : desired data type of arrays, optional
#2. copy : (optional). By default(true), the object is copied
#3. order : C(row major) or F(column major) or A(any)(default)
#4. subok : by default, returned array forced to be a base class array. if true, sub-class passed through
#5. ndmin : Specifies minimum demensions of resultant array


#1. 2-D array
import numpy as np
# a=np.array(([1,2,3],[3,4,5]))
# print(a)

#2. 3-D array
# a=np.array([(1,2,3),(4,5,6),(6,7,8)])
# print(a)
# a=np.array([(1,2,3),(5,7,6),(8,6,3)])
# print(a)

#3. Using data-type parameter
# a=np.array([1,2,3], dtype=int)
# print(a)
# a=np.array([10,20,30], dtype=complex)
# print(a)
# a=np.array([1,2,3], dtype=float)
# print(a)

#Creating Arrays from Scratch
#For larger arrays, it is more efficient to create arrays from scratch using routines built- into NumPy
print("Create a length-n integer array filled with zeroes")
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(5, dtype=int)
# print(a)
# a=np.zeros(3,dtype=int)
# print(a)
# a=np.zeros(9,dtype=int)
# print(a)

# print("Create a 3*4 floating-point array filled with ones")
# a=np.ones((3,4), dtype=float)
# print(a)
# a=np.ones((4,3), dtype=float)
# print(a)
# a=np.ones((2,3), dtype=float)
# print(a)
# a=np.ones((2,2), dtype=float)
# print(a)
# a=np.ones((3,5), dtype=float)
# print(a)

# print("Create a 3*4 array filled with 9.81")
# a=np.full((3,4), 9.99)
# print(a)
# a=np.full((2,2), 8.88)
# print(a)
# a=np.full((4,2), 5.55)
# print(a)
# a=np.full((2,1), 4.22)
# print(a)

#Example 3.
print("Create a 3*3 array of normally distributed random values\nWith mean 1 and Standard Deviation 2")
# g=np.random.normal(1,2,(3,2))
# print(g)
# g=np.random.normal(1,2,(3,4))
# print(g)
# a=np.random.normal((1,3),(3,3))
# print(a)
g=np.random.normal((1,2),(2,3))
print(g)