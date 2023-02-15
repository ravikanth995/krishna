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

# a=np.identity(3, dtype=int)
# print("3 rows and columns:\n",a)
# a=np.identity(4)
# print("4 rows and colums:\n",a)
# import numpy as np
# a=np.identity(3, dtype=int)
# print("3 Rows and columns:\n",a)
# a=np.identity(4)
# print("4 rows and columns:\n",a)

#4. zeros: it returns a nwe array of specified size which is filled with zeros
#syntax: np.zeros(shape, dtype, order)
#shape: shape of the array , e.g., (2,3)or 2
#dtype: desired data type for the array, e.g., np.int8 default is np.float64
#1. default data type is float
import numpy as np
# floatType=np.zeros(6)
# print("The float data type is:",floatType)
# a=np.zeros(4)
# print("4 zeros:\n",a)

#int data type
# intType=np.zeros((5,), dtype=np.int)
# print("Int data type is:\n",intType) 
# a=np.zeros((4,),dtype=int)
# print("The int data type is:\n",a)

# a=np.zeros((8,), dtype=int)
# print(a)
# a=np.zeros((9,),dtype=int)
# print(a)
# a=np.zeros((5,), dtype=complex)
# print(a)
# a=np.zeros((6,),dtype=int)
# print(a)

#custom data type
# custType=np.zeros((2,2), dtype=[('x','i4'), ('y','i4')])
# print("Custom data type is:\n",custType)

#ones: returns a new array of specified size and type which filled with ones
#np.ones(shape, dtype, order)
#arrayy of six ones Default dtype is float
# a=np.ones(5)
# print("default dtype is:\n",a)

# a=np.ones([2,3], dtype=int)
# print("int data type is:\n",a)

#5. full: it returns a new array of given shape and type which filled with fill_value
#np.full(shape,fill_value, dtype=None, order='C')
# a=np.full((2,3), 11)
# print(a)
# a=np.full((3,3), 11)
# print(a)

#Array from existing Data
#NumPy Provides us the way to create an array by using the existing data. 
#1. asarray(a[,dtype, order]) : Converts the input to an array
#2. asmatrix(data,[,dtype]) : Interpret the input as a matrix
#3. frombuffer(buffer[,dtype, count, offset]) : Interprets a buffer as a 1-D array
#4. fromfile(file,[dtype, count, sep, offset]) : construct an array from data in a text or binary file
#5. fromiter(iterable, dtype, count=-1): create a new 1-D array from an iterable object
#6. copy(a,[order]): return an array copy of the given object

#1. asarray : This schedule is utilized to generate an array by using the existing data within the form of lists or tuples.
     #This schedule is valuable within the situation where we ought to change over a python sequence into the numpy array object
#syntax --> asarray(a,[,dtype, order])
#creating numpy array using the list.
# l=[1,2,3,4,5]
# a=np.asarray(l)
# print(type(a))
# print(a)
# l=[1,2,3,4,5]
# a=np.asarray(l)
# print(a)
# print(type(a))

# l=[1,2,3,4,5,6]
# a=np.asarray(l)
# print(type(a))
# print(a)

#creating a numpy array using tuple
# t=(1,2,3,4,5,6,7,8)
# a=np.asarray(t)
# print(type(a))
# print(a)
# l=(1,2,3,4,5,6,7,8,9)
# a=np.asarray(l)
# print(type(a))
# print(a)
# l=(1,2,3,4,5,6,7,8,9)
# a=np.asarray(l)
# print("Data type of the list is:\n",type(a))
# print(a)

#creating a numpy array using more than one list
# l=[[1,2,3,4,5,6,7],[8,9,10]]
# a=np.asarray(l)
# print("Type of Data:\n",a)
# print(a)
# l=[[1,2,3,4,5,6],[7,8,9]]
# a=np.asarray(l)
# print("data type:\n",type(a))
# print("list into array:",a)
# l=[[1,2,3],[4,5,6,7,8,9]]
# a=np.asarray(l)
# print('Data type:\n',type(a))
# print(a)

