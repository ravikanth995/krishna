import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import csv 
pstore=pd.read_csv("Statewise_General_Index_july2019_20Aug2020_dec20_2_4.csv")
print(pstore.head(6))
sb.displot(pstore.Karnataka)
# print(plt.show())

# sb.displot(pstore.Karnataka, bins=28, color='g')
# print(plt.title("Consumer price Index of Karnataka State ", fontsize=29, color='red'))
# print(plt.style.use('classic'))

sb.displot(pstore.Karnataka,bins=28, color='g')
plt.title("Consumer Price Index of Karnataka from 2019-2020", fontsize=25, color='green')
# print(plt.show())

# print(pstore["Karnataka"].value_counts())

#Pie Chart
plt.figure(figsize=[4,2])
pstore["Karnataka"].value_counts().plot.pie()
# print(plt.show())

#bar chart
plt.figure(figsize=[9,7])
pstore["Karnataka"].value_counts().plot.bar()
print(plt.show())

m=np.array([[1,6,8],[9,10,12]])
#heat map
sb.heatmap(pstore)
sb.heatmap(m)
# print(plt.show())

# data={
#     "apple":[3,2,1,0],
#     "Oranges":[4,5,6,1]
# }
# purchases=pd.DataFrame(data)
# sb.heatmap(purchases, annot=True, Vmin=15, Vmax=0)
# print(plt.show())

fig=plt.figure(figsize=(12,10), dpi=80)
ax=fig.add_subplot(111, projection='3d')
property(plt.show())

