import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

staffExcel = pd.read_excel(r'file_example_XLS_10.xls')

allinfo = staffExcel.head()
allAges = staffExcel["Age"]
mean = st.mean(allAges)
meanAge = round(st.mean(allAges))
mode = st.mode(allAges)
median = st.median(allAges)
std = st.stdev(allAges)
maxAge = max(allAges)
minAge = min(allAges)

x = []
y = []
for i in allAges:
    c = 0
    if i in x:
        continue
    else:
        for k in allAges:
            if i == k:
                c += 1
        x.append(i)
        y.append(c)

print(x, y)

plt.hist(x)
plt.show()
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
plt.show()
plt.bar(x, y)
plt.show()

