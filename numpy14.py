#numpy sorting and searching

import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(np.sort(a))
print(np.sort(a, axis=None))

a=np.array([1,3,2])
np.argsort(a)

b=np.arange(6)
print(b)
a=b[2]
print(np.argmax(a))