#2. asmatrix: It interpretes the input as a matrix. Unlike, matrix, asmatrix doesn't make a copy if the input is already a matrix or an ndarray
#it is equivalent to a matrix(data=False)
#syntax: asmatrix(data=dtype=None)
# a=np.array([[10,20],[30,40]])
# print("s:\n",a)
# b=np.asmatrix(a)
# print("b:\n",b)
# a[0,0]=5
# print("After Changing b:\n",b)
# print("After Change a:\n",a)

# a=np.array([[10,20],[40,50]])
# print("a:\n",a)
# b=np.asmatrix(a)
# print("b :\n",b)
# a[0,0]=4
# print("After changing --b :\n",b)

# a=np.array([[1,2,3],[5,4,1]])
# print("a before change:\n",a)
# b=np.asmatrix(a)
# print("b copied:\n",b)
# a[0,1]=9
# print("b after mutate:\n",b)

#3. frombuffer : It interpretes buffer as a 1-D array
#syntax: np.frombuffer(buffer, dtype=float, count=-1, offset=0)
#Note: If the buffer has data that is not in machine byte-order, this should be specified as part of the data-type
#Initialize byte
# l=b'Cravikanth!'
# print(type(l))
# a=np.frombuffer(l, dtype="S1")
# print(type(a))
# print(a)
# l=b'CSonuNigam'
# print(type(l))
# a=np.frombuffer(l, dtype="S1")
# print(type(a))
# print(a)

l=b"Hello World"
# print(type(l))
# print(l)
# a=np.frombuffer(l, dtype="S1")
# print(a)
# arr=np.frombuffer(l, dtype="S1", count=5)
# print(arr)
# arr=np.frombuffer(l, dtype="S1",count=3)
# print(arr)
# arr=np.frombuffer(l, dtype="S1", count=7)
# print(arr)

# arr=np.frombuffer(l, dtype="S1", count=6, offset=2)
# print(arr)
# arr=np.frombuffer(l, dtype="S1", count=4, offset=5)
# print(arr)

#4. fromfile: It constructs an array from data in a text or binary file
#syntax: np.fromfile(file, dtype=float, count=-1, sep=" ", offset=0)
import tempfile
#Construct an ndarray
# dt=np.dtype([('time',[('min', np.int64),('sec',np.int64)]), ('temp', float)])
# x=np.zeros((1,), dtype=dt)
# x['time']['min']=11; x['temp']=96.74
# print(x)
# dt=np.dtype([('time',[('min', np.int64), ('sec',np.int64)]), ('temp',float)])
# x=np.zeros((1,), dtype=dt)
# x['time']['min']=11; x['temp']=96.05
# print(x)
# dt=np.dtype([('time',[('min', np.int64),('sec',np.int64)]), ('temp',float)])
# x=np.zeros((1,), dtype=dt)
# x['time']['min']=11; x['temp']=99.99
# print(x)

# #Saving the raw data to disk
# fname=tempfile.mkstemp()[1]
# print(fname)
# x.tofile(fname)

# import numpy as np
# import tempfile
# # dt=np.dtype([('time',[('min',np.int64),('sec',np.int64)]), ('temp',float)])
# # x=np.zeros((1,), dtype=dt)
# # x['time']['min']=11; x['temp']=19.98
# # print(x)

# import numpy as np
# import tempfile
# dt=np.dtype([('time',[('min',np.int64),('sec',np.int64)]), ('temp',float)])
# x=np.zeros((1,), dtype=dt)
# x['time']['min']=12; x['temp']=99.12
# print(x)
# #Saving raw data to disk
# # fname=tempfile.mkstemp()[1]
# # print(fname)
# # x.tofile(fname)
# # filename=tempfile.mkstemp()[-1]
# # print(x)
# # x.tofile(filename)
# filename=tempfile.mkstemp()[-1]
# print(x)
# x.tofile(filename)
# #reading raw data from disk
# np.fromfile(filename, dtype=dt)
# #the recommanded way to store and load data
# np.save(filename, x)
# print(np.load(filename+'.npy'))

# import numpy as np
# import tempfile
# dt=np.dtype([('time',[('min',np.int64), ('sec',np.int64)]),('temp',np.int64)])
# x=np.zeros((1,),dtype=dt)
# x['time']['min']=11; x['temp']=89.23
# print(x)
# #saving the raw data to disk
# fname=tempfile.mkstemp()[1]
# print(fname)
# x.tofile(fname)
# #read the data from disk
# np.fromfile(fname,dtype=dt)
# #store and load data
# np.save(fname, x)
# print(np.load(fname+'.npy'))

