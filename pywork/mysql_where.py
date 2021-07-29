# mysql_where.py

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="m1234",
    database="test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers2 WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)