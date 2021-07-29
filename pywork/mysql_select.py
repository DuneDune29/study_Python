# mysql_select.py

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="m1234",
    database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers2")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)