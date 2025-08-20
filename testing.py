import numpy as np

a = np.longdouble(2**-64)
b = np.longdouble(1)

print(np.longdouble(np.longdouble(1)+np.longdouble(2**-64)-np.longdouble(1)))