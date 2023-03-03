import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pstore=pd.read_csv("water_potability.csv")
print(pstore.head())
print(pstore = pstore.dropna())
print(pstore.isnull().sum())
