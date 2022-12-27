#Anonymous Function or Lambda Function
#Syntax
#lambda argument_list:expression
# sum=lambda x,y:x+y
# sum(2,3)
# print(sum)

# sum=lambda x:x+10
# print(sum(56))

# sum=lambda x:x+2
# print(sum(3))

# #1. Accept employee data from the user using the input function and displaying it using the print function
# name=input("Enter Name:")
# salary=float(input("Enter Salary:"))
# company=input("Enter Company name:")
# print("** Employee Details**")
# print("name","Salary","Company")
# print(name,salary,company)

#2. Following code takes two Input from console and typecasts them to integer then prinnts the sum
# num1=input("Enter A Value:")
# num2=input("Enter B Value:")
# #Type Casting 
# num1=int(num1)
# num2=int(num2)
# print(num1+num2)

# num1=input("Enter a Value:")
# num2=input("Enter b Value:")
# num1=int(num1)
# num2=int(num2)
# print(num1+num2)

#Built-in Python
#eval(expression, globals=None, locals=None)

#Expression = A String or Expression that will be evaluated as Python Code'
#Globals= (Optionals). A Dictionary containing Global Parameters 
#Locals= (Optionals) A Dictionary containing local Parameters

# a=eval("12")
# print(a)
# b=eval("9")
# print(b)

# a=eval("12+12")
# print(a)

# b=eval("900+122")
# print(b)

# exp=eval("2**9")
# print(exp)
# exp=eval("2**3")
# print(exp)
exp=eval("3**9")
print(exp)