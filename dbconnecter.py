import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="12345")
mycursor = conn.cursor()
query='create table studentdb(name varchar(100),rollno varchar(100))'
mycursor.execute(query)