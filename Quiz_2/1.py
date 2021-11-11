import mysql.connector
import statistics as st
from scipy import stats as sc
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from faker import Faker

faker = Faker()

dbname = "educenter"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=dbname
)

mycursor = mydb.cursor()


def createDatabase(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(name))


# createDatabase(dbname)

def student_migration(tb="students"):
    query = "CREATE TABLE IF NOT EXISTS {} (" \
            "id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
            "pn INT(10) NOT NULL," \
            "hours FLOAT NOT NULL)".format(tb)
    mycursor.execute(query)


# student_migration()

def randStudentGenerator():
    ids = list(range(100, 1000))
    rd.shuffle(ids)
    data = []
    for i in range(0, 100):
        for k in range(0, 7):
            data.append([ids[i], round(rd.uniform(0, 5), 2)])
    return data


# 1,2
def add_students_todb(data):
    sql = "INSERT INTO students (pn, hours) VALUES (%s, %s)"
    mycursor.executemany(sql, data)
    mydb.commit()
    return mycursor.rowcount


# add_students_todb(randStudentGenerator())

def executequery(sql):
    mycursor.execute(sql)
    return mycursor.fetchall()


# 3
def student_days():
    studentspn = executequery("SELECT DISTINCT pn FROM students")
    students = []
    for i in studentspn:
        students.append(executequery("SELECT hours FROM students WHERE pn=" + str(i[0])))

    return students


def make_scatter():
    students = student_days()
    weekAverages = []
    for t in range(0, 7):
        day = []
        for i in students:
            day.append(i[t][0])
        weekAverages.append(st.mean(day))

    print(weekAverages)

    x = range(1, 8)
    y = weekAverages

    plt.scatter(x, y)
    plt.show()  # Y-ze gamovitane kviris dgeebi da X-ze yvela studentis saatebis sashualo. rogorc pirobashi iyo ise upro martivia magram agar shevcvale


make_scatter()


# 4
def mean_sd_min_max():
    studentHours = executequery("SELECT hours FROM students")
    hours = []
    for i in studentHours:
        hours.append(i[0])
    print("Mean: {}\nSD: {}\nMin: {}\nMax: {}".format(st.mean(hours), st.stdev(hours), min(hours), max(hours)))


# mean_sd_min_max()

# 5
def percentilef3hour():
    students = student_days()
    # print(students)
    weekDays = []
    for t in range(0, 7):
        day = []
        for i in students:
            day.append(i[t][0])
        weekDays.append(day)

    for i in range(0, 7):
        print("Day {}: ".format(i + 1) + str(sc.percentileofscore(weekDays[i], 3)))

# percentilef3hour()
