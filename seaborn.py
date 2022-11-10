import pandas as pd
pstore=pd.read_csv('size.csv')
pstore.head(6)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(pstore.GameNumber)
plt.show()
