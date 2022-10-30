import random
f=random.random() #it gives any random number from 0 to 1
print(f)


#rondom choice(sequence)
s='String'
t=(1,2,3)
d={1:2,3:4,5:6}
l=[1,2,3,4,5]
print(random.choice(s))

#shuffle method to shuffle the sequence (list)
print(l)
random.shuffle(l)

l11=[1,2,3]
print(l11)
print(random.choice(l11))