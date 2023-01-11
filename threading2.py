# from threading import Thread
# def Disp(a,b):
#     print("Thread Running")
# t=Thread(target=Disp,args=(10,20))
# print(t)
# t.start()    

from threading import Thread, current_thread
# def Disp(a,b):
#     print("Thread Running")
# t=Thread(target=Disp, args=(10,20))
# print("Thread Name is",t)
# t.start()    

# def thread(a,b):
#     print("Thread Starts")
# t=Thread(target=thread, args=(20,40))
# print("Thread Name is:",t)
# t.start()   

# def disp(a,b):
#     print("Thread Running:",a,b)
# for i in range(5):
#     t=Thread(target=disp, args=(10,35))
#     print("Thread Name is",t)
#     t.start()    

# def disp(a,b):
#     print("Thread Running :",a,b)
# for i in range(4):
#     t=Thread(target=disp, args=(40,4))
#     print("Thread Name is:",t)
#     t.start()        

# def func(a,b):
#     print("Thread Running",a,b)
# for i in range(6):
#     t=Thread(target=func, args=(20,50))
#     print("Thread Name is:",t)
#     t.start()

# def disp():
#     print("Thread Running:")
# t=Thread(target=disp) 
# print("Thread Name:",t)
# t.start()   

# def disc(a):
#     print("The Thread is Running:",a)
# t=Thread(target=disc, args=(10,))
# print("Thread Name is:",t)
# t.start()   

# def dis(a,b):
#     print("Thread is running:",a,b)
# for i in range(5):
#     t=Thread(target=dis,args=(10,19))
#     print("Thread Name is:",t)
#     t.start()     

# def dis():
#     print("Child Thread:")
# t=Thread(target=dis)
# print("Thread Name is:",t)
# t.start()
# for i in range(5):
#     print("Main Thread")    

# def disp():
#     print("Child Thread Object:",current_thread)
# t1=Thread(target=disp)
# t1.start()
# print("Main Thread:",current_thread().getName)
# t2=Thread(target=disp)
# t2.start()    

# def disp():
#     print("Child Thread:",current_thread().getName())
# t1=Thread(target=disp)
# t1.start()
# print("Main Thread:",current_thread().getName())
# t2=Thread(target=disp)
# t2.start()    

# def disp():
#     print("default Child Name:",current_thread().name)
#     current_thread().name="ravikanth"
#     print("New Child Name:",current_thread().name)
# t=Thread(target=disp)
# t.start()
# print("default Main Name:", current_thread().name)
# current_thread().name="RaviKanth Shows"
# print("New Main Name:",current_thread().name)

# def disp():
#     print("Default Child Name:",current_thread().name)
#     current_thread().name="Harisingh"
#     print("New Child Name:",current_thread().name)
# t=Thread(target=disp)
# t.start()
# print("Default Main Name is:",current_thread().name)
# current_thread().name="Ravikanth"
# print("Default Main Thread:",current_thread().name)    

# def disp():
#     print("default Thread Name is:",current_thread().name)
# t=Thread(target=disp)
# t.start()
# print("Main Thread is:",current_thread().getName)
# t2=Thread(target=disp)
# t2.start()    

# def disp():
#     print("Default Child Name:",current_thread().name)
# t1=Thread(target=disp)
# t1.start()
# print("Main Thread:",current_thread().getName)
# t2=Thread(target=disp)
# t2.start()    

# def disp():
#     print("Default Child Name:",current_thread().name)
# t=Thread(target=disp)
# t.start()
# print("Main Thread Name is:",current_thread().getName)
# t1=Thread(target=disp)
# t1.start()
# print("Child Thread Name is:",current_thread().getName)    

# def disp():
#     pass
# t=Thread(target=disp)
# print("Default :",t.name)
# t.name="Flying Thread"
# print("NEw:",t.name)
# t.start()

# class myThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Child Thread")
# t=myThread()
# t.start()
# t.join()            
# for i in range(5):
#     print("Main Threa")

