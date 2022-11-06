import pandas as pd
# data={ 'apple':[1,2,3,4], 'oranges':[6,7,8,9]
# }
# purchases=pd.DataFrame(data,index=['a','b','c','d'])  
# or pd.DataFrame(data) for  not indexing
# print(purchases)
# ser=pd.pandas(data=data)
# ser.shape


data={ 'Mon', 21, 'Tue',22, 'Wed',23, 'Thu',24, 'Fri',25, 'Sat',26, 'Sun',27}
series=pd.Series(data=data, name='series_from_dict')
print(series)


