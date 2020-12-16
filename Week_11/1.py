import mysql.connector
import statistics as st
import matplotlib.pyplot as plt
import random as rd
from faker import Faker

faker = Faker()

dbname = "taxipark"

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
    mycursor.execute("CREATE DATABASE {}".format(name))

# createDatabase(dbname)

def cab_migration(tb="cabs"):
    query = "CREATE TABLE IF NOT EXISTS {} (" \
            "id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
            "plate VARCHAR(10) NOT NULL)".format(tb)
    mycursor.execute(query)

# cab_migration()

def work_migration(tb="work"):
    query = "CREATE TABLE IF NOT EXISTS {} (" \
            "id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
            "cab_id INT(11) UNSIGNED NOT NULL,"\
            "hours FLOAT NOT NULL,"\
            "FOREIGN KEY (cab_id) REFERENCES cabs(id))".format(tb)
    mycursor.execute(query)

# work_migration()


def randLicensePlateGenerator():
    return faker.bothify(text = '??-###-??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def insert_cabs_method():
    data=[]
    for i in range(1,101):
        plate = randLicensePlateGenerator()
        while plate in data:
            plate = randLicensePlateGenerator()
        data.append([plate])

    sql = "INSERT INTO cabs (plate) VALUES (%s)"
    mycursor.executemany(sql, data)
    mydb.commit()
    return mycursor.rowcount

# insert_cabs_method()


def insert_work_method():
    cabs = executequery("SELECT id FROM cabs")

    data=[]
    for i in cabs:
        for k in range(1, 8):
            data.append([i[0], round(rd.uniform(0,12),2)])

    sql = "INSERT INTO work (cab_id, hours) VALUES (%s, %s)"
    mycursor.executemany(sql, data)
    mydb.commit()
    return mycursor.rowcount

# insert_work_method()

def executequery(sql):
    mycursor.execute(sql)
    return mycursor.fetchall()

def make_scatter():
    cabs = executequery("SELECT id FROM cabs")
    data=[]
    for i in cabs:
        data.append(executequery("SELECT hours FROM work WHERE cab_id="+str(i[0])))
    print(data)
    weekAverages = []
    for t in range(0,7):
        day=[]
        for i in data:
            day.append(i[t][0])
        weekAverages.append(st.mean(day))

    print(weekAverages)
    print("Standart Devitation is: {}".format(st.stdev(weekAverages)))

    x = range(1,8)
    y = weekAverages

    plt.scatter(x,y)
    plt.show()

make_scatter()

