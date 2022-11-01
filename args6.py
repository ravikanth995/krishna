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

def osho(**kwargs):
    for key, value in kwargs.items():
        print('%s==%s'%(key,value))

osho(first='hello',mid='namaste', last='bye')        



