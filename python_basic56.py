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
# print("Create a length-n integer array filled with zeroes")
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
# print("Create a 3*3 array of normally distributed random values\nWith mean 1 and Standard Deviation 2")
# g=np.random.normal(1,2,(3,2))
# print(g)
# g=np.random.normal(1,2,(3,4))
# print(g)
# a=np.random.normal((1,3),(3,3))
# print(a)
# g=np.random.normal((1,2),(2,3))
# print(g)

#Array Attributes:
#1. Shape: This array attribute returns a tuple consisting of array dimensions. It can also be used to resize the array
import numpy as np
# a=np.array([[1,2,3,4],[4,5,6,6]])
# print(a.shape)
# a=np.array([[1,2,3],[3,4,5]])
# print(a.shape)
# a=np.array([[1,2,3],[4,5,6]])
# print(a.shape)
# a.shape=(3,2)
# print(a)
# print(a.reshape(2,3))

# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# a.shape=(3,2)
# print(a)
# print(a.reshape(2,3))

# a=np.array([[1,2,3],[5,4,3]])
# print(a)
# (a.shape)=(3,2)
# print((a.reshape(2,3)))
# a=np.array([[1,2,3],[4,5,6]])
# print(a.shape)
# a.shape=(3,2)
# print(a)

# a=np.array([[1,2],[3,4],[5,6]])
# print(a)
# a.shape=(2,3)
# a.reshape(3,2)
# print(a.reshape(3,2))

# a=np.array([[2,3,4],[6,4,1]])
# print(a)
# a.shape=(3,2)
# print(a.reshape(3,2))

#ndim : This array attribute returns the number of arrays dimensions
# An Array of evenly spaced numbers
import numpy as np
# a=np.arange(12)
# print(a)

#One-Dimensional Array
# a=np.arange(24)
# print(a)
# a.ndim
# #now reshape
# b=a.reshape(2,4,3)
# print(b)

# a=np.arange(24)
# print(a)
# a.ndim
# b=a.reshape(2,4,3)
# print(b)

# a=np.arange(24)
# a.ndim
# b=a.reshape(2,4,3)
# print(b)
# a=np.arange(24)
# a.ndim
# b=a.reshape(2,4,3)
# print(b)

# a=np.arange(24)
# a.ndim
# b=a.reshape(2,4,3)
# print(b)
# a=np.arange(24)
# a.ndim
# b=a.reshape(3,4,2)
# print(b)

# a=np.arange(24)
# a.ndim
# b=a.reshape(2,4,3)
# print(b)
# a=np.arange(24)
# a.ndim
# b=a.reshape(3,2,4)
# print(b)

#itemsize : This array attribute returns the length of each element of arrays in bytes
#dtype of array is int8(1byte)
# a=np.eye(2, dtype=int)
# print("2 rows in the Output:\n",a)
# a=np.eye(2,dtype=int)
# print(a)
# a=np.eye(2, dtype=int)
# print("2 rows in the Output:\n",a)
# a=np.eye(3,dtype=int)
# print(a)
# a=np.eye(3, k=1)
# print(a)
# a=np.eye(3, k=1)
# print(a)

#Identity: The Identity array is a square array with ones on the main diagonal.
#syntax= numpy.identity(n, dtype=None)
#Parameters --> n: int
        # Number of rows(and columns) in n*n output
     #dtype:data-type, optional
          # data-type of the output. Default to float

#Returns ---> out:ndarray
       #n*n array with its main diagonal set to one, and all other elements 0
# a=np.identity(3, dtype=int)
# print("3 rows:\n", a)

# a=np.identity(3, dtype=int)
# print(a)
# a=np.identity(3, dtype=int)
# print(a)

#default data type is float
#Zeroes
# floattype=np.zeros(6)
# print(floattype)
# floattype=np.zeros(4)
# print(floattype)

#int data type
# intType=np.zeros(4)
# print(intType)

# intType=np.zeros(9)
# print(intType)

#custom data type
# costType=np.zeros((2,2), dtype=[('x','i4'), ('y','i4')])
# print(costType)

# customType=np.zeros((3,3), dtype=[('x', 'i4'),('y','i4')])
# print(customType)
# customType=np.zeros((3,4), dtype=[('x','i4'),('y','i4')])
# print(customType)

#Ones
# defType=np.ones(6)
# print(defType)
# a=np.ones(7)
# print(a)

# a=np.ones([3,3], dtype=int)
# print(a)
# a=np.ones([3,3], dtype=int)
# print(a)
# a=np.ones([4.4], dtype=int)
# print(a)
# a=np.ones([2,2])
# print(a)
# a=np.ones([3,3], dtype=int)
# print(a)

