# def orders(*item):
#     print(item)
#     print(*item)
# print('Phine','stake','pk')    
# def orders(arg, *item):
#     print(arg)
#     print(*item)
# print('phone','cool','margin')    

# def display(name, *args):
#     print(name)
#     for i in args:
#         print(i)

# name='Gun'
# item=['ek','do','teen']
# display(name, *item)        

# def osho(**kwargs):
#     for key, value in kwargs.items():
#         print('%s==%s'%(key,value))

# osho(first='hello',mid='namaste', last='bye')    


# def myfun(*args, **kwargs):
#     :
# print('*args:',args)
# print('kwargs',kwargs)

# myfun('HEllo','python','world', first='hello', mid='python', last='world')
    

def display(name, *args, **kwargs):
    print(name)
    for i in args:
        print(i)
        for k, v in kwargs.items():
            print(f'{k} in a {v}')

name='Roopa'
item=['1','2','3']
d={'ravi':'kanth','hari':'singh'} 
display(name, *item, **d)               
    