# import numpy as np
# import tempfile
# dt=np.dtype([('time',[('min',np.int64),('sec',np.int64)]),('temp',np.int64)])
# x=np.zeros((1,),dtype=dt)
# x['time']['min']=99.1; x['temp']=99
# print(x)
# #save the raw data to disk
# fname=tempfile.mkstemp()[1]
# print(fname)
# x.tofile(fname)
# #read the raw data from disk
# np.fromfile(fname, dtype=dt)
# #load the data from disk
# np.save(fname,x)
# print(np.load(fname+'.npy'))

# import numpy as np
# import tempfile
# dt=np.dtype([('time',[('min',np.int64), ('sec',np.int64)]),('temp',float)])
# x=np.zeros((1,),dtype=dt)
# x['time']['min']=9; x['temp']=11.09
# print(x)
# #save raw data to the disk
# fname=tempfile.mkstemp()[1]
# print(fname)
# x.tofile(fname)
# #read the data
# np.fromfile(fname, dtype=dt)
# #load the data from disk
# np.save(fname,x)
# print(np.load(fname+'.npy'))

# import numpy as np
# import tempfile
# dt=np.dtype([('time',[('min',np.int64), ('sec',np.int64)]),('temp',float)])
# x=np.zeros((1),dtype=dt)
# x['time']['min']=11.22; x['temp']=11.72
# print(x)
# #save the data to the disk
# fname=tempfile.mkstemp()[1]
# print(fname)
# x.tofile(fname)
# #read the raw data from disk
# np.fromfile(fname,dtype=dt)
# #load the raw data from the disk
# np.save(fname,x)
# print(np.load(fname+'.npy'))

#from iter() function : used to create a new 1-D array from an iterable object
#syntx: np.fromiter(iterable, dtype, count=1)
#obtain an iterator pbject from list
import numpy as np
# list=range(4)
# iterator=iter(list)
# #use iterator to create ndarray
# x=np.fromiter(iterator, dtype=float)
# print(x)

# list=range(7)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# # print(x)
# list=range(5)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=int)
# print(x)

# import numpy as np
# list=range(6)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)
# list=range(6)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)
# list=range(7)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)
# list=range(6)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)
# list=range(5)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)

# list=range(7)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)
# list=range(9)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)
# import numpy as np
# it=(x*x for x in range(5))
# #creating numpy from an iterable
# arr=np.fromiter(it, dtype=float)
# print(arr)

# td=(x*x for x in range(5))
# arr=np.fromiter(td, dtype=int)
# print(arr)
# dt=(x*x for x in range(5))
# n=np.fromiter(dt, dtype=float)
# print(n)

# td=(x*x for x in range(6))
# y=np.fromiter(td, dtype=float)
# print(y)

#copy: returns the copy of given object
#create an array x, with referrence y and a copy z:
# x=np.array([1,2,3])
# y=x
# z=np.copy(x)
# #note that, when we modifyx , y changes not z
# x[0]=9
# print("x[0]==y[0] is :",x[0]==y[0])
# print("x[0]==z[0] is:",x[0]==z[0])
# print(z)

# x=np.array([1,2,3,4])
# y=x
# z=np.copy(x)
# x[0]=9
# print(x[0]==y[0])
# print(x[0]==z[0])
# print(y)
# print(z)

# x=np.array([2,1,3,4,5])
# y=x
# z=np.copy(x)
# x[0]=7
# print(x[0]==y[0])
# print(x[0]==z[0])
# print(y)
# print(z)
# x=np.dtype([('time',[('min',np.int64),('sec',np.int64)]),('temp',np.int64)])
# y=np.zeros((1,),dtype=x)
# y['time']['min']=11; y['temp']=99.99
# print(y)
# #Save raw data to disk
# fname=tempfile.mkstemp()[1]
# print(fname)
# y.tofile(fname)
# #Read the raw data from disk
# np.fromfile(fname,dtype=x)
# #recommended way to store and load data
# np.save(fname,y)
# print(np.load(fname+'.npy'))

