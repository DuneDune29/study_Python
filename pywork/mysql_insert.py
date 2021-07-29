# mysql_insert.py

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="m1234",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers2 (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")