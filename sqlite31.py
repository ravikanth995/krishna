import pandas as pd
import sqlite3 
# conn=sqlite3.connect("rest.db")
# conn.execute('''
#     CREATE TABLE Purchase1(
#     Code   INTEGER,
#     Name   NVARCHAR,
#     Budget REAL
#     );''')
# conn.commit()
# conn.execute("INSERT INTO Purchase1(Code,Name,Budget)Values(null, 'IT11',65000)")
# df=pd.read_sql_query("SELECT* FROM Purchase1",conn)
# print(df)
# conn=sqlite3.connect('rest.db')
# cur=conn.cursor()
# cur.execute("INSERT INTO Purchase1(Code,Name,Budget)VALUES('AUTOCAD','HTML',20);")
# cur.execute("INSERT INTO Purchase1(Code,Name,Budget)VALUES('Quick Hill','Python',23);")
# cur.execute("INSERT INTO Purchase1(Code,Name,Budget)VALUES('Key Board','JavaScript',2);")
# cur.execute("INSERT INTO Purchase1(Code,Name,Budget)VALUES('Mouse','CoreJava',4);")
# conn.commit()
# df=pd.read_sql_query("SELECT * FROM Purchase1 limit 4,4",conn)
# print(df)

# conn=sqlite3.connect("rest.db")
# cur=conn.cursor()
# cur.execute("UPDATE Purchase1 SET Budget= Budget+5")
# conn.commit()
# print("Code\tName\tBudget\n")
# cursor=cur.execute("SELECT *FROM Purchase1")
# for i in cursor:
#     print(i[0],"--->",i[1],"--->",i[2],"\n")
# conn.close()    

# df=pd.read_json("jason2.json")
# # print(df.head(4))
# print(df.tail(2))
# print(df.info())
# print(df.shape)

df=pd.read_json("jason2.json")
# print(df)
# print(df.head(5))
# print(df.tail(4))
#Duplicates
# df1=df.to_csv("Sample-Spreadsheet-100-rows.csv",index=None,index_label="Title")
# print(df.head(4))

# temp=df.append(df)
# # # print(df.head(3))
# # # print(temp)
# temp=temp.drop_duplicates()
# # print(temp)
# print(temp.rename(columns={"Budget":'Budet Allocated'}, inplace=True))

