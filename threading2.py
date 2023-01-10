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