#From iter() function
#used to create a new 1-d array from an iterable object
# list=range(6)
# iterator=iter(list)
# x=np.fromiter(iterator,dtype=float)
# # print(x)

# list=range(7)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)

# list=range(8)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=int)
# print(x)
# list=range(8)
# iterator=iter(list)
# x=np.fromiter(iterator, dtype=float)
# print(x)

#2.
# y=(x*x for x in range(5))
# arr=np.fromiter(y, dtype=float)
# print(arr)
# y=(x*x for x in range(8))
# x=np.fromiter(y, dtype=float)
# print(x)

# y=(x*x*x for x in range(6))
# x=np.fromiter(y, dtype=int)
# print(x)

#copy
# x=np.array([1,2,3,4])
# y=x
# z=np.copy(x)
# x[0]=6
# print(x[0]==y[0])
# print(z[0]==y[0])
# x=np.array([1,2,3,4,5])
# y=x
# z=np.copy(x)
# x[0]=9
# print(x[0]==y[0])
# print(x[0]==z[0])
# print(x[2]==y[2])
# print(x[1]==z[1])

#Array from numerical ranges
#1. Arange()
# a=np.arange(1,20,2,dtype=float)
# print(a)
# a=np.arange(1,22,2,dtype=float)
# print(a)
# a=np.arange(0,20,2,dtype=float)
# print(a)

#2. linspace()
# a=np.linspace(0,20,num=5, endpoint=True)
# print(a)
# a=np.linspace(0,29,num=5,endpoint=True)
# print(a)
# a=np.linspace(1,30,num=3, endpoint=True, dtype=int)
# print(a)
# a=np.linspace(1,20,num=7, endpoint=True, dtype=float)
# print(a)
# a=np.linspace(1,20,num=5, endpoint=True, dtype=float)
# print(a)

# b=np.linspace(1,22,num=10,endpoint=True, dtype=float)
# print(b)
# a=np.linspace(1,22,num=10, endpoint=True, dtype=int)
# print(a)

#logspace
# a=np.logspace(1,22,num=8, endpoint=True, dtype=float)
# print(a)

# a=np.logspace(1,22,num=7, endpoint=True, dtype=float)
# print(a)

#Slicing
# a=np.array([1,2,3,4,5,6])
# print("Index 3 to last index valiue :",a[3:])
# print("Index 0 t0 3:",a[:3])
# print("Index 3(included) upto the index (excluded):",a[3:6])
# print("Value without last element:",a[:-1])
# print("Value without second last and last element:",a[:-2])
# print("All elements is in reverse order:",a[::-1])
# print("All even number reverse order:",a[::-2])
# print("All odd numbers in reverse order:",a[-2::-2])

# a=np.array([1,2,3,4,5,6,7,8])
# print("Index 3 to last value:",a[3:])
# print("Index 0 to 3:",a[:3])
# a=np.array([1,2,3,4,5,6,7])
# print("Index 3 and last index value:",a[3:])
# print("Index 0 to 3 index value:",a[:3])
# print("Index 3 upto index 6:",a[3:6])
# print("value without last element:",a[:-1:])
# print("value without second last and last element:",a[:-2])
# print("All elements in reverse order:",a[::-1])
# print("All even numbers in reverse order:",a[:1:-2])
# print(a[::])

# a=np.array([[1,2,3,4],[5,6,7,8],[10,12,13,14]])
# b=a[:2,1:3]
# r1=a[0,:]
# r2=a[0:3,:]
# print("Row 1, shape of row:\n",r1, r1.shape)
# print("Row 2, shape of row :\n",r2, r2.shape)
# a=np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])
# b=a[:1,1:2]
# r1=a[0,:]
# r2=a[0:3,:]
# print("Row 1, shape of the row:\n",r1,r1.shape)
# print("Row 2, shape of the row 2:\n",r2,r2.shape)
# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# b=a[:2,1:2]
# x=a[0,:]
# y=a[0:3,:]
# print("Row 1, shape of the row:\n",x,x.shape)
# print("Row 2, shape of the row 2:\n",y,y.shape)
# c1=a[:,1]
# c2=a[:,1:2]
# print("Column 1, shape of the column:\n",c1,c1.shape)
# print("Column 2, shape of the column 2:\n",c2,c2.shape)

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# x=a[2,:]
# y=a[0:3,:]
# print("Row 1, shape of the row 1:\n",x,x.shape)
# print("Row 2, shape of the row 2:\n",y,y.shape)
# c1=a[:,1:2]
# c2=a[:,0:3]
# print("Column 1, shape of the column:\n",c1,c1.shape)
# print("Column 2, shape of the column:\n",c2,c2.shape)
# x=a[1,:]
# y=a[0:3,:]
# print("Row 1, shape of the row 1:\n",x,x.shape)
# print("Row 2, shape of the row 2:\n",y,y.shape)
# c1=a[:,1]
# c2=a[:,1:2]
# print(c1,c1.shape)
# print(c2,c2.shape)

