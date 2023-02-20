import numpy as np
import pandas as pd
# data=np.array(['g','e','e','k','s'])
# ser=pd.Series(data)
# print(ser)
# ser=np.array(['r','a','v','i'])
# print(ser)
# data=pd.Series(ser)
# print(data)
# ser=np.array(['r','a','v','i','k','a','n','t','h'])
# print(ser)
# data=pd.Series(ser)
# print(data)

# lst=["ravi","kanth","chavan",
#      "kasu","bai","chavan"]
# df=pd.Series(lst)
# print(df)

# list1=["ravi","kanth","chavan","Bsc","passed","out"]
# df=pd.DataFrame(list1)
# print(df)

# list1=["ravi","kanth","chavan"]
# df=pd.Series(list1)
# print(df)
# print(type(df))

# list1=["ravi","kanth","chavan"]
# df=pd.DataFrame(list1)
# print(df)
# print(type(df))

# data={
#     "Apple":[1,2,3,4,5],
#     "Oranges":[6,7,8,9,10]
# }
# ser=pd.Series(data=data)
# df=pd.DataFrame(data)
# print(ser)
# print(df)

# data={
#     "Oranges":[1,2,3,4,5,6],
#     "Apples" :[0,1,2,3,4,5]
      
# }
# ser=pd.Series(data=data)
# df=pd.DataFrame(data)
# print(ser)
# print(df)

# mylist=list(["abcdefghij"])
# my_arr=np.arange(10)
# my_dict=dict(zip(mylist,my_arr))
# ser=pd.Series(mylist)
# ser1=pd.Series(my_arr)
# ser3=pd.Series(my_dict)
# print(ser3.head())

# data={
#     "Apples":[3,7,8,3],
#     "Oranges":[9,8,7,4]
# }
# purchase=pd.DataFrame(data, index=["Robert","Lily","Micheal","Akon"])
# print(purchase)
# print(purchase.loc["Robert"])

# data={
#     "Oranges":[8,3,8,7],
#     "apples":[6,5,4,3],
#     "banana":[8,6,5,6],
#     "Kiwi":[4,3,2,5]
# }
# purchases=pd.DataFrame(data,index=["Ravikanth","Shashikanth","KasuBai","Shalini",])
# print(purchases)
# print(purchases.loc["Shalini"])

# data={
#     "Apples":[5,4,6,3],
#     "Oranges":[3,8,7,5],
#     "Sapoota":[7,9,8,5],
#     "Angur":[1,2,3,4]
# }
# purchases=pd.DataFrame(data, index=["Ravi","Shalini","KasuBai","Khushi"])
# print(purchases.loc["Ravi"])

# data={
#     "Oranges":[6,7,5,4],
#     "Saputa":[3,4,5,2],
#     "Apples":[4,5,6,7],
#     "Banana":[4,5,6,8],
#     "Mango":[3,5,2,4]
# }
# purchase=pd.DataFrame(data, index=["Ravi","Shalini","Khushi","Kasu"])
# print(purchase)
# print(purchase.loc["Khushi"])

# data={
#     "Ten":[10,9,8,7],
#     "Twenty":[29,28,27,26],
#     "Fifty":[10,18,17,16],
#     "Hundred":[19,17,15,14]
# }
# purchase=pd.DataFrame(data, index=["Ravi","Kasu","Khushi","Shalini"])
# print(purchase)
# print(purchase.loc["Kasu"])

# data={
#     "iPhone":[2,3,4,5],
#     "Samsung":[1,2,3,2]
# }
# purchase=pd.DataFrame(data, index=["Ravikanth","Shalini","Kasubai","Khushi"])
# print(purchase)
# print(purchase.loc["Khushi"])

# data={
#     "iPhone":[4,3,2,1],
#     "Xiome":[1,2,3,1]
# }
# purchase=pd.DataFrame(data, index=["Ravi","Shine","Jackson","Micheal"])
# print(purchase)
# print("-"*40)
# print(purchase.loc["Shine"])
# print(purchase.head())

# df=pd.read_csv("Sample-Spreadsheet-100-rows.csv")
# print(df.head(5))

# data={
#     "apples":[6,5,4,3,2]
# }
# purchase=pd.DataFrame(data, index=["a","b","c","d","e"])
# print(purchase)
# print(purchase.loc["a"])

