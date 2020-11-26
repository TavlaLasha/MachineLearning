import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

staffExcel = pd.read_excel(r'file_example_XLS_10.xls')

allinfo = staffExcel.head()
mean = np.mean(staffExcel["Age"])
# print(mean)
ds = np.arange(staffExcel["Age"].min(), staffExcel["Age"].max()+1)
ypoints = mean
print(ypoints)
plt.hist(ds, ypoints)
plt.show()