#indexing: it referes to the plave where the items of array are stored
#two types of index 
#1. integer
#2. Bolean 
#1. Integer: You can index into numpy using numpy slicing, the resulting array view will always be a sub-array of the original array.
#in contrast, the integer array index allows you to construct arbitrary arrays using the data from another array
# a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a[0,0],a[1,1],a[2,0])
# a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a[0,0],a[1,1],a[2,2],a[3,0])
# print(np.array([a[0,0],a[1,1],a[2,0]]))
# print(a[[0,0],[1,1]])
# print(np.array([a[0,1],a[0,1]]))

# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[0,0],a[1,1],a[2,2])
# print(np.array([a[0,0],a[1,1],a[2,2]]))
# print(a[[0,0],[1,1]])
# print(np.array([a[0,1],a[0,1]]))

# a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print("Array is a:\n",a)
# b=np.array([1,2,0])
# print(np.arange(3),b)
# print(np.arange(3),b)
# print(np.arange(3),b)
# print("-"*30)
# a[np.arange(3),b]+=10
# print(a)

#2. Boolean Array Indexing: It lets you pick out an arbitrary elements of an array
# a=np.array([[1,20],[0,40],[2,60]])
# bid=(a>2)
# print(bid)
# print(a[bid])
# print(a[a>2])

#Python program to demonstrate indexing in NumPy
# a=np.array([[1,2,3,4],[4,5,6,7],[6,7,8,9],[5,5,5,5]])
# print("Your Array is:\n",a)
# #Slicing array
# temp=a[:4,::2]
# print(temp)

# a=np.array([[1,2,3,4],[4,5,6,7],[6,7,8,9],[5,5,5,5]])
# # temp=a[:4,::2]
# # print("Temp file:\n",temp)
# #Integer Array Indexing Example
# temp=a[[0,1,2,3],[3,2,1,0]]
# print("Elements at indices (0,3),(1,2),(2,1),(3,0):\n",temp)
# b=a>0
# temp=a[b]
# print("\nElements greater than 0 is:",temp)

#Joining of arrays : Concatenation
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.concatenate((arr1,arr2))
# print("Concatenation:\n",arr)
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.concatenate((arr1,arr2))
# print("Array after Concatenation:\n",arr)
#2-d array Concatenation

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# arr=np.concatenate((arr1,arr2),axis=1)
# print(arr)
# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# arr=np.concatenate((arr1,arr2),axis=1)
# print("Array 1 and 2:\n",arr)

#Joining arrays using stack functions
#inplace of concatenation, we use stack() method, the difference is that stacking done along a new axis
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# # arr=np.stack([arr1,arr2], axis=1)
# # print(arr)
# arr=np.hstack((arr1,arr2))
# print(arr)
# arr3=np.vstack((arr1,arr2))
# print(arr)

#Splitting the array
#it breaks the one array into multiple
# arr=np.array([1,2,3,4,5,6,7])
# newArr=np.array_split(arr,4)
# print(newArr)
# arr=np.array([1,2,3,4,5,6,7,8])
# newArr=np.array_split(arr,3)
# print(newArr)
# arr=np.array([1,2,3,4,5,6])
# newArr=np.array_split(arr,2)
# print(newArr)
# arr=np.array([1,2,3,4,5,6,7,8,9])
# newArr=np.array_split(arr,3)
# print(newArr)
# arr=np.array([1,2,3,4,5,6,7])
# arrNew=np.array_split(arr,4)
# print(arrNew)

