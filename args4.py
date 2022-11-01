def display(name, *args, **kwargs):
    print(name)
    for i in args:
        print(i)
        for k, v in kwargs.items():
            print(f'{k} is a {v}')

name='Start'
item=['Hello','let\'s','begin']
d={'ravi':'kanth','kasu':'bai'}  
display(name, *item, **d)          