import numpy as np
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)

# arr=np.array([1,2,3,4])
# print(arr)
# print(type(arr))

#two-Dimensional Array
# arr=np.array([[1,2,3],[3,4,5]])
# print(arr)
# print(type(arr)

# arr=np.array([(1,2,3),(4,5,6)])
# print(arr)
#1. empty() --> Functions creates array with random garbage values
# arr=np.empty([3,2])
# print("Creating array with empty method and Zero method")
# print(arr)

# arr=np.empty([3,5])
# print(arr)

#2. zero method
# arr=np.zeros([3,2])
# print(arr)

#Features of Numpy
#1. High-Perfomance N-Dimensional Array Object
#a. 1-Dimension
#b. Multi-Dimensional Array
#2. It contains tools for integrating code from C\C++.
#3. It contains a multi-dimensional container for generic data. generic data : parameterized data types of arrays
#4. Additional linear, Fourier Transform and Random Number capabilities
#5. It Contains Broadcasting Functions

#Python NumPy v/s Python List
#We use python NumPy array instead of a list because of the below three reasons
#1. less memory
#2. Fast
#3. Convenient

#1. less memory
# import numpy as np
# import time
# import sys
# s=range(1000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))
# print("-"*30)
# d=np.arange(1000)
# print(type(d))
# print(d.size*d.itemsize)

# import numpy as np
# import sys
# import time
# s=range(1000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))
# print("*"*40)
# d=np.arange(1000)
# print(type(d))
# print(d.size*d.itemsize)

# import sys
# import time
# import numpy as np
# s=range(1000)
# print(type(s))
# print(sys.getsizeof(s)*len(s))
# print("-"*50)
# d=np.arange(1000)
# print(type(d))
# print(d.size*d.itemsize)

# import numpy as np
# import time
# import sys
# a=range(1000)
# print(sys.getsizeof(a)*len(a))
# print(type(a))
# print("-"*50)
# b=np.arange(1000)
# print(b.size*b.itemsize)
# print(type(b))

# #2. Fast
# import time
# import sys
# import numpy as np
# size=100000000
# l1=range(size)
# l2=range(size)
# start=time.time()
# result=[(x,y) for x,y in zip(l1,l2)]
# print(time.time()-start()*1000)
# print("-"*50)
# print("-"*40)
# a1=np.arange(size)
# a2=np.arange(size)
# start=time.time()
# result=a1+a2
# print((time.time()-start)*1000)

#1. Once a NumPy array is created, we cannot change its size, but list can be changed.
#2. NumPy array contains homogeneous types. 
#Python list contains elements of heterogenous or homogeneous types
#3. NumPy array occupies much less space and memeory consumption than a python list

#NumPy array data structure is also called ndarray. Ndarray means N-Dimensional array. 
#An ndarray is a(usually fixed-size)multi-dimensionally container of items of the same data and size.
#It describes the collection of items of the same type.
#Items inside the collection can be accessed using a zero-based index
#The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray ver easy
#dtype= Each Object in an ndarray takes the identical size of block inside the memory
# . each element in ndarray is an item of data-type object also known as dtype.
# Syntax:
#        np.array(object, dtype=None, copy=True, order=None, subok=False, mdmin=0)
#Object= Any object exposing the array interface method returns an array, or any(nested) sequence
# dtype= Desired data type of array, optional
# copy= optional. By default(true), the object is copied.
# order= C(row major) or F(column major) or A(any)(default)

#1-D NumPy array
import numpy as np
# a=np.array([1,2,3,4])
# print(a) 
# a=np.array([[1,2,3],[4,5,6]])
# print(a)

#3-D array
# a=np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(a)
# a=np.array([(1,2,3),(4,5,6),(6,7,8)])
# print(a)
# a=np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(a)
# a=np.array([10,20,30], dtype=None)
# print(a)
# a=np.array([10,20,30],dtype=int)
# print(a)
# a=np.array([10,20,30],dtype=float)
# print(a)
# a=np.array([10,20,30],dtype=complex)
# print(a)
# a=np.array([10,20,30],dtype=str)
# print(a)
# a=np.array([10,20,30],dtype=list)
# print(a)
# a=np.array([10,20,30],dtype=None)
# print(a)

