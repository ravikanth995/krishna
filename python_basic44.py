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

# dct={'shikha':1, 'Kelia':2, 'Karab':8, 'Karan':5}
# boys={'Karab':8, 'Karan':5}
# girls={'shikha':1, 'Kelia':2}
# students=list(dct.keys())
# students.sort()
# for s in students:
#     print(":".join((s, str(dict[s]))))

#Dictionary Function
#Built-in methods
#1) setdefault()
#d.setdefault(key,value)

# d={1:'rama', 2:'krishna', 3:'murthy'}
# print(d.setdefault(4, "Vinay"))
# print(d)
# print(d.setdefault(1,"schin"))
# print(d)

# d={1:"ravi", 2:"kanth", 3:"chavan", 4:"rockstar"}
# print(d.setdefault(4,"dict"))
# print(d)
# print(d.setdefault(5,"dict"))
# print(d)

#2. copy()
#This method duplicates(clones)dictionary. This method returns a shaloow copy of the dictionary. it doesn't modify the original dictionary
#dict.copy

# dct={1:'ravi', 2:"kanth"}
# d=dct.copy()
# print("original:", dct, id(dct))
# print("*"*12)
# print("Duplicates:", d, id(d))

# dct={1:"ravi", 2:"kanth"}
# print("Original:", dct, id(dct))
# print("*"*35)
# d=dct.copy()
# print("Duplicates:",d, id(d) )

# dct={1:"kanth", 2:"ravi"}
# print("Original:", dct, id(dct))
# print("-"*50)
# d=dct.copy()
# print("Duplicates:", d, id(d))

#2. len() built-in function
# len(s)
# dct=[]
# print(dct)
# print("Length is:", len(dct))
# dct={1:1, 3:2}
# print(dct, "length is:", len(dct))

# dct=[]
# print(dct)
# print("Length is:",len(dct))
# print("-"*50)
# dct={1:2, 3:2, 4:6}
# print(dct, "length is:", len(dct))

# dct={}
# print(dct)
# print("Length is:",len(dct))
# print("-"*30)
# dct={1:2, 3:5, 6:2}
# print(dct, "length is:", len(dct))

# dct={}
# print(dct,"Length is:", len(dct))
# print("-"*25)
# d={1:2, 3:4, 5:6, 6:7, 8:6, 4:5, 3:2}
# print(d, "length is:", len(d))

# dct={}
# print(dct, "Length is:", len(dct))
# print("-"*25)
# d={1:2, 3:4, 5:6, 7:8, 8:4}
# print(d, "length is:", len(d))

#2. update built-in method
#The update() method adds elements(s) to the dictionary if the key is not in the dictionary. if the key is in the dictionary, it updates the key with the new value
#dict.update([other])

# d={1:100,2:100}
# print(d)
# d2={2:300}
# d.update(d2)
# print(d)

# d={1:100, 2:300}
# print(d)
# d1={2:800}
# d.update(d1)
# print(d)

# d={1:123, 2:397, 4:653}
# print(d)
# d1={2:300, 4:300}
# d.update(d1)
# print(d)

# d={1:211, 2:544}
# print(d)
# d1={1:200, 2:200}
# d.update(d1)
# print(d)
# d2={2:200}
# d.update(d2)
# print(d)
# d3={2:400}
# d.update(d3)
# print(d)
# d4={4:500}
# d.update(d4)
# print(d)

# d={1:111, 2:222, 3:333, 4:444, 5:555}
# print(d)
# d1={1:100, 5:500}
# d.update(d1)
# print(d)
# d2={2:200, 4:400}
# d.update(d2)
# print(d)
# d3={3:300}
# d.update(d3)
# print(d)

# d={1:211, 3:44, 5:1, 6:2, 7:23}
# print(d)
# d1={1:100, 2:200, 3:300}
# d.update(d1)
# print(d)
# d2={7:700, 5:500}
# d.update(d2)
# print(d)
# d3={6:600}
# d.update(d3)
# print(d)

#Comparison in dictionary
#It compares values and keys of two dictionaries. if both are same, it will return 0 otherwise 1 or -1. if the first dictionary has more elements than second, it will return 1 otherwise -1.
#cmp(dict1,dict2)
# dict1={1:'100', 2:'200'}
# dict2={1:'200', 2:'300'}
# dict3={1:'100', 2:'200'}
# print("return value:%d"%dict1(dict, dict2))
# print("return value:%d"%dict2(dict2,dict3))
# print(dict1==dict2)
# print(dict2==dict3) #Comparison is not supported by python3

#4. keys() and values()
# month={"Jan":1, "Feb":2, "March":3}
# print(month.keys())
# print(month.values())

#5. Items() in dictionaries
#it returns a list of tuples(keys, values) representing key:values pairs. It is useful when you wish to iterate through the keys or values of a dictionary, even through in no particular order.
# month={"jan":1, "feb":2, "March":3}
# print(month.items())

# month={"Jan":1, "Feb":2, "March":3}
# print(month.items())

# month={"Jan":1, "Feb":2, "March":3}
# print(month.items())

# month={"Sept":9, "Oct":10, "Nov":11, "Dec":12}
# print(month.items())

