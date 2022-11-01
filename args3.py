def display(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
        for k,v in kwargs.items():
            print(f'{k} is a {v}')


name='Namaste'
item=['Hi','I','Am','Printing'] 
d={'Ravi':'Kanth','Hari':'Singh'}           
display(name, *item, **d)


# def display(name, *args,**kwargs):
#     print(name)
#     for i in args:
#         print(i)
#         for  key,value in kwargs.items():
#             print(f'{key} is a {value}:')

# name='Gun'
# item=['phone','is','over','heating']
# d={'ravi':'kanth','hari':'singh'}
# display(name, *item, **d)