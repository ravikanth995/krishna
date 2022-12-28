#String : Slicing, Membership, Pattern Matching
#String Slicing
# Str="TBalaji"
# s1=slice(3)
# s2=slice(1,5,2)
# s3=slice(-1,-5,-2)
# print(Str[s1])
# print(Str[s2])
# print(Str[s3])

# str="Ravikanth"
# s1=slice(3)
# s2=slice(1,4,1)
# s3=slice(-1,-6,-2)

# print(str[s1])
# print(str[s2])
# print(str[s3])

# str="Python"
# s1=slice(3)
# s2=slice(4,1)
# s3=slice(-1,-5,-2)

# print(str[s1])
# print(str[s2])
# print(str[s3])

#Indexing Sequence
# str="Python"
# print(str[:3])
# print(str[1:4:1])
# print(str[-1:-5:1])

# str="Python"
# print(str[: :-1])

#Pattern Matching
#import re
# import re
#re.compiler
#syntax
#sPattern=re.compile(pattern)
#result=sPattern.match(string)
# import re
# txt="hello World"
# #check if the string starts with hello
# x=re.findall("^hello",txt)
# if x:
#     print("yes, the string starts with 'hello'")
# else:
#     print("No Match")    

# import re
# txt="hello challo world"
# x=re.findall("^hello",txt)
# if x:
#     print("It starts with 'hello'")
# else:
#     print("No match")    

# import re
# txt="my World Crazy"
# x=re.findall("^my",txt)
# if x:
#     print("Pattern matching with 'my'")
# else:
#     print("No Match")    

# import re
# txt="meri duniya tu hi re"
# x=re.findall("meri",txt)
# if x:
#     print("Yes, String Starts with meri")
# else:
#     print("No Match")    

# import re
# txt="Python Language"
# x=re.findall("^Python",txt)
# if x:
#     print("Yes, String is Matching with the Python")
# else:
#     print("No Match")    

# import re
# txt="My World is you Khushi"
# x=re.findall("^My",txt)
# if x:
#     print("Yes, String starts with My")
# else:
#     print("No Match")    

# import re
# txt="Python is a coding language"
# x=re.findall("^Python",txt)
# if x:
#     print("Yes, string starts with Python")
# else:
#     print("No Match")    

# import re
# txt="Python is here"
# x=re.findall("Python",txt)
# if x:
#     print("Yes, it starts with 'Python'")
# else:
#     print("No Match")    

# import re
# txt="Python, is here"
# x=re.findall("^Python",txt)
# if x:
#     print("Yes, it starts with 'Python'")
# else:
#     print("No match")

# import re
# txt="Python begins here"
# x=re.findall("here$",txt)
# if x:
#     print("It Ends with 'here'")
# else:
#     print("No Match")    

# import re
# txt="Python is programming language"
# x=re.findall("language$",txt)
# if x:
#     print("Yes, it ends with 'language'")
# else:
#     print("No Match")    

# import re
# txt="Python is a programing langauge"
# x=re.findall("langauge$",txt)
# if x:
#     print("yes, it ends with 'language'")
# else:
#     print("no match")    

# import re
# txt="hello world"
# x=re.findall("[a-h]",txt)
# print(x)

# import re
# x1="Hello\nWorld"
# print(x1)
# x2=r"hello\nWorld"
# print(x2)

# string="\n and \r are escape sequence"
# result=re.findall(r'[\n\r]',string)
# print(result)

#Python regular expression function
#match(): it resturns the first occurance
# import re
# pattern="^a...s$"
# strint_test='abass'
# re.match(pattern, strint_test)
# print(re.match(pattern, strint_test))
# print(re.match("Bolly","Bollywood"))
# print(re.match("wood","bollywood"))

# import re
# pattern="^a...s$"
# str_test="abass"
# re.match(pattern,str_test)
# print(re.match(pattern,str_test))
# print(re.match("bolly","bollywood"))
# print(re.match("pilo","pilo chai"))

# import re
# pattern="^a...s$"
# str_test="abass"
# re.match(pattern, str_test)
# print(re.match(pattern,str_test))
# print(re.match("bolly","bollywood"))
# print(re.match("wood","bollwood"))

# import re
# pattern="^a...s$"
# str_test="abass"
# re.match(pattern, str_test)
# print(re.match(pattern, str_test))
# print(re.match("bolly","bollywood"))
# print(re.match("wood","bollywood"))

# import re
# pattern="^a...s$"
# str_test="abass"
# re.match(pattern, str_test)
# print(re.match(pattern, str_test))
# print(re.match("bitcoin","bitcoinwood"))
# print(re.match("wood","boitcoinwood"))

