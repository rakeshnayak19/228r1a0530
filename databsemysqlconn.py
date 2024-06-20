import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydb")
mycurs=mydb.cursor()
#
#mycurs.execute("show databases")
#mycurs.execute("create database mydb")
#mycurs.execute("show tables")
#mycurs.execute("create table User_my(name varchar(20),email varchar(40) ,Password varchar(20))")
#sql="Insert into user_my values(\"bunny\",\"dcfgh\",\"yvhj\");"
#val=("Manogna","abc@gmail.com","123452")
mycurs.execute("Insert into user_my values(\"bunny\",\"dcfgh\",\"yvhj\");")
#mycurs.execute("select * from User_my")
#mycurs.fetchall()
#for i in mycurs:
 #  print(i)