#Arithmetic operations on Array
# a=np.array([[1,2],[3,4]],dtype=int)
# b=np.array([[6,7],[3,2]],dtype=int)
# print("Addition of a and b are:",a+b)
# print("Addition of a and b using add(x,y):\n",np.add(a,b))
# print("-"*50)
# print("Subtraction of a and b are:",a-b)
# print("Subtraction using np.subtract:\n",np.subtract(a,b))
# print("-"*50)
# print("Multiplication of a and b are:",a*b)
# print("Multiplication of a and b using np.multiply(a,b)\n",np.multiply(a,b))
# print("-"*50)
# print("Division of a and b :",a/b)
# print("Division of a and b are using np.divide(a,b):\n",np.divide(a,b))
# print("-"*50)
# print("Square root of numbers :\n",np.sqrt(a))
# x=np.array([[10,20],[30,40]],dtype=int)
# y=np.array([[50,60],[100,120]],dtype=int)
# print("Addition of x and y:",x+y)
# print("Addition using np.add(x,y):\n",np.add(x,y))
# print("-"*50)
# print("Subtraction of x and y are:",x-y)
# print("Subtraction using np.subtract(x,y):;\n",np.subtract(x,y))
# print("-"*50)
# print("Multiplication of x and y are:",x*y)
# print("Subtract using np.multiply(x,y)\n",np.multiply(x,y))
# print("-"*50)
# print("Division of x and y are:",x/y)
# print("Division of x and y using np.divide(x,y):\n",np.divide(x,y))
# print("-"*50)
# print("Square root of x is:\n",np.sqrt(x))
# print("-"*50)
# print("Square root of y is:\n",np.sqrt(y))

# x=np.array([[9,16],[25,36]],dtype=int)
# y=np.array([[49,64],[81,100]],dtype=int)
# print("Addition of x and y:",x+y)
# print("Addition using np.add(x,y):",np.add(x,y))
# print("-"*50)
# print("Subtraction of x and y:",x-y)
# print("Subtraction using np.subtract(x,y):",np.subtract(x,y))
# print("-"*50)
# print("Multiplication of x and y:",x*y)
# print("Multiplication using np.multi(x,y):",np.multiply(x,y))
# print("-"*50)
# print("Divison of x and y:",x/y)
# print("Division using np.divide(x,y):",np.divide(x,y))
# print("-"*50)
# print("Square root of x:",np.sqrt(x))
# print("-"*50)
# print("Square root of y:",np.sqrt(y))

# x=np.array([[1,2],[3,4]])
# print("Sum of all elements:",np.sum(x))
# print("Sum of Columns is:",np.sum(x,axis=0))
# print("Sum of row elements:",np.sum(x,axis=1))
# x=np.array([[1,2],[4,5]])
# print("Sum of all elements:",np.sum(x))
# print("Sum of Columns is:",np.sum(x,axis=0))
# print("Sum of Rows are :",np.sum(x,axis=1))
# x=np.array([[1,2],[3,1]])
# print("Sum of all elements :",np.sum(x))
# print("Sum of Columns is:",np.sum(x,axis=0))
# print("Sum of Rows is:",np.sum(x, axis=1))

#Transpose of arrays
# x=np.array([[1,2,3],[4,5,6]])
# print("Matrix :",x)
# print("Transposed matrix:",x.T)
# ax=np.array([[1,2,3,4],[5,6,7,8]])
# print("Normal Matrix:",ax)
# print("Transposed Matrix:",ax.T)
# x=np.array([[1,2,3],[5,3,1]])
# print("Normal Matrix:",x)
# print("Transposed Matrix:",x.T)

# bx=np.array([1,2,3,4,5])
# print("Matrix:",bx)
# print("Transposed Matrix:",bx.T)

#NumPy Random
import numpy as np
import random
# l=[1,2,3,4,5,6]
# print(random.random())
# print(random.choice(l))
# l1=[1,2,3,4,5,6]
# print(random.choice(l1))
# print(random.random())

#Sorting and Searching
# a=np.array([[12,15],[10,1]])
# arr1=np.sort(a,axis=0)
# print("Along the First Axis:",arr1)
# a=np.array([[10,12],[2,5]])
# arr1=np.sort(a,axis=0)
# print("Sorted along first axis:",arr1)

