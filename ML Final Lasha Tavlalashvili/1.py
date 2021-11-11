import pandas as pd
import random as rd
import statistics as st
import matplotlib.pyplot as plt
from faker import Faker

faker = Faker()

ean = []
for i in range(70):
    ean.append(faker.ean(length=13))


def dataCreator():
    data = []

    for i in range(0, 70):
        data.append([ean[i], faker.pystr(min_chars=5, max_chars=10), faker.random_int(min=500, max=5000),
                     faker.random_int(min=0, max=50)])
    return data


def excelCreator():
    dt = []
    for i in range(30):
        data = dataCreator()
        for k in data:
            dt.append(k)
    rd.shuffle(dt)

    sum = []
    for i in dt:
        sum.append(i[2])
    priceMean = st.mean(sum)

    print("---------6----------")
    # data = []
    # for k in range(30):
    #     sum = 0
    #     for i in dt:
    #         sum += int(i[k][3])
    #     data.append(sum)
    # plt.scatter(range(30), data)
    # plt.show()

    print("---------5----------")
    data2 = []
    for i in dt:
        if (i[2] > priceMean):
            data2.append(i)

    print("---------7----------")
    dict = {}
    data = []
    for i in ean:
        count = 0
        for k in dt:
            if(i == k[0]):
                count += k[3]
        data.append([i, count])
    # print(dict)

    print(st.mean(dict.values()))
    print(st.stdev(dict.values()))




    df = pd.DataFrame(dt)
    df2 = pd.DataFrame(data2)
    writer = pd.ExcelWriter('cond.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1', index=False)
    df2.to_excel(writer, sheet_name='sheet2', index=False)
    writer.save()


excelCreator()
