import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

excelData = pd.read_excel(r'quiz3_data.xlsx')
# print(excelData.head())

print("---------1--------")


def task_1():
    femaleAge = []
    maleAge = []
    for i in excelData.values:
        if i[3] == "Female":
            femaleAge.append(i[5])
        elif i[3] == "Male":
            maleAge.append(i[5])

    print(femaleAge)
    # print(maleAge)

    print("Female Age Mean: {} Standard Devitation: {}".format(st.mean(femaleAge), st.stdev(femaleAge)))


# task_1()

print("---------2--------")


def tast_2():
    countries = excelData['Country'].unique()
    d = {}
    for s in countries:
        d[s] = 0

    for i in excelData.values:
        for k in countries:
            if i[4] == k:
                d[k] += 1
    print(d)
    print(max(d))


# tast_2()

print("---------3--------")


def task_3():
    ages = excelData['Age'].values
    # print(ages)

    plt.hist(ages)
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.title("Age Histogram")
    plt.show()


# task_3()

print("---------4--------")


def task_4():
    countries = excelData['Country'].unique()
    d = {}

    for c in range(0, len(countries)):
        arr = []
        for i in excelData.values:
                if i[4] == countries[c]:
                    arr.append(i[5])
        d[countries[c]] = st.mean(arr)

    print(d)
    print("Youngest people in: {}".format(min(d)))


task_4()
