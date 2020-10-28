import mysql.connector
from dateutil.relativedelta import relativedelta
from datetime import datetime
import random as rd
from faker import Faker

faker = Faker()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myml"
)

mycursor = mydb.cursor()


def datagenerator(gender):
    arr = []
    name = ''
    lastname = ''
    if gender == "Male":
        name = faker.first_name_male()
        lastname = faker.last_name_male()
    elif gender == "Female":
        name = faker.first_name_female()
        lastname = faker.last_name_female()

    date = faker.date_of_birth()
    age = relativedelta(datetime.now(), date).years
    reg_date = datetime.now()
    password = faker.password(length=8, special_chars=True, upper_case=True)
    gender = gender
    arr.extend([name, lastname, age, date, reg_date, password, gender])

    return arr


def insertmethod(data):
    sql = "INSERT INTO users (name, lastname, age, date, reg_date, password, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, data)
    mydb.commit()
    return mycursor.rowcount


def writedata():
    count = 0
    data = []

    for i in range(1, 5000001):
        if len(data) >= 10000:
            count += insertmethod(data)
            print(count, "rows inserted")
            data = []
        data.append(datagenerator(rd.choice(['Female', 'Male'])))


def executequery(sql):
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


print("---------------1--------------")
executequery("SELECT age, date, reg_date, gender FROM users LIMIT 3")
print("---------------2--------------")
executequery("SELECT * FROM users LIMIT 2")
print("---------------3--------------")
executequery("SELECT * FROM users WHERE id>1 AND id<4")
print("---------------4--------------")
executequery("SELECT * FROM users WHERE id<2 OR id>=4")
print("---------------5--------------")
executequery("SELECT * FROM users WHERE date='2014-07-04'")
print("---------------6--------------")
executequery("SELECT * FROM users WHERE date>'2014-07-04'")
print("---------------7--------------")
executequery("SELECT * FROM users WHERE date BETWEEN '2014-06-04' AND '2014-07-04'")
print("---------------8--------------")
executequery("SELECT * FROM users WHERE age>=10 AND age<=18")