# data={
#     "Apples":[3,4,5,6,7]
# }
# purchase=pd.DataFrame(data)
# print(purchase)
# print(purchase.loc[1])
# print(purchase.info())
# print(purchase.head(3))

# data={
#     "Oranges":[5,6,7,8]
# }
# purchase=pd.DataFrame(data)
# print(purchase)
# print(purchase.info())
# print(purchase.loc[0])
# print(purchase.head(3))

# data={
#     "Chittapur":["Ravikanth","ShashiKanth","KasuBai","Bhabhi"],
#     "Sedam":["Shalini","Khushi","Prakash","Charan"]
# }
# location=pd.DataFrame(data)
# print(location)
# print(location.info())
# print(location.loc[3])

# data={
#     "Honda Shine":["Shashikanth","Prakash","LaximKanth"],
#     "Rolls Roys":["RaviKanth","Charan","Khushi"]
# }
# purchase=pd.DataFrame(data, index=["a","b","c"])
# print(purchase)
# print(purchase.info())

# data={
#     "apples":[1,2,3,4,5]
# }
# purchase=pd.DataFrame(data, index=["a","b","c","d","e"])
# print(purchase)
# print(purchase.info())
# print(purchase.loc["d"])
# print(purchase.shape)
# print("*"*49)
# ser=pd.Series(data=data)
# print(ser)
# print(ser.shape)

# data={"Mon":21, "Tue":23, "Wed":24, "Thur":25,"Fri":26,"Sat":27,"Sun":28}
# ser=pd.Series(data=data, name="Series_from_dict")
# print(ser)
# print(ser.info())
# print(ser.shape)

# dates={"Mon":21,"Tue":22,"Wed":23,"Thu":24,"Fri":25,"Sat":26,"Sun":27}
# ser=pd.Series(dates, name="Dict")
# print(ser)
# print(ser.shape)

# dates={"Ravikanth":28,"Shashikanth":32,"Shalini":30,"Kasubai":50}
# ser=pd.Series(dates, name="from_dict")
# print(ser)
# print(ser.info())
# print(ser.shape)

# dates={"Ravikanth":28, "Shalini":30,"Khushi":8,"Charan":1}
# ser=pd.Series(dates, name="dict")
# print(ser.info())
# print(ser)

# data=pd.DataFrame({"col":pd.Series([22,33,44])})
# # print(data)
# data=pd.Series({"Col":pd.Series([22,23,89])})
# print(data)

# ser=pd.Series(data=7.3, 
#               index=["a","b","c","d"],
#               name="Series_from_dict")
# print(ser)

# ser=pd.Series(data=3.8, index=[1,2,3,4,5,6,7],name="From_Dict")
# print(ser)
# data={
#     "Apple":[1,2,3,4,5]
# }
# df=pd.DataFrame(data=data, index=["a","b","c","d","e"], columns=None, dtype="int8")
# print(df.info())
# print(df)
# data={
#     "Salaries":[12000,13000,14000,15000]
# }
# df=pd.DataFrame(data=data, index=["ravikanth","Shashikanth","Shalini","khushi"], columns=None, dtype="int64")
# print(df)

# data={
#     "Salaried":[19000,18000,21000,22000]
# }
# df=pd.DataFrame(data=data, index=["Ravikanth","Shashikanth","Shalini","Kasubai"], columns=None,dtype="int64")
# print(df)

# data={
#     "Salaries":[12000,120000,12000000,120000000]
# }
# df=pd.DataFrame(data=data, index=["ravikanth","Shashikanth","Shalini","Khushi"], columns=None, dtype="int64")
# print(df)

# df=pd.DataFrame({"Col":[1,2],"Col2":[3,4],"Col3":[6,7]})
# print(df)

# df=pd.DataFrame({"Col":[4,5],"Col1":[6,7],"Col3":[9,8],"Col4":[6,3]},index=["A","B"], columns=None, dtype="int64")
# print(df)

# df=pd.DataFrame({"Column 1":[2,3],"Column 2":[4,5],"Column 3":[6,7],"Column 4":[8,9]}, columns=None, dtype="int64")
# print(df)
# data=pd.DataFrame({"Col1":[2,3,4,5],"Col2":[6,7,8,9],"Col3":[10,11,12,13],"Col4":[14,15,16,17]}, index=["A","B","C","D"], columns=None, dtype="int8")
# print(data)
# df=pd.DataFrame({"Col":[80000,90000],"Col2":[100000,110000],"Col3":[120000,130000],"Col4":[140000,160000]}, index=["Ravikanth","Shashikanth"], dtype="int32", columns=None)
# print(df)
# data={
#     "apples":[3,2,1,0],
#     "oranges":[4,2,1,4]
# }
# df=pd.DataFrame(data)
# print(df)
# df1=pd.DataFrame(data, index=["Robert","Lily","June","david"], dtype="int8", columns=None)
# print(df1)

