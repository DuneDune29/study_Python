# table.py

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="m1234",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")