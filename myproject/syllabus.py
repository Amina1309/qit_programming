import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


#An example of working with the numpy library
Z = np.random.randint(10, size=(1,10))
print('The original one-dimensional vector Z of random integers up to 10:\n', Z)
Z.sort()
print('Sorted vector Z:\n', Z)


#An example of working with the scipy and matplotlib library
x = np.arange(5, 20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x, y)
x1 = np.arange(6, 12)
y1 = f(x1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()
