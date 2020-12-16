import matplotlib.pyplot as plt
from scipy import stats as st

x = [8, 9, 2, 3, 5]
y = [18, 19, 20, 17, 16]

slope, intercept, r, p, std_err = st.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
