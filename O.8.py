Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========================== RESTART: C:/VENOM/8.1.py ===========================
Table staff Exists/Drop
Table staff Created
Rows are inserted in Table staff Created
Displaying staff Created
(1, 'Name 1', 21, 'M')
(2, 'Name 2', 28, 'F')
(3, 'Name 3', 26, 'M')
1
1

=========================== RESTART: C:/VENOM/8.1.py ===========================
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')

=========================== RESTART: C:/VENOM/8.1.py ===========================
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')
Traceback (most recent call last):
  File "C:/VENOM/8.1.py", line 42, in <module>
    result = conn.execute('select * Name,Age from staff')
sqlite3.OperationalError: near "Name": syntax error

=========================== RESTART: C:/VENOM/8.1.py ===========================
(1, 'Name 1', 21, 'M')
(3, 'Name 3', 26, 'M')
('Name 1', 21)
('Name 2', 28)
('Name 3', 26)

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Traceback (most recent call last):
  File "C:/VENOM/8.2.py", line 18, in <module>
    conn.execute('insert into (Roll_no,subject,Phone_no,City) values(0001,"subject 1",21,"KTM")')
sqlite3.OperationalError: near "(": syntax error

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'subject 1', 21, 'KTM')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'subject 1', 21, 'KTM')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')
(1, 'KTM')
(2, 'PKR')
(3, 'BIRATNAGAR')

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
Traceback (most recent call last):
  File "C:/VENOM/8.2.py", line 41, in <module>
    conn.execute(query)
sqlite3.OperationalError: unrecognized token: ":"

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'subject 1', 21, 'KATHMANDU')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'subject 1', 21, 'KATHMANDU')
(2, 'subject 2', 28, 'KATHMANDU')
(3, 'subject 3', 26, 'KATHMANDU')

========================== RESTART: C:/VENOM/8.2.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'subject 1', 21, 'KATHMANDU')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')

========================== RESTART: C:/VENOM/8.3.py =========================

========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'subject 1', 21, 'KTM')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')

========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')

========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Traceback (most recent call last):
  File "C:/VENOM/8.3.py", line 38, in <module>
    conn.execute("DELETE from student where City='KTM'")
sqlite3.OperationalError: no such table: student

========================== RESTART: C:/VENOM/8.3.py =========================
Traceback (most recent call last):
  File "C:/VENOM/8.3.py", line 37, in <module>
    conn.execute("DELETE from student where City='KTM'")
sqlite3.OperationalError: no such table: student
>>> 
========================== RESTART: C:/VENOM/8.3.py =========================
>>> 
========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'KTM')
(2, 'PKR')
(3, 'BIRATNAGAR')
>>> 
========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'KTM')
(2, 'PKR')
(3, 'BIRATNAGAR')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')
>>> 
========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Traceback (most recent call last):
  File "C:/VENOM/8.3.py", line 37, in <module>
    conn.execute("DELETE from student where City='KTM'")
sqlite3.OperationalError: no such table: student
>>> 
========================== RESTART: C:/VENOM/8.3.py =========================
Table student Exists/Drop
Table student Created
Rows are inserted in Table student Created
Displaying student Created
(1, 'KTM')
(2, 'PKR')
(3, 'BIRATNAGAR')
(2, 'subject 2', 28, 'PKR')
(3, 'subject 3', 26, 'BIRATNAGAR')