#Creating arrays from scratch
#Especially for larger arrays, it is more efficient to create arrays from scratch using routines built into NumPy
# print("Create a length-10 integer array filled with zeroes...")
import numpy as np
# a=np.zeros(10,dtype=int)
# print(a)
# a=np.zeros(10,dtype=float)
# print(a)
# a=np.zeros(9, dtype=int)
# print(a)
# a=np.zeros(10, dtype=int)
# print(a)
# a=np.zeros(11, dtype=int)
# print(a)
# a=np.zeros(10,dtype=int)
# print(a)

# print("Create a r*c floating-point array filled with ones")
# a=np.ones((3,4), dtype=float)
# print(a)
# a=np.ones((4,5),dtype=int)
# print(a)
# a=np.ones((2,3), dtype=float)
# print(a)
# a=np.ones((3,4), dtype=None)
# print(a)
# a=np.ones((3,4), dtype=None)
# print(a)
# a=np.ones((3,5), dtype=None)
# print(a)

# print("Create a 3*4 array filled with 9.91")
# a=np.full((3,4),9.81)
# print(a)
# a=np.full((3,2), 9.77)
# print(a)
# a=np.full((4,3), 8.88)
# print(a)

#2. 
# print("Create an array filled with a linear sequence,\nStarting at 0, ending at 20, stepping by 3\n(This is similar to the built-in range() function")
# a=np.arange(0,20,3)
# print(a)
# a=np.arange(20)
# print(a)

#3. 
# print("Create a 3*3 array of uniformly distributed random values between 1 and 2")
# a=np.random.random((3,3))
# print(a)
# a=np.random.random((3,4))
# print(a)
# a=np.random.random((5,4))
# print(a)
# a=np.random.random((4,3))
# print(a)
# a=np.random.random((2,3))
# print(a)
# a=np.random.random((3,2))
# print(a)
# a=np.random.random((2,1))
# print(a)

# print("Create 3*3 array of normally distributed random values \nWith mean 1 and standard deviation 2")
# g=np.random.normal(1,2,(3,4))
# print(g)
# g=np.random.normal(1,2,(4,3))
# print(g)
# g=np.random.normal(2,3,(2,3))
# print(g)
# a=np.random.normal(3,2,(1,2))
# print(a)
# a=np.random.normal(2,1,(3,2))
# print(a)

# print("Create a 3*3 array random integers in the interval[1,10]")
# g=np.random.randint(1,10,(3,3))
# print(g)
# a=np.random.randint(1,10,(2,3))
# print(a)
# a=np.random.randint(1,10,(3,3))
# print(a)
# g=np.random.randint(2,8,(3,3))
# print(g)
# g=np.random.randint(1,8,(2,3))
# print(g)
# a=np.random.randint(2,18,(5,5))
# print(a)

#4.
# print("Create a 3*3 identity matrix")
# a=np.eye(3)
# print(a)
# a=np.eye(4)
# print(a)
# a=np.eye(3)
# print(a)
# a=np.eye(4)
# print(a)
# a=np.eye(3)
# print(a)
# a=np.eye(8)
# print(a)
# a=np.eye(4)
# print(a)
# a=np.eye(5)
# print(a)
# a=np.eye(2)
# print(a)
# a=np.eye(4)
# print(a)
# a=np.eye(3)
# print(a)
# a=np.eye(4)
# print(a)

# a=np.empty(3)
# print(a)
# a=np.empty(3)
# print(a)
# a=np.empty(4)
# print(a)

#Array Attributes
#1. Shape()
#This array attributes returns a tuple consisting of array dimensions. it can also be used to resize the array
import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a.shape)
# a=np.array([[1,2,3],[4,5,6]])
# a.shape=(3,2)
# # print(a.shape)
# print(a)
#1. An array of evenly spaced numbers
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.reshape(3,2))

