import pandas as pd
import random as rd
import numpy as np
from scipy import stats as st

print("-------1---------")
nums = []
dividers = list(range(2, 1000))

for i in range(10, 3001):
    c = 0
    for k in dividers:
        if i == k:
            continue
        if i % k == 0:
            c += 1
            if c >= 2:
                nums.append(i)
                break
print(nums)

print("-------2---------")
numstring = ""
for i in range(1, 11):
    numstring += str(round(rd.uniform(1, 10), 2)) + "-"
numstring = numstring[:-1]

numbers = list(map(float, numstring.split("-")))
print(numbers)

data = []
for x in numbers:
    y = 3 * x - 2
    data.append([x, y])

df = pd.DataFrame(data)
writer = pd.ExcelWriter('numbers.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheetOne', index=False)
writer.save()

print("-------3---------")
gelist = "აბგდევზთიკლმნოპჟრსტუფღყშცძწხჯჰ"
words = []


def wordGenerator(length, symbols):
    word = ""
    for i in range(1, length + 1):
        word += symbols[rd.randint(0, len(symbols) - 1)]

    return word


for k in range(1, 21):
    words.append(wordGenerator(10, gelist))
words.sort()
print(words)

print("-------4---------")
data = []
nums = list(range(1, 501))

for i in range(1, 501):
    rd.shuffle(nums)
    randSymb = rd.choice(['A', 'B', 'C', 'D', 'E', 'F'])
    randint = rd.randint(0, 101)
    randfloat = rd.uniform(2, 5)
    randuniqueunt = nums[i - 1]
    data.append([randSymb, randint, randfloat, randuniqueunt])

df = pd.DataFrame(data)
writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1', index=False)
writer.save()

excelFile = pd.read_excel(r'data.xlsx')
mean = np.mean(excelFile[1])
mode = st.mode(excelFile[1])[0][0]
median = np.median(excelFile[1])
sd = np.std(excelFile[1])
print(mean, "; ", mode, "; ", median, "; ", sd)

mostCommonSymb = st.mode(excelFile[0])[0][0]
print("Most Common Symbol: {}".format(mostCommonSymb))

mean3 = np.mean(excelFile[2])
sd3 = np.std(excelFile[2])
print(mean3, "; ", sd3)