#Sort along last axis
# a=np.array([[10,15],[12,1]])
# arr1=np.sort(a,axis=-1)
# print(arr1)

# a=np.array([[12,15],[10,1]])
# arr3=np.sort(a,axis=None)
# print(arr3)
# a=np.array([[10,12],[3,1]])
# arr1=np.sort(a,axis=None)
# print(arr1)
# a=np.array([[12,11],[9,2]])
# arr1=np.sort(a,axis=None)
# print(arr1)
# a=np.array([[[12,7],[8,3],[9,1],[8,3],[6,2]]])
# arr1=np.sort(a,axis=None)
# print(arr1)
# a=np.array([[[12,11],[10,9],[6,8],[5,4],[7,3],[2,1]]])
# arr1=np.sort(a, axis=None)
# print(arr1)

#numpy.argsort(): This returns the indices that would sort an array
# a=np.array([9,3,1,6,4,8,2])
# print("Unsorted Array:",a)
# b=np.argsort(a)
# print("Sorted Indices of original array:",b)
# c=np.zeros(len(b), dtype=int)
# for i in range(0, len(b)):
#      c[i]=a[b[i]]
# print("Sorted array:",c)     

# a=np.array([8,9,1,4,2,3,6,5,7,])
# print("Unsorted Array:",a)
# b=np.argsort(a)
# print("Sorted indices of array:",b)
# c=np.zeros(len(b), dtype=int)
# for i in range(0,len(b)):
#      c[i]=a[b[i]]
# print("Sorted Array:",c)     

# a=np.array([10,9,8,7,6,5,4,3,2,1])
# print("Unsorted Array:",a)
# b=np.argsort(a)
# print("Sorted Indices of Array:",b)
# c=np.zeros(len(b), dtype=int)
# for i in range(0,len(b)):
#      c[i]=a[b[i]]
# print("Sorted Array:",c)     

#np.lexsort: this function returns an indirect sort using a sequence of keys
# a=np.array([1,3,6,8,5,2,6,2,5])
# b=np.array([3,2,1,4,6,3,2,6,7])
# print("Column a, \bColumn b")
# for (i,j) in zip(a,b):
#      print(i," ",j)
# ind=np.lexsort((b,a))
# print("Sorted Indices:",ind)

# a=np.array([1,2,3,4,5,6,7,8,9])
# b=np.array([9,8,7,6,5,4,3,2,1])
# print("Column a,\bColumn b")
# for (i,j) in zip(a,b):
#      print(i, " ",j)
# ind=np.lexsort((b,a))
# print("Sorted Indices:",ind)     

# a=np.array([1,2,3,4,5,6,7,8,9])
# b=np.array([9,8,7,6,5,4,3,2,1])
# print("Column a,\bColumn b")
# for (i,j) in zip(a,b):
#      print(i,"",j)
# ind=np.lexsort((b,a))
# print("Sorted Arrays:",ind)     

# a=np.array([1,2,3,4,5,6,7,8])
# b=np.array([8,6,4,3,1,5,7,8])
# print("Column a,Column b")
# for (i,j) in zip(a,b):
#      print(i,"",j)
# ind=np.lexsort((b,a))
# print("Sorted Lexsort:",ind)    

# a=np.array([1,2,3,4,5,6,7,8,9]) 
# b=np.array([9,8,7,6,5,4,3,2,1])
# print("Column a, Column b")
# for (i,j) in zip(a,b):
#      print(i,"",j)
# ind=np.lexsort((b,a))
# print(ind)     

#NumPy vector : V
#Scalar : Single Numbber
# print(scalar)
# print(Scalar.shape)
# print(Scalar.ndim)

#Matrix 1-D array 
# matrix=np.array([
#      [1,2],
#      [3,4]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

# matrix=np.array([
#      [1,2],
#      [4,5]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

# matrix=np.array([
#      [2,3],
#      [6,4]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)
# print(matrix.size)

# matrix=np.array([
#      [3,2],
#      [5,7]
# ])
# print(matrix.shape)
# print(matrix)
# print(matrix.ndim)
# print(type(matrix))

