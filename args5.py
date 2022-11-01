def display(name, *args, **kwargs):
    print(name)
    for i in args:
        print(i)
        for k, v in kwargs.items():
            print(f' {k} is a {v}')


name='class'
item=['ravi','is','a','python','student']
d={'python':'software','java':'javascript'} 
display(name, *item, **d)           
