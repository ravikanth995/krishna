def func(*a):
    for arg in a:
        print(arg)
        return a
var=func("hello","ravi","kanth")
print(var)