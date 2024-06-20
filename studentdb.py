import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="customerdata")
mycursor = conn.cursor()
if(mycursor):
    print("sucess")
else:
    print("problem")
query='create table studentdatab(name varchar(100),rollno varchar(100))'
#query='drop table studentdatab'
mycursor.execute(query)
