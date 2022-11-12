class basic:
    pass
 
b=basic()
print(b)

b.name='Praveen'
print(b.name)
b.position=('Instructor')
print(b.position)


b1=basic()
b1.name='Ravi'
print(b.name)
b1.position='Student'
print(b1.position)


basic.no_cls=54
print(basic.no_cls)
print(b.no_cls)
print(b1.no_cls)


b.no_cls=39
print(b.no_cls)

b1.no_cls=24
print(b1.no_cls)
