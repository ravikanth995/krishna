#random choice(sequence)
import numpy as np
import random
# s='ravi'
# t=(1,2,3)
# d={1,2,3,}
l=[1,2,3,4,5,6]
# # print(random.choice(t))
# it prints any element of the data type that is prescribed in the print(random.choice(here))


#shuffle method to shhuffle the sequence
# random.shuffle(l)
# print(l)

# l1=[1,2,3]
# print(random.choice(l1))

a=np.random.random(2)
a=np.random.rand(3,2)
a=np.random.randint(2, size=4)
print(a)



arr=np.arange(9)
np.random.shuffle(arr)
print(arr)

