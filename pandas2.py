import pandas as pd
# import json
import sqlite3
data = {
    'apples': [3, 2, 0, 1]
	}
# purchases = pd.DataFrame(data)
# purchases = pd.DataFrame(data)
# purchases = pd.DataFrame(data,index=['a', 'b', 'c','d'])
# print(purchases)
# purchases.shape
# purchases.loc['b']

# ser = pd.Series(data=data)
# print(ser.shape)

# data = {'Mon': 22, 'Tues': 23, 'Wed': 23, 'Thurs': 24, 'Fri': 23, 'Sat': 22, 'Sun': 21}
# series = pd.Series(data=data, name='series_from_dict')
# print(series)

# series = pd.Series(data=7.3, 
#                    index=['a', 'b', 'c', 'd','e'],
#                    name='series_from_scalar')
# print(series)

# data11 = pd.DataFrame({"Col1": pd.Series([22, 33, 38])})
# print(data11)


pd.DataFrame
dtype=pd.Int64Dtype()
# dtype='int8'
df = pd.DataFrame(data=data, index=['a', 'b', 'c','d'],columns=None, dtype='int16')
# df.info()
# print(df)


# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4],
#                    'col3': [5, 6]})
# print(df1)


# data = {
#     'apples': [3, 2, 0, 1], 
#     'oranges': [0, 3, 7, 2]
# }

# purchases = pd.DataFrame(data)

# print(purchases)



# data1 = {
#     'apples': [3, 2, 0, 1], 
#     'oranges': [0, 3, 7, 2]
# }
# purchases = pd.DataFrame(data1)
# purchases = pd.DataFrame(data1, index=['June', 'Robert', 'Lily', 'David'])

# purchases
# genre_col = purchases[['apples','oranges']]
# print(genre_col)


# age = [['Ritik', 99.5, "Male"], ['Bobby', 65.7, "Female"],
# 	['Mona', 85.1, "Female"], ['Virat', 100.0, "Male"]]

# df = pd.DataFrame(age, columns=['Name', 'Marks', 'Gender'])  
# # df.head(2)
# # df.columns
# print(df)



# df.to_csv('ravi.csv',index = None)
# df.to_csv(index = None, header=False)
# print(df)


# df = pd.read_csv('ravi.csv')
# print(df)

# df = pd.read_json('sam.json')
# print(df)


conn = sqlite3.connect('ravi.db')
 
conn.execute('''
CREATE TABLE Purchase (
   Code INTEGER ,
   Name NVARCHAR,
   Budget REAL
 );''')
 
print(conn.commit())