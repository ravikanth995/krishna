# dct={}
# dct=dict()
# print(dct)

# dct[1]='aaa'
# dct[2]='bbb'
# dct[3]='ccc'
# dct[4]='ddd'
# print(dct)

# dct={}
# dct[0]='ravi'
# dct[1]='kanth'
# dct[2]='rakshit'
# print(dct)

# dct['a']='aa'
# dct['b']='bb'
# dct['c']='ccc'
# print(dct)

#Accessing elements from Dictionary
# dct={'a':9023, 'b':9024, 'c':9025, 'd':9026, 'd':9027, 'e':9028}
# print(dct)
# print(dct['a'])
# print(dct['b'])
# print(dct['c'])
# print(dct['d'])

# dct={1:2,2:3,4:5,6:7}
# print(dct)

# print(dct[1])
# print(dct[2])
# print(dct[4])

# num={'a':80, 'b':90, 'c':70}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])

# num={'a':90, 'b':70, 'c':99}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])

# num={'a':2, 'b':3, 'c':5, 'd':9, 'e':34, 'f':66, 'g':74}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])
# print(list(num)[3])
# print(list(num)[4])
# print(list(num)[5])
# print(list(num)[6])

# num={'a':2, 'b':6, 'c':9, 'd':8, 'e':5, 'e':4, 'f':1, 'g':2, 'h':3}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])
# print(list(num)[3])
# print(list(num)[4])
# print(list(num)[5])
# print(list(num)[6])
# print(list(num)[7])

# num={1:2, 3:4, 5:6, 7:8, 9:0}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])
# print(list(num)[3])
# print(list(num)[4])

# l={1:2,3:4,5:6,7:8,9:0,2:1,4:3,6:5,7:6,9:8}
# print(list(l)[0])
# print(list(l)[1])
# print(list(l)[2])
# print(list(l)[3])
# print(list(l)[4])
# print(list(l)[5])
# print(list(l)[6])
# print(list(l)[7])

# d={'roll_no':'101', 'name':'krishna', 'marks':'456'}
# print(d['roll_no'])

# d={'roll_no':'101', 'name':'krishna','marks':4656}
# if 'total' in d:
#     print(d[total])
# else:
#     print("Given key is not available")    

# dct={'name':'Buddha','age':29}
# print(dct['name'])
# print(dct.get('age'))
# print(dct.get('address'))

# dct={'name':'Buddha', 'age':29}
# print(dct['name'])
# print(dct.get('age'))
# print(dct.get('address'))

# dct={'name':'Buddha', 'age':29}
# print(dct['name'])
# print(dct.get('age'))
# print(dct.get('address'))

#Iterating over a dictionary
# d={'a':100, 'b':200, 'c':300, 'd':400}
# for key in d:
#     print(key)

# d={'a':211, 'b':700, 'c':499, 'd':210}
# for key in d:
#     print(key)

# d={'a':21, 'b':200, 'c':100, 'd':291, 'l':302}
# for key in d:
#     print(key)

# d={1:2,3:4,5:6,7:8}
# for key in d:
#     print(key)

# d={1:2,'shashi':12, 12:'ravi'}
# for key in d:
#     print(key)

# d={'ravi':1995, 'shashi':1991, 'shalini':1993, 'kasubai':1975}
# for key in d:
#     print(key)

#We can also use the method keys() to get the same results
# d={'ravi':1995, 'kanth':1991, 'Shashi':1991, 'Shalini':1993}
# for key in d.keys():
#     print(key)

# d={'ravi':1995, 'kanth':556, 'kant':214, 'bandit':982}
# for key in d.keys():
#     print(key)

# d={'oho':'aaho','pichi':'kichti','rooba':'orange','tooba':'mehbooba'}
# for key in d.keys():
#     print(key)

# d={'camera':'man','Photo':'anand','sada':'ammai'}
# for key in d.keys():
#     print(key)

# d={'tata':'tisco','amabuja':'cement'}
# for key in d.keys():
#     print(key)

# d={'ashneer':'grover', 'ash':'warya'}
# for key in d.keys():
#     print(key)

# d={'a':100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600}
# for values in d.values():
#     print(values)

# d={'a':100, 'b':699, 'c':321, 'd':463}
# for values in d.values():
#     print(values)

#The above loop is logically equivalent to the following one:
# d={'a':100, 'b':200, 'c':300, 'd':400}
# for key in d:
#     print(d[key])

#Updating elements in a Dictionary
 #d[key]=valule

# dct={'name':'Buddha', 'Age':29}
# print("Before Upgradtion Dictionary values:", dct)
# print("reference id value is:", id(dct))
# dct['Age']=38
# dct['address']='Lumbini, nepal'
# print("After updation")
# print(dct)
# print("refernce id after updation:",id(dct))

