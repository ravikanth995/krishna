import pandas as pd
# data={'apple': [1,2,3,4], 'orange':[5,6,7,8]}
# var=pd.DataFrame(data)
# print(var)

# data1={'apple':[3,2,1,8], 'oranges':[1,2,3,5]}
# var1=pd.DataFrame(data1)
# var1=pd.DataFrame(data1, index=['june','robert','jack','nostoc'])
# print(var1)


age=[['ritk', 77,'Male'], ['Robert', 88, 'Male'],['gita', 55, 'Female'],['meera',44, 'Female']]
pd.DataFrame(age, columns=['Name','Marks','Sex'])
print(pd)
[pd.to_csv(index=name)]