# matrix=np.array([
#      [3,1],
#      [8,4]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

# matrix=np.array([
#      [1,3],
#      [6,4]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

# matrix=np.array([
#      [1,2],
#      [8,9]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

#Matrix 4*3
# matrix=np.array([
#      [1,2,3],
#      [4,5,6],
#      [7,8,9]
# ])
# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)
# matrix=np.array([
#      [3,2,1],
#      [6,5,4],
#      [9,8,7]
# ])
# print(matrix)
# print(matrix.ndim)
# print(matrix.ndim)
# print(matrix.T)

# matrix=np.array([
#      [1,2,3],
#      [4,3,1],
#      [5,6,3]
# ])
# print(matrix)
# print(matrix.ndim)
# print(matrix.shape)
# print(matrix.T)

#Tensor: Array more than 2-D array
# tensor=np.array([
#      [
#           [1,2,3],
#           [4,5,6]
#      ],
#      [
#           [5,4,3],
#           [8,5,9]
#      ]
# ])
# print(tensor)
# print(tensor.shape)
# print(tensor.ndim)
# print(tensor.T)

# tensor=np.array([
#      [
#           [1,2,3],
#           [5,4,3],
#           [9,8,6]
#      ],
#      [
#           [4,6,2],
#           [9,5,1],
#           [8,8,8]
#      ]
# ])
# print(tensor)
# print(tensor.shape)
# print(tensor.ndim)
# print(tensor.T)

# tensor=np.array([
#      [
#           [1,2,3],
#           [4,5,6],
#           [7,8,9]
#      ],
#      [
#           [1,2,3],
#           [4,5,6],
#           [7,8,9]
#      ]
# ])
# print(tensor)
# print(tensor.ndim)
# print(tensor.shape)

# tensor1=np.array([
#      [1,2,3],
#      [4,5,6],
#      [6,7,8]
# ])
# tensor2=np.array([
#      [1,3,2],
#      [5,6,7],
#      [7,6,3]
# ])
# print(tensor1)
# print(tensor2)
# tensor3=tensor1-tensor2
# print(tensor3)

# tensor1=np.array([
#      [1,2,3],
#      [4,5,6],
#      [6,5,3]
# ])
# tensor2=np.array([
#      [5,6,7],
#      [8,5,3],
#      [9,6,4]
# ])
# print(tensor1)
# print(tensor2)
# tensor3=tensor1+tensor2
# tensor4=tensor1-tensor2
# tensor5=tensor1*tensor2
# print(tensor3)
# print(tensor4)
# print(tensor5)

# v1=np.array([1,2,3])
# v2=np.array([3,2,1])
# np.dot(v1,v2)
# v3=v1+v2
# v4=v1-v2
# print(v3)
# print(v4)

# v1=np.array([4,6,1])
# v2=np.array([7,8,9])
# np.dot(v1,v2)
# v3=v1+v2
# v4=v1*v2
# print(v3)
# print(v4)

# dot=np.dot(4,5)
# print(dot)
# dot=np.dot(9,7)
# print(dot)
# dot=np.dot(5,6)
# print(dot)
# dot=np.dot(2,1)
# print(dot)
# dot=np.dot(9,8)
# print(dot)

#Vector
# vect1=np.array([4+7j])
# vect2=np.array([5+7j])
# np.dot(vect1,vect2)
# vect3=vect1+vect2
# vect4=vect1*vect2
# print(vect3)
# print(vect4)
# vect1=np.array([[1,2],[5,6]])
# vect2=np.array([[5,4],[9,8]])
# vect3=np.dot(vect1,vect2)
# print(vect3)

# A=np.array([[1,2,3,4],[5,6,7,8]])
# print(A)
# print(A.shape)
# print(A.T)
# print(A.size)
# print(A.ndim)

#matrix
# A=np.array([[[1,2,3,4],[5,6,7,8]],
#           [[10,11,12,13],[14,15,16,17]]])
# print(A)
# print(A.shape)
# print(A.ndim)
# print(A.size)
# print(A.T)          

A=np.array([[[1,2,3,4],[5,6,7,8],
          [10,11,12,13],[15,16,17,18]]])
print(A)
print(A.shape)
print(A.size)
print(A.ndim)          