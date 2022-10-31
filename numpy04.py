import numpy as np
a=np.array([(1,2,3),(4,5,6)])
for i in a:
    print(a)


    a=np.zeros((2,3))
    print(a)

    a=np.ones(3)
    a=np.ones((2,3)) 
    print(a)   

    a1=np.empty([2,3])
    print(a1)
    print(a1.shape)
    print(a1.size)

    a2=np.linspace(1,5,12)
    print(a2)


    for i in a2:
        print(a2)

        p=np.reshape(3,3)
        print(p)    
        res=p.ravel()
        print(res)