#full
# a=np.full((3,3), 9.89)
# print(a)
# a=np.full((2,2), np.inf)
# print(a)
# a=np.full((3,2), np.inf)
# print(a)
# a=np.full((3,3), 9.99)
# print(a)

#Array From Existing data
#1. asarray(a,[,dtype, order]) : Convert the input to an array
#2. asmatrix(data,[,dtype]) : interpret the input as a matrix
#3. frombuffer(buffer[,dtype, count, offset]) : Interpret a buffer as a 1-D array
#4. fromfile(file[,dtype, count, sep, offset]) : Construct an array from data in a text or binary file
#5. fromiter(iterable, dtype, count=-1) : Create a new 1-D array from an iterable object
#6. copy(a,[order]) : Return an array copy of the Given Object

#1. asarray(a,[order]) : This Schedule is valuabale within the situation where we ought to change over a pythonn sequence into the numpy array object.
#Creating a numpy array using object
# l=[1,2,3,4,5,6,7,8,9]
# a=np.asarray(l)
# print(type(a))
# print(a)

# l=[1,2,3,4,5,6,7,8,9]
# a=np.asarray(l)
# print(type(a))
# print(a)

# l=[0,1,2,3,4,5,6,7,8,9]
# a=np.asarray(l)
# print(type(a))
# print(a)

#Creating a numpy array using Tuple
# t=(0,1,2,3,4,5,6,7,8,9)
# a=np.asarray(t)
# print(type(a))
# print(a)

# t=[1,2,3,4,5,6]
# a=np.asarray(t)
# print(type(a))
# print(a)

#Creating a Numpy array using more than one list
# l=[[1,2,3,4,5],[7,8,9]]
# a=np.asarray(l)
# print(type(a))
# print(a)

# l=[[1,2,3,4],[7,8]]
# a=np.asarray(l)
# print(type(a))
# print(a)

#2. asmatrix: It iterpretes the input as a matrix. Unlike, matrix, asmatrix does not make a copy if the input is already a matrix or an ndarray. It is equivalent to a matrix(data, copy=False)
# x=np.array([[10,20],[30,40]])
# print("x:\n",x)
# m=np.asmatrix(x)
# print("m:\n",m)
# x[0,0]=5
# print("After Changing m:\n",m)

# x=np.array([[10,20],[30,40]])
# print("x\n",x)
# m=np.asmatrix(x)
# print("m\n",m)
# x[0,0]=5
# print(m)

# x=np.array([[10,20,30],[40,50,60]])
# print(x)
# m=np.asmatrix(x)
# print(m)
# x[0,1]=7
# print(m)

# x=np.array([[9,7,4],[3,5,4]])
# print(x)
# m=np.asmatrix(x)
# print(m)
# x[0,2]=90
# print(m)
# print(x)

# x=np.array([[20,10,30],[40,50,59]])
# print(x)
# m=np.asmatrix(x)
# print(m)
# x[0,1]=19
# print(m)

#2. frombuffer : It interpretes a buffer as a 1-D array
#Note : If the Buffer has data that is not in machine byte-order, this should be spacified as part of the data-type

#Initialize bytes
# l=b'Tbalaji'
# print(type(l))

# a=np.frombuffer(l, dtype="S1")
# print(a)
# print(type(a))

import numpy as np
# x=b"Ravikanth"
# a=np.frombuffer(x, dtype='S1', count=5)
# print(a)

# x=b"RaviKa"
# a=np.frombuffer(x, dtype="S1", count=6)
# print(a)

#fromfile : An extremely pro-effiecient way of reading binary data with a known data-type , as well as parsing simply formatted text files.
#- Data written using the tofile() can be read using fromfile()
import numpy as np
import tempfile as tf
#Construct an array
# dt=np.dtype([('time', [('min', np.int64),('sec',np.int64)]),('temp',float)])
# x=np.zeros((1,), dtype=dt)
# x['time']['min']=11; x['temp']=95.21
# print(x)

# dt=np.dtype([('time',[('min',np.int64),('sec',np.int64)]),('temp', float)])
# x=np.zeros((1,),dtype=dt)
# x['time']['min']=11; x['temp']=95.21
# print(x)

dt=np.dtype([('time',[('min', np.int64),('sec',np.int64)]), ('temp',float)])
x=np.zeros((1,),dtype=dt)
x['time']['min']=11; x['temp']=95.21
print(x)