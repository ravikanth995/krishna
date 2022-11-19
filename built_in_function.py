#abs
# it is a built in function that returns the absolute value of a given number. Absolute value or modulus of a number

#Len
#it returns the length of an object, where argument may be either a sequence or a collection.
# list=[1,2,3,4,5,6,8]
# print(len(list))

# tuple=(1,2,3,4,5,6,6)
# print(len(tuple))


#Len for dictionary
# dict={1:2,3:4,5:6}
# print(len(dict))

#format
#returns the formatted represenation of a specified value
# l=format(8,)
# print(l)
# print(l)
# l=format(6,'.3f')
# print(l)

# l=format(3,'.5f')
# print(l)

#List
# list=[1,2,3,4,5]
# print(list)

# l=list("hello")
# print(l)

# l=list("Helo Ravikanth")
# print(l)


#isAplha
# l="ravikanth"
# l.isalpha()

# #is append
# list=list()
# print(list)

# list.append(1)
# print(list)

# list.append(2)
# print(list)

# list.append(3)
# print(list)

# list.append(4)
# print(list)

# list.append(5)
# print(list)

#append

# list=list()
# # print(list)

# list.append(1)
# print(list)

# list.append(2)
# print(list)



#Round
# l=round(6.98) #returns the floating value into given digits but when digits is not given, then ot will be considered zero by default
# print(l)


# l=round(9.0089)
# print(l)


# l=round(9.6267)
# print(l)

# #Reversed inbuilt function
# str='Python'
# print(list(reversed(str)))



# str='Ravikanth'
# print(list(reversed(str)))


# str="Ravikanth_chavan"
# print(list(reversed(str)))


# str='Ravi'
# print(list(reversed(str)))


#Map Inbuilt Functions
#map(function, iterable)


# def add(num):
#     return num+num
# res=map(add,[3,2,1])
# print(list(res))




# def add(num):
#     return num+num
# res=map(add,[5,4,3,2,1])
# print(list(res))    


# def add(num):
#     return num+num
# res=map(add,(3,2,1))
# print(tuple(res)) 
# 
# 
# 
# def add(num):
#     return num+num
# res=map(add,[4,3,2,1])
# print(list(res))       


#Split This method is used to split a string into list of elements

# #string.split("separator")
# str='Python is programming language'
# list=str.split("is")
# print(list)


# string="python is not a readable code"
# list=string.split("not")
# print(list)

# str='Ravikanth is selected for this job'
# list=str.split("is")
# print(list)

# str="Ravikanth is hired for this job"
# list=str.split("is")
# print(list)

# str="lucky is not lucky"
# list=str.split("not")
# print(list)

# #Split
# str="lucky is not enough lucky"
# list=str.split("not")
# print(list)


#join Inbuilt Function 
#This method is used to take all items from an iterable and join them into single string
#string.join(iterable)

# list=['Python','Programming','Language']
# separator="\t"
# string=separator.join(list)
# print(string)