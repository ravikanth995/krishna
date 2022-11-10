import sqlite3
import pandas as pd

# import sqlite3
 
conn = sqlite3.connect('test.db')
 
conn.execute('''
CREATE TABLE Purchase (
   Code INTEGER ,
   Name NVARCHAR,
   Budget REAL
 );''')
 
conn.commit()
# conn=sqlite3.connect('test.db')
# conn.execute('''
# CREATE TABLE Purchase(
#     Code INTEGER ,
#     Name  NVARCHAR,
#     Budget  REAL

# );''')


conn.commit()

conn.execute("INSERT INTO Purchase(Code,Name,Budget) VALUES (null,'IT11',65000);")
#conn.execute("INSERT INTO Purchase(Code,Name,Budget) VALUES (null,'IT11',65000);") 
#conn.execute("INSERT INTO Purchase(Code,Name,Budget) VALUES(null,'IT11',65000);") 

df=pd.read_sql_query("SELECT *FROM Purchase", conn)
df.to_csv('new_purchase.csv')
#df.to_json("new_purchase.json")
#df.to_sql("new_purchase", conn)

df=pd.read_csv('new_purchase.csv')
df.head(5)
#df.tail()
#df.info()
df.shape()