#2. ndim
#This array attribute returns the mumber of array dimensions
#1. An array of evenly spaced numbers'
# a=np.arange(12)
# print(a)
# a=np.arange(13)
# print(a)
# a=np.arange(13)
# print(a)

#2. One dimension array
# a=np.arange(24)
# print(a.ndim)
# #now reshaping it
# b=a.reshape(2,3,4)
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

# a=np.arange(12)
# a.ndim
# b=a.reshape(2,2,3)
# print(b)
# a=np.arange(24)
# a.ndim
# b=a.reshape(2,3,4)
# print(b)

# a=np.arange(28)
# a.ndim
# b=a.reshape(2,4,3)
# print(b)

#3. itemsize
#This array returns the length of each element of arrays in bytes
#1. dtype of arrays is int8(1byte)
# a=np.array([1,2,3,4], dtype= np.int8)
# print(a.itemsize)

# a=np.array([1,2,3,4], dtype=np.int8)
# print(a.itemsize)
# a=np.array([1,2,3,4], dtype=np.int8)
# print(a.itemsize)
# a=np.array([1,2,3,4,5], dtype=np.int8)
# print(a.itemsize)

#2. dtype of arrays is now float32 bytes(4 bytes)
# a=np.array([1,2,3,4,5], dtype=np.float32)
# print(a.itemsize)
# a=np.array([1,2,3,4,5], dtype=np.float32)
# print(a.itemsize)
# a=np.array([10,20,30,40,50])
# print(a.flags)

#Array Creation Routines
#1. empty : It creates an uninititated array of specified shape and dtype
#The elements in an array show random values as they are not initialized.
#syntax: empty(shape[,dtype, order])
# a=np.empty([3,4], dtype=int)
# print(a)
# a=np.empty([3,4], dtype=int)
# print(a)
# a=np.empty([3,2], dtype=int)
# print(a)
# a=np.empty([3,3], dtype=int)
# print(a)
# a=np.empty([3,4], dtype=int)
# print(a)

#2. Eye: it returns a 2-D array with ones on the diagonal and zeros else where
#syntax: np.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')[source]
#N=int : Number of rows in the output
#M=int, optional: Number of columns.
#k=int, optional: index of the diagonal; 0(the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.
# dtype=data-type
# order{'C','F'}, optional
# a=np.eye(2, dtype=int)
# print("2 rows in the output:\n",a)
# a=np.eye(3,k=1)
# print("3 rows in the output:\n",a) 

# a=np.eye(2, dtype=int)
# print(a)
# a=np.eye(3, k=1)
# print(a)

# a=np.eye(3, dtype=int)
# print(a)
# a=np.eye(3, k=1)
# print(a)

# a=np.eye(3, dtype=int)
# print(a)
# a=np.eye(3,k=1)
# print(a)

#identity: identity array is a square array with ones on the main diagonal
#np.identity(n, dtype=None)
#n= Number of rows(and columns) in n*n output. default dtype is float
# a=np.identity(3, dtype=int)
# print("3 rows :\n",a)
# a=np.identity(4)
# print("4 rows :\n",a)
# a=np.identity(3, dtype=int)
# print("3 rows and columns:\n",a)
# a=np.identity(4)
# print("4 rows and columns:\n",a)

# a=np.identity(3, dtype=int)
# print("3 rows:\n",a)
# a=np.identity(4)
# print(a)

# a=np.identity(3, dtype=int)
# print("3 rows and 3 columns:\n",a)
# a=np.identity(4)
# print("4 rows and 4 columns:\n",a)

# a=np.identity(3, dtype=int)
# print(a)
# a=np.identity(4)
# print(a)

a=np.identity(3, dtype=int)
print("3 rows and columns:\n",a)
a=np.identity(4)
print("4 rows and colums:\n",a)