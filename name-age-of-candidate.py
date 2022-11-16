name=input("Enter name")
age=int(input("Hi%s, Enter Your Age:"%name))

if (age<24):
    print("Congratulations ! %s"%name+'..')
    print("You are eligible for Military Services")
if (age>24):
    print("Sorry %s "%name,"..")
    print("You are not eligible for Military services")