d={ 1:7, 4:6, 2:4, 7:1}
d.items()
# #dict_values([1:3,5:6])
# for key, values in d.items():
#     print(key,values)




#for key, values in d.items():
    #print(key, "", values)
    # print(key,values)

a={key:values for key, values in d.items()}
a
#{1:2,3:4,5:6}
#{for key/2:values/2 for key, values in d.items}