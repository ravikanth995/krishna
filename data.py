import sqlite3
import pandas as np 
conn = sqlite3.connect('test.db')
conn.execute('''
CREATE TABLE Purchase (
Code INTEGER ,
Name NVARCHAR,
Budget REAL
);''')
 
conn.commit()