# dct={'name':'Buddha', 'age':20,}
# print("before updation of dictionary")
# print("reference id :",id(dct))
# print("after updation")
# dct['name']='Gautam_Buddha'
# dct['age']=29
# dct['address']='Lumbini, Nepal'
# print(dct)
# print("after updation:",id(dct))

# dct={'name':'buddha','age':28}
# print("Before Updation")
# print("reference id is:", id(dct))
# print("After Updation is:",id(dct))
# dct['name']="Gautam_Buddha"
# dct['age']=29
# dct['address']='Bodh_Gaya'
# print(dct)

#Deleting items in a dictionary 
#pop()---> This method removes as item in a dictionary in many ways
#popitem()---> This method removes and return an arbitrary item(key, value) from the dictionary
#clear()---> This method removes all the items at once
#del keyword ---> This keyword to remove individual items or the entire dictionary itself

#Example

# d={1:100, 2:200, 3:300, 4:400, 5:500, 6:600}
# d.pop(4)
# print(d)

# d.pop(3)
# print(d)

# d.popitem()
# print(d)

# d={1:100, 2:200, 3:300, 4:400, 5:500, 6:600, 7:700, 8:800, 9:900}
# print(d)
# d.pop(2)
# print(d)

# d.popitem()
# print(d)

# del d[1]
# print(d)

# d.popitem()
# print(d)

# d={0:000, 1:100, 2:200, 3:300, 4:400, 5:500, 6:600, 7:700, 8:800, 9:900}
# print(d)

# d.pop(0)
# print(d)

# d.popitem()
# print(d)

# del d[1]
# print(d)

# d.clear()
# print(d)

# del d
# print(d)

#Sorting The Dictionary
# Dict={'somu':18, 'ramu':19, 'sita':22, 'Bheemu':21}
# boys={'somu':18, 'ramu':19, 'bheemu':21}
# gir={'sita':22}
# students=list(Dict.keys())
# students.sort()
# for S in students:
#     print(":".join((S,str(Dict[S]))))

# dict={'somu':21, 'seema':23, 'Reema':81, 'bhumu':23}
# boys={'somu':21, 'bhimu':23}
# girls={'seema':23, 'Reema':81}
# students=list(dict.keys())
# for s in students:
#     print(":".join((s, str(dict[s]))))

# dict={'ravi':27, 'shashi':31, 'shalini':30, 'kasu':52}
# boys={'ravi':27, 'shashi':31}
# girls={'shalini':30, 'kasu':52}
# students=list(dict.keys())
# for s in students:
#     print(":".join((s, str(dict[s]))))

# dict={'ravi':21, 'shashi':31, 'kanth':24, 'kasu':22}
# boys={'ravi':21, 'shashi':31, 'kanth':24}
# women={'kasu':22}
# students=list(dict.keys())
# for s in students:
#     print(":".join((s, str(dict[s]))))

# dict={'ravi':27, 'Shashi':31, 'kasubai':52, 'Shalini':30, 'Khushi':7, 'Charan':1}
# boys={'ravi':27, 'Shashi':31, 'Charan':1}
# girls={'kasubai':52, 'Shalini':30, 'Khushi':7}
# students=list(dict.keys())
# for s in students:
#     print()

# dict={'ravi':1, 'kanth':2, 'break':3, 'Samkhya':4, 'darshan':5, 'upanishad':6, 'Girls':0}
# boys={'ravi':1, 'kanth':2, 'break':3, 'samkhya':4, 'darshan':5}
# girl={'Girls':0}
# students=list(dict.keys())
# for s in students:
#     print(":".join((s, str(dict[s]))))

# dict={'preet':1, 'rita':2, 'geeta':3, 'masculine':4, 'feminine':6, 'manliness':8}
# boys={'masculine':4, 'manliness':8}
# girl={'preet':1, 'rita':2, 'geeta':3, 'feminine':6}
# students= list(dict.keys())
# students.sort()
# for s in students:
#     print(":".join((s, str(dict[s]))))

# dict={'male':2, 'bheemla':1,'karobari':4,'naykan':3, 'Tandri':4,'maati':3}
# man={'male':2, 'bheemla':1, 'karobari':4, 'maati':3}
# female={'naykan':3, 'taandri':4}
# students=list(dict.keys())
# students.sort()
# for s in students:
#     print(":".join((s, str(dict[s]))))

dct={'shikha':1, 'Kelia':2, 'Karab':8, 'Karan':5}
boys={'Karab':8, 'Karan':5}
girls={'shikha':1, 'Kelia':2}
students=list(dct.keys())
students.sort()
for s in students:
    print(":".join((s, str(dict[s]))))