#search() it returns only first occurance
#matchObject=re.serach(pattern,input_str,flags=0)
# import re
# str="he sells M3R5 in this shop"
# pattern="sells"
# if re.search(pattern, str):
#     print("match found")
# else:
#     print(pattern,"is not present in the string")    

# import re
# str=" man sells his home for auction"
# pattern="home"
# if re.search(pattern,str):
#     print("Match Found")
# else:
#     print(pattern,"is not present in the string")    

# import re
# str="Ashtavkra geeta is my heart"
# pattern="geeta"
# if re.search(pattern,str):
#     print("Match Found")
# else:
#     print(pattern,"is not present in the string")    

# import re
# str="My name is Ravikanth"
# pattern="name"
# if re.search(pattern,str):
#     print("matchh found")
# else:
#     print(pattern, "not present in the string")    

# import re
# pattern="name"
# str="my name is ravikanth"
# if re.search(pattern,str):
#     print("Match found")
# else:
#     print(pattern, "is not found")    

#findall() : used to search for 'all' occurance that  a given pattern.
# import re
# txt="This is Bollywood"
# x=re.findall("is",txt)
# print(x)

#split(): used to split string where there is match amd returns a list of string where the splits have occured.
# import re
# txt="this is nonsense"
# pattern=" "
# x=re.split(pattern, txt)
# print(x)

# import re
# txt="this is bollywood"
# x=re.split("\s",txt)
# print(x)

import re
# txt="this is tiger"
# x=re.split("\s",txt)
# print(x)

# txt="ajyaan hai andhakar"
# x=re.split("\s",txt)
# print(x)

# txt="this is idiot"
# x=re.split("\s",txt,1)
# print(x)

#sub(): used to substitue the part of a string with another. takes 3 arggs=pattern, substring,string
# txt="this is bollywood"
# x=re.sub("\s","5",txt)
# print(x)

# txt="this is tigress"
# x=re.sub("\s"," ",txt)
# print(x)

# txt="this is best"
# x=re.sub("\s",":",txt)
# print(x)

# str="abc 12\
#      de 23 \n f45 6"
# pattern="\s+"
# replace=" "
# new_str=re.subn(pattern, replace, str)
# print(new_str)

#Numeric Functions
#eval
# import math
# x=eval("12*22")
# print(x)

#max()
#max(n1,n2,n3....) or max(iterable)
# x=max(5,10)
# print(x)
# x=max("apple","boy","cat")
# print(x)

# x=min(5,10)
# print(x)
# x=min("apple","cat","doge")
# print(x)

#round 
#round(number, digits)
# print(round(2.009,2))
# print(round(3.001346,3))
# print(round(9.00976252,2))

# print(round(2.8871,3))
# print(round(9.7772,1))

# print(round(2.990,1))
# print(round(3.110,1))

#pow() returns the value of x raised to the power of y. both the powe and(**) perfonme exponentation. ** is an operator and pow() is a built-in function
# #pow(x,y)
# print(pow(12,3))
# print(pow(3,4))
# print(pow(3,2))

#ceil(): returns ceiling value of x i,e. the smallest whole number greater than or equal to x
import math
# #math.ceil(x)
# print(math.ceil(-23))
# print(math.ceil(300.16))
# print(math.ceil(300.71))
# print(math.ceil(1.09))
# print(math.ceil(-1.18))

#floor(): returns floor value of x i.e, the largest integer not greater than x.
# print(math.floor(-23.19))
# print(math.floor(25.008))
# print(math.floor(33.990))

# print(math.floor(2.0900))
# print(math.floor(22.12))

# #sqrt()
# print(math.sqrt(225))
# print(math.sqrt(625))

#fabs(): returns the absolute value of x
# print(math.fabs(-23.11))

#factorial(): 
# print(math.factorial(4))
# print(math.factorial(6))

# print(math.gcd(6,19))
# print(math.gcd(4,24))

#fmod and remainder(x,y) returns as tupe
# print(math.fmod(25,5))
# print(math.fmod(20,6))
# print(math.fmod(33,2))

# print(math.exp(5))
# print(math.exp(4))
# print(math.exp(2))
# print(math.exp(3))

# import random
# print(random.random())
# print(random.random())
# print(random.random())

import random
# print(random.random())
# print(random.random())
# print(random.random())

# #randrange():
# print(random.randrange(0,12,2))
# print(random.randrange(0,5))
# print(random.randrange(1,12,2))
# print(random.randrange(1,10,3))
# print(random.randrange(0,12,1))

#Date Time Functions
from datetime import date
from datetime import time
from datetime import datetime
today=date.today()
print("today\'s date",today.day)
print("today\'s time",today.month)
print("today\'s year",today.year)
print("todays\'s weekday",today.weekday())
