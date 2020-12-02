import pandas as pd
import random as rd
import statistics as st
from faker import Faker

faker = Faker()

staffExcel = pd.read_excel(r'staff_1000.xlsx')
nums = list(range(1, 101))
rd.shuffle(nums)


def excel_creator():
    print("---------------1--------------")
    data = []

    for i in range(1, 101):
        dt = [faker.lexify(text='??????????'), rd.randint(0, 10), rd.randint(1, 7), nums[i - 1]]
        data.append(dt)

    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheetOne', index=False)
    writer.save()

    print("---------------2--------------")

    data = []
    for i in range(1, 51):
        rd.shuffle(nums)
        dt = [nums[i - 1], faker.first_name(), faker.last_name(), rd.randint(2000, 5000)]
        data.append(dt)

    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data.xlsx', engine='openpyxl', mode='a')
    df.to_excel(writer, sheet_name='sheetTwo', index=False)
    writer.save()

    print("---------------3--------------")

    wr = pd.ExcelWriter('datanew.xlsx', engine='openpyxl', mode='a')
    data1 = pd.read_excel(r'data.xlsx', sheet_name="sheetOne")
    data2 = pd.read_excel(r'data.xlsx', sheet_name="sheetTwo")
    data1.to_excel(wr, sheet_name="sheetOne", index=False)
    data2.to_excel(wr, sheet_name="sheetTwo", index=False)
    wr.save()

    print("---------------4--------------")

    arr = []
    for k in data1[0]:
        if 'a' in k:
            arr.append([k])
    df = pd.DataFrame(arr)
    df.to_excel(wr, sheet_name="sheet3", index=False)
    wr.save()

    print("---------------5--------------")

    wr = pd.ExcelWriter('datanew.xlsx', engine='openpyxl', mode='a')
    data2 = pd.read_excel(r'data.xlsx', sheet_name="sheetTwo")
    arr = []
    for k in data2[3]:
        arr.append([k])
    arr.sort(reverse=True)
    df = pd.DataFrame(arr)
    df.to_excel(wr, sheet_name="sheet4", index=False)
    wr.save()


print("---------------6--------------")
print(staffExcel)
print(st.mean(staffExcel["Age"]))
print(round(st.mean(staffExcel["Age"])))
# print(st.multimode(staffExcel["Age"]))
print(st.median(staffExcel["Age"]))
print(max(staffExcel["Age"]))
print(min(staffExcel["Age"]))

print("---------------7--------------")
data = []
for i in staffExcel["Age"]:
    if 30 < i < 50:
        data.append(i)

df = pd.DataFrame({ 'Age': data})
writer = pd.ExcelWriter('staff_age.xlsx', engine='openpyxl')
df.to_excel(writer, index=False)
writer.save()
