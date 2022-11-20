#Capitalize
#first letter of the string will be converted into capital
#string_name.capitalize()

# str='ravi is kanth its ravikanth'
# l1=str.capitalize()
# print(l1)


# str='ravi'
# l1=str.capitalize()
# print(l1)

#Center()
#this method has the two arguemnts. one is width of the string and the other is the filling character
#string_name.center(width, filling_char)

# str='HELLO'
# l1=str.center(15,"#")
# print(l1)

# str='HI'
# l1=str.center(8,"#")
# print(l1)

# str="HI"
# l1=str.center(6,"*")
# print(l1)

#Count
#it returns the number of times the value is repeated in the string. It consists of three arguments, one is the string and other two are begining and end of strig which denoted starting and ending indices.
#string_name.count(string,begining,end)

# str='welcome to python programming'
# l1=str.count('w',0,len(str)) #w is printed is only one time the string, so output will be 1 and e is two times, so output will be 2
# print(l1)

str='ravi kanth'
l1=str.count('a',0,len(str))
print(l1)