# age=[["Hritik",29,"Male"],["Shah Rukh khan",67,"Male"],
#      ["Amir Khan",66,"Male"],["Deepika",35,"Female"]]
# df=pd.DataFrame(age, columns=["Name","Age","Gender"])
# print(df)

# age=[["Lilly",89,"Female"],["Leela",77,"Female"],
#      ["Prashant",66,"Male"],["Vishnu",72,"Male"]]
# df=pd.DataFrame(age,columns=["Name","Age","Gender"])
# print(df)

# gods=[["Balaji",1400,"Tirumala"],["Buddha",2500,"Bodhgaya"],
#      ["Kedarnath",2700,"Badrinath"],["Krishna",1000,"KurukShetra"]]
# df=pd.DataFrame(gods, columns=["Name","Km","Location"])
# print(df)
# person=[["ravikanth",28,"Wadi"],["ShashiKanth",32,"Wadi"],["Shalini",30,"Wadi"],["Kasubai",50,"Wadi"]]
# df=pd.DataFrame(person, columns=["Name","Age","Birth_Place"])
# print(df)

# mobile=[["ravikanth",8999,"Xiome"],["ShashiKanth",80000,"iPhone"],
#         ["Shalini",8000,"redme"],["kasubai",7999,"redme"]]
# df=pd.DataFrame(mobile, columns=["Name","Price","cell_phone"])
# print(df)

# df=pd.read_csv("Sample-Spreadsheet-100-rows.csv")
# print(df.head(6))
# df=pd.read_csv("Sample-Spreadsheet-100-rows.csv")
# print(df.head(6))


# df=pd.read_json("jason2.json")
# print(df)

import numpy as np
import pandas as pd
import sqlite3
# conn=sqlite3.connect("chinook.db")
# print("data base connected")
# conn.execute('''
# CREATE TABLE Purchase1(
# Code INTEGER,
# Name NVARCHAR,
# Budget NVARCHAR);'''
# )

# conn.execute("INSERT INTO Purchase1(Code,Name, Budget)VALUES(91,'Ravikanth',20000);")
# conn.execute("INSERT INTO Purchase1(Code,Name,Budget)VALUES(23,'Samsung',8800);")
# conn.commit()
# df=pd.read_sql_query("SELECT *FROM Purchase1",conn)
# print(df)

# conn=sqlite3.connect("Climate.db")
# print("Table Data Base Created")
# conn.execute('''
# CREATE TABLE Temp3(
# Data FLOAT,
# Temperature FLOAT,
# Increase FLOAT
# );''')

# conn.execute("INSERT INTO Temp3(Data, Temperature, Increase)VALUES(15.5,32.8,1.5);")
# conn.execute("INSERT INTO Temp3(Data, Temperature, Increase)VALUES(15.5, 37,2.0);")
# conn.commit()
# df=pd.read_sql_query("SELECT *FROM Temp3",conn)
# print(df)

# conn=sqlite3.connect("person.db")
# conn.execute('''
# Create Table Person2(
# Gender NVARCHAR,
# Height INTEGER,
# Weight INTEGER
# # );''')
# conn.execute("INSERT INTO Person1(Gender, Height, Weight)VALUES('Male',165,54);")
# conn.execute("INSERT INTO Person2(Gender, Height, Weight)VALUES('Female',165,47);")
# conn.commit()
# df=pd.read_sql_query("SELECT *FROM Person2",conn)
# print(df) 
# conn=sqlite3.connect("person.db")
# conn.execute("UPDATE Person2 SET Gender='Male',Height=88, Weight=77;")
# conn.commit()
# conn=sqlite3.connect("person.db")
# df=pd.read_sql_query("SELECT *FROM Person2",conn)
# print(df)


conn=sqlite3.connect("person.db")
cur=conn.cursor()
cur.execute("UPDATE Person2 SET Gender='Transgender', Height=187, Weight=1=67")
conn.commit()
df=pd.read_sql_query("SELECT *FROM Person2",conn)
print(df)