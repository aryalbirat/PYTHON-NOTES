import sqlite3
import os
db_filename = 'database.db'
conn = sqlite3.connect(db_filename)

"""

conn.execute('drop table if exists staff')
print("Table staff Exists/Drop")


#creating table
conn.execute('create table staff(ID int,Name text,Age int,Gender text)')
print("Table staff Created")


#insert Values
conn.execute('insert into staff(ID,Name,Age,Gender) values(0001,"Name 1",21,"M")')
conn.execute('insert into staff(ID,Name,Age,Gender) values(0002,"Name 2",28,"F")')
conn.execute('insert into staff(ID,Name,Age,Gender) values(0003,"Name 3",26,"M")')

conn.commit()
print("Rows are inserted in Table staff Created")

cursor = conn.cursor()

print("Displaying staff Created")

#cursor.execute('select * from staff')
#result = cursor.fetchall()
#result= cursor.fetchone()


"""


result = conn.execute('select * from staff where gender=="M"')
for rows in result:
    print(rows)


result = conn.execute('select Name,Age from staff')
for rows in result:
    print(rows)

