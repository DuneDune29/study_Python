# mysql_limit.py

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="m1234",
  database="test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers2 ORDER BY name DESC LIMIT 5"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)