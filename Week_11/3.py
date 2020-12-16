import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st
import random as rd

x = []
y = []
for i in range(0, 60):
    x.append(rd.randint(10, 20))
    y.append(rd.randint(500, 1000))

print(x)
print(y)

mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(min(x), max(x), 1000)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
