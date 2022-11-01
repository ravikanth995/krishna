#arbitoroy arguments
# def display(*details):
#     for i in details:
#         print(i)

# display('ravi','kanth','chavan','omla')        



# def display(*folks):
#     for i in folks:
#         print(i)

# name=['ravi','kanth','chavan','omla','narayan']        
# names=['ravi','hari','narayan','chavan']
# display(name,*names)



# def orders(name,*names):
#     print('items purchased by customer is:', name)
#     for i in item:
#         print('\t\t',i)
        
# name='pale'
# item=['phone','cooling','heat','panchabhoot']

# orders(name,*item)


def display(name, *args,**kwargs):
    print(name)
    for i in args:
        print(i)
        for  key,value in kwargs.items():
            print(f'{key} is a {value}:')

name='Gun'
item=['phone','is','over','heating']
d={'ravi':'kanth','hari':'singh'}
display(name, *item, **d)