# import threading
# import time
# def cal_sqr(num):
#     print("Calculate the Square root of a number:")
#     for n in num:
#         time.sleep(0.3)
#         print("Square of a number:",n*n)
# def cal_cube(num):
#     print("Calculate the Cube of a Number:")
#     for n in num:
#         time.sleep(0.3)
#         print("Cube of a given number:",n*n*n)
# t1=time.time()
# # num=int(input("Enter Number:"))
# arr=[3,4,5,6,7]
# cal_sqr(arr)
# cal_cube(arr)
# print("Total time Taken by Thread is:",time.time()-t1)  

# import threading
# import time
# def call_sqr(num):
#     print("Square of Number:")
#     for n in num:
#         time.sleep(0.3)
#         print("Square of number is:",n*n)
    
# def call_cube(num):
#     print("Cube of Given Number:")
#     for n in num:
#         time.sleep(0.3)
#         print("Cube of Given Number:",n*n*n)
# arr=[3,4,5,6,7,8]            
# call_sqr(arr)
# call_cube(arr)
# t1=time.time()
# print("Total time taken to print thread:",time.time()-t1)

# import threading
# import time
# def call_sqr(num):
#     print("*"*30)
#     for n in num:
#        time.sleep(0.3)
#        print("Square is:",n*n)

# def call_cube(num):
#     print("-:"*30)
#     for n in num:
#         time.sleep(0.3)
#         print("Cube is:",n*n*n)
# t1= time.time()
# arr=[1,2,3,4,5,6]
# call_sqr(arr)
# call_cube(arr)
# print("Time taken by Thread is:",time.time()-t1)               

# import threading
# import time
# def call_sqr(num):
#     print("-"*20)
#     for n in num:
#       time.sleep(0.3)
#       print("Square is:",)
# def call_cube(num):
#     print("-"*20)
#     for n in num:
#         time.sleep(0.3)
#         print("Cube is:",n*n*n)
# arr=[1,2,3,4,5]
# t1=time.time()
# call_sqr(arr)
# call_cube(arr)
# print("Total Time by Thread is:",time.time()-t1)              


# import time
# from threading import Thread
# from threading import *
# def call_sqr(num):
#     print("-"*20)
#     for n in num:
#         time.time()
#         print("Square is:",n*n)
# def call_cube(num):
#     print("-"*20)
#     for n in num:
#         time.time()
#         print("Cube is:",n*n*n)
# t1=time.time()
# arr=[3,4,5,6,7]
# th1=Thread(target=call_sqr, args=(arr,))
# th2=Thread(target=call_cube, args=(arr,))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print("Total Time by Thread is:", time.time()-t1)
# print("Again executing the Main Thread")
# print("Thread 1 and Thread 2 have finished thier execution")

# import time
# from threading import *
# from threading import Thread
# def call_sqr(num):
#     print("Square of the Number are:")
#     for i in num:
#         time.time()
#         print("Square of Number is:",i*i)

# def call_cube(num):
#     print("Cube of the Number are:")
#     for i in num:
#         time.time()
#         print("Cube of the Number:",i*i*i)
# t=time.time()
# arr=[2,3,4,5,6,7,8]                
# call_sqr(arr)
# call_cube(arr)
# t1=Thread(target=call_sqr, args=(arr,))
# t2=Thread(target=call_cube, args=(arr,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Total Time by Thread:", time.time()-t)

# from threading import Thread
# from threading import *
# import time
# def call_sqr(num):
#     print("Square of the Number is:")
#     for n in num:
#         time.time()
#         print("Square is:",n*n)
# def call_cube(num):
#     print("Cube of Numbers:")
#     for n in num:
#         time.time()
#         print("Cube of Number is:",n*n*n)
# t=time.time()
# arr=[9,8,7]
# th1=Thread(target=call_sqr, args=(arr,))
# th2=Thread(target=call_cube, args=(arr,))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print("Time taken by Thread is:",time.time()-t)                

import threading
import os
def task1():
    print("Task 1 assigned to thread{}".format(threading.current_thread))
    print("ID of process running Task 1 :{}".format(os.getpid()))
def task2():
    print("Task 2 assigned to thread 2{}".format(threading.current_thread()))
    print("Id of processes running task 2{}".format(os.getpid())) 
if __name__=="__main__":
    print("ID process main program {}".format(os.getpid()))
    #Name of the Thread
    print("Main thread name is{}".format(threading.current_thread().name))
    #Creating Threads
t1=Thread(target=task1, name="t1")
t2=Thread(target=task2, name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
