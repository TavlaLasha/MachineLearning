import mysql.connector
import random as rd
from faker import Faker

faker = Faker()

dbname = "myTestData"
tbname = "customers"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=dbname
)

mycursor = mydb.cursor()

#1
def createDatabase(name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE {}".format(name))

# createDatabase(dbname)

#2
def migration(tb):
    query = "CREATE TABLE IF NOT EXISTS {} (" \
            "id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
            "name VARCHAR(30)," \
            "lastname VARCHAR(30)," \
            "age INT," \
            "salary INT," \
            "gender VARCHAR(20))".format(tb)
    mycursor.execute(query)

# migration(tbname)

#3
def randStringGenerator(len):
    return ''.join(faker.random_letters(length=len))

def data_generator():
    arr = []
    name = randStringGenerator(rd.randint(4,15))
    lastname = randStringGenerator(rd.randint(15,40))
    age = rd.randint(20, 65)
    salary = rd.randint(1000, 10000)
    gender = rd.choice(["Male", "Female"])
    arr.extend([name, lastname, age, salary, gender])

    return arr

def insert_method(data, tb):
    sql = "INSERT INTO {} (name, lastname, age, salary, gender) VALUES (%s, %s, %s, %s, %s)".format(tb)
    mycursor.executemany(sql, data)
    mydb.commit()
    return mycursor.rowcount


def write_data():
    count = 0
    data = []

    for i in range(1, 1000002):
        if len(data) >= 10000:
            count += insert_method(data, tbname)
            print(count, "rows inserted")
            data = []
        data.append(data_generator())

# write_data()

def executequery(sql, pr = True):
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if pr:
        print(myresult)
    return myresult

#4
executequery("SELECT gender, COUNT(gender) FROM customers GROUP BY gender ORDER BY COUNT(gender) DESC LIMIT 1")

#5
executequery("SELECT COUNT(age) FROM customers WHERE age < 50")

#6
executequery("SELECT AVG(salary) FROM customers")
executequery("SELECT salary FROM customers GROUP BY salary ORDER BY COUNT(*) DESC LIMIT 1")
# executequery("SET @rowindex := -1; SELECT AVG(salary) (SELECT @rowindex:=@rowindex + 1 AS rowindex, salary FROM customers ORDER BY salary) AS g WHERE g.rowindex IN (FLOOR(@rowindex / 2) , CEIL(@rowindex / 2));")
executequery("SELECT STD(salary) FROM customers")

#7
executequery("SELECT MAX(age) FROM (SELECT age FROM customers ORDER BY age LIMIT 700000) AS age")

#8
executequery("SELECT MAX(age) FROM (SELECT age FROM customers ORDER BY age LIMIT 870000) AS age")

#9
executequery("SELECT LENGTH(name) FROM customers GROUP BY LENGTH(name) ORDER BY COUNT(*) DESC LIMIT 1")
