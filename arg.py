def func(*hi):
    for arg in hi:
        print(arg)
        yield arg

var=func('hello','prye')
print(var)


def display(b,a):
    print(a,b)

display(3,2)    