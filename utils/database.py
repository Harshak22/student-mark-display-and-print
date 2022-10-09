import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varshu@2001",
    database="sql_training"
)
print("connected")
cursor=db.cursor()
cursor.execute('create table if not exists student(id int primary key AUTO_INCREMENT,name varchar(100),Email varchar(200),password varchar(200),year int,examdate date,examtype varchar(200) , Maths int,Chemistry int,English int,Biology int)')
db.commit()
db.close()

