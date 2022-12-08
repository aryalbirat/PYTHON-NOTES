import sqlite3
import os
db_filesubject = 'database2.db'
conn = sqlite3.connect(db_filesubject)



conn.execute('drop table if exists student')
print("Table student Exists/Drop")


#creating table
conn.execute('create table student(Roll_no int,subject text,Phone_no int,City text)')
print("Table student Created")


#insert Values
conn.execute('insert into student(Roll_no,subject,Phone_no,City) values(0001,"subject 1",21,"KTM")')
conn.execute('insert into student(Roll_no,subject,Phone_no,City) values(0002,"subject 2",28,"PKR")')
conn.execute('insert into student(Roll_no,subject,Phone_no,City) values(0003,"subject 3",26,"BIRATNAGAR")')

conn.commit()
print("Rows are inserted in Table student Created")

cursor = conn.cursor()

print("Displaying student Created")

#cursor.execute('select * from student')
#result = cursor.fetchall()
#result= cursor.fetchone()


"""result = conn.execute('select Roll_no,City from student')
for rows in result:
    print(rows)

"""

query = "update student set City='KATHMANDU'where City='KTM'"
conn.execute(query)
conn.commit()

result = conn.execute('select * from student ')
for rows in result:
    print(rows)