#Python Dictionary comprehension
# dict={ x:x*x for x in range(1,10)}
# print('x:x*x:',dict)

# dct={x:x*x for x in range(1,11)}
# print(dct)

# dct={x:x*x for x in range(12)}
# print(dct)

# dct={x:x*x for x in range(1,15,2)}
# print(dct)

# dct={x:x*x for x in range(2,19,2)}
# print(dct)

# dct={x:x*x for x in range(1,10)}
# print(dct)

# dct={x:x*x for x in range(1,18)}
# print(dct)

#dictionaries con-catenation
#1. update() method
# dict1={'a':10, 'b':2}
# dict2={'c':1, 'd':4}
# dict2.update(dict1)
# print("Dict1",dict1)
# print("-"*24)
# print("dict2",dict2)

# dc1={'a':1, 'b':2}
# dct2={'c':3, 'd':4}
# dct2.update(dc1)
# print("Dict1:",dc1)
# print("="*32)
# print("dict2:",dct2)

# dct1={'a':1, 'b':2}
# dct2={'c':3, 'd':4}
# dct2.update(dct1)
# print("Dct1:",dct1)
# print("-"*29)
# print("Dct2:",dct2)

# dct1={'a':1, 'b':2}
# dct2={'c':3, 'd':4}
# dct2.update(dct1)
# print(dct1)
# print("-"*29)
# print(dct2)

#Using ** in Python
# dc1={'a':1, 'b':2}
# dc2={'c':3, 'd':4}
# dc3={**dc1, **dc2}
# print(dc1)
# print(dc2)
# print(dc3)

# dc1={'a':1, 'b':2}
# dc2={'c':3, 'd':4}
# dc3={**dc1, **dc2}
# print("Dc1:",dc1)
# print("Dc2:",dc2)
# print("Dc3:",dc3)

# dc1={'a':1, 'b':2}
# dc2={'c':3, 'd':4}
# dc3={**dc1, **dc2}
# print("Dict1:",dc1)
# print("dict2:",dc2)
# print("Dict3:",dc3)

# dc1={'a':1, 'b':2}
# dc2={'c':3, 'd':4}
# dc3={**dc1, **dc2}
# print("Dict1:",dc1)
# print("Dict2:",dc2)
# print("Dict3:",dc3)

# dc1={'a':1, 'b':2}
# dc2={'c':3, 'd':4}
# dc3={**dc1, **dc2}
# print("Dc1:",dc1)
# print("dc2:",dc2)
# print("Dc3:",dc3)

#For task in to merge three dictionaries into fourth dictionary
# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5, 'f':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5, 'f':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5, 'f':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5, 'f':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5, 'f':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'e':5, 'f':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={'a':1, 'b':2}
# d2={'c':3, 'd':4}
# d3={'d':5, 'e':6}
# d4={}
# for d in (d1,d2,d3): d4.update(d)
# print(d4)

# d1={1:2, 2:3, 4:5}
# d2={6:7, 8:5, 5:6}
# d3={11:2, 34:5, 67:5}
# d4={}

# for d in (d1,d2,d3): d4.update(d)
# print(d4)

#Some examples to find the Maximnum, minimum and mean value in dictionary
#1. Maximum an in-built
#1. max_key=max(a_dictionary, key=a_dictionary.get)
#2. min_key=min(a_dictionary, key=a_dictionary.get)

# income={'Ashish': 2000,
#         'Manish': 5000,
#         'Ramesh': 3000}
# print("maximum:",max(income, key=income.get))
# print("Minimum:",min(income, key=income.get))        

# Incomme={'Ravi':2000,
#         'Shashi':5000,
#         'Shalini':6000}
# print("Maximum Income is of:", max(Incomme, key=Incomme.get))
# print("Minimum income is of:",min(Incomme, key=Incomme.get))  

# income={'Ravikanth':5000,
#        'Shashikanth':6000,
#         'Kasubai':45000}
# print("Income of:",max(income, key=income.get))
# print("Income of:",min(income, key=income.get))        

# income={'Ravikanth':4000,
#         'Shashikanth':23000,
#         'Kasubai':45000,
#         'Kalavati':22000}
# print("Maximum income is of:",max(income, key=income.get))
# print("Minimum income is of:",min(income, key=income.get))

# income={'Khushi':12000,
#        'Charan':11000,
#         'Shalini':10000}
# print("Maximum Income is of:",max(income, key=income.get))
# print("Minimum Income is of:", min(income,key=income.get))        

# income={'raaj':23000,
#         'Govind':35000,
#         'Rajkumar':33000,
#         'Kasubai':54000}
# print("Maximum Salary is of:",max(income, key=income.get))
# print("Minimum Income is of:",min(income, key=income.get))        

# income={"Akshay Kumar":450000,
#        "ShahRukhKhan":400000,
#        "Amir Khan":340000}
# print("Maximum Money is of:",max(income, key=income.get)) 
# print("Minimum Money is of:",min(income, key=income.get))      

income={"Ravi":10000,
       "Shashi":23000,
       "Kalavati":24000,
       "KasuBai":55000}
print("maximum Income is of:", max(income, key=income.get))
print("Minimum Income is of:",min(income, key=income.get))       