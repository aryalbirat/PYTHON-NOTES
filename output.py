Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========================== RESTART: C:/PYthon/paste.py =========================

 1. Function Basic example
Total :  20

 2. Function with return
Value from add_return() :  20

 3. Function with parameter , argument and return
Value from add_return() :  58
25

 4. Function with default parameter & return
Value from add_return() :  44

 5. Function with default parameter & return
Value from multiply() :  30

======================== RESTART: C:/PYthon/paste.py ========================

 1. Function Basic example
Total :  20

======================== RESTART: C:/PYthon/paste.py ========================

 1. Function Basic example
Showing DOCString : Function add(): calculates sum of variables
Showing __name__ : add
Total :  20

====================== RESTART: C:/PYthon/function1.py ======================


=================== RESTART: C:/PYthon/4.function.test.py ===================

====================== RESTART: C:\PYthon\function1.py ======================
HELLO

====================== RESTART: C:\PYthon\function1.py ======================

====================== RESTART: C:\PYthon\function1.py ======================
HELLO
I AM HERE

====================== RESTART: C:\PYthon\function1.py ======================
HELLO
I AM HERE
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 8, in <module>
    print(HELLO.__NAME.__)
NameError: name 'HELLO' is not defined

====================== RESTART: C:\PYthon\function1.py ======================
HELLO
I AM HERE
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 8, in <module>
    print(hello.__name.__)
AttributeError: 'function' object has no attribute '__name'. Did you mean: '__name__'?

====================== RESTART: C:\PYthon\function1.py ======================
HELLO
I AM HERE
hello

====================== RESTART: C:\PYthon\function1.py ======================
HELLO
I AM HERE
hello

====================== RESTART: C:\PYthon\function1.py ======================
HI
I AM HERE
hello
 THIS
FUNCTION
SHOWS
HELLO

====================== RESTART: C:\PYthon\function1.py ======================
HI
I AM HERE
hello
 THIS
FUNCTION
SHOWS
HELLO
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 20, in <module>
    add()
  File "C:\PYthon\function1.py", line 18, in add
    print("TOTAL=",x)
NameError: name 'x' is not defined

====================== RESTART: C:\PYthon\function1.py ======================
HI
I AM HERE
hello
 THIS
FUNCTION
SHOWS
HELLO
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 20, in <module>
    add(10,20)
TypeError: add() takes 0 positional arguments but 2 were given

====================== RESTART: C:\PYthon\function1.py ======================
HI
I AM HERE
hello
 THIS
FUNCTION
SHOWS
HELLO
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 20, in <module>
    add(10,20)
  File "C:\PYthon\function1.py", line 18, in add
    print("TOTAL=",x)
NameError: name 'x' is not defined

====================== RESTART: C:\PYthon\function1.py ======================
HI
I AM HERE
hello
 THIS
FUNCTION
SHOWS
HELLO
TOTAL= 30

====================== RESTART: C:\PYthon\function1.py ======================
TOTAL= 30

====================== RESTART: C:\PYthon\function1.py ======================
TOTAL= 30
TOTAL= 5

====================== RESTART: C:\PYthon\function1.py ======================
TOTAL= 30
TOTAL= 3

====================== RESTART: C:\PYthon\function1.py ======================
TOTAL= 30
TOTAL= 3
TOTAL= 6

====================== RESTART: C:\PYthon\function1.py ======================
1
1
2
2
2
2
1,2
(1, 2)


====================== RESTART: C:\PYthon\function1.py ======================
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 30, in <module>
    add(a,b)
NameError: name 'a' is not defined

====================== RESTART: C:\PYthon\function1.py ======================

====================== RESTART: C:\PYthon\function1.py ======================

====================== RESTART: C:\PYthon\function1.py ======================
total 15

====================== RESTART: C:\PYthon\function1.py ======================
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 31, in <module>
    add( )
TypeError: add() missing 2 required positional arguments: 'a' and 'b'

====================== RESTART: C:\PYthon\function1.py ======================

====================== RESTART: C:\PYthon\function1.py ======================
total 11

====================== RESTART: C:\PYthon\function1.py ======================
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 31, in <module>
    add(5,6)
  File "C:\PYthon\function1.py", line 29, in add
    print("total====",add(a,b))
  File "C:\PYthon\function1.py", line 29, in add
    print("total====",add(a,b))
  File "C:\PYthon\function1.py", line 29, in add
    print("total====",add(a,b))
  [Previous line repeated 1021 more times]
  File "C:\PYthon\function1.py", line 25, in add
    if a>=0 and b>=0:
RecursionError: maximum recursion depth exceeded in comparison

====================== RESTART: C:\PYthon\function1.py ======================
total==== 11

====================== RESTART: C:\PYthon\function1.py ======================
11

====================== RESTART: C:\PYthon\function1.py ======================
30
0
1

====================== RESTART: C:\PYthon\function1.py ======================
3

====================== RESTART: C:\PYthon\function1.py ======================
wrong value

====================== RESTART: C:\PYthon\function1.py ======================
3

====================== RESTART: C:\PYthon\function1.py ======================
30

====================== RESTART: C:\PYthon\function1.py ======================
30
wrong value

====================== RESTART: C:\PYthon\function1.py ======================
(1, 2, 3)
(1, 2)

====================== RESTART: C:\PYthon\function1.py ======================
(1, 2, 3)
<class 'tuple'>
(1, 2)
<class 'tuple'>

====================== RESTART: C:\PYthon\function1.py ======================
(1, 2, 3)
<class 'tuple'>
(1, 2)
<class 'tuple'>
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

====================== RESTART: C:\PYthon\function1.py ======================
(1, 2, 3)
<class 'tuple'>
(1, 2)
<class 'tuple'>
<class 'list'>
a=(1, 2, 3)
new=list(a)
new
[1, 2, 3]
type(new)
<class 'list'>
dir(new)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
sum(a)
6
sum(new)
6

====================== RESTART: C:\PYthon\function1.py ======================

====================== RESTART: C:\PYthon\function1.py ======================

====================== RESTART: C:\PYthon\function1.py ======================
(10,)
()
(1,)

====================== RESTART: C:\PYthon\function1.py ======================
(10, 34, 34)
()
(1, 4)

====================== RESTART: C:\PYthon\function1.py ======================
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 63, in <module>
    add(10,34,34)
  File "C:\PYthon\function1.py", line 55, in add
    print(add(a))
  File "C:\PYthon\function1.py", line 55, in add
    print(add(a))
  File "C:\PYthon\function1.py", line 55, in add
    print(add(a))
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded

====================== RESTART: C:\PYthon\function1.py ======================
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 64, in <module>
    add(10,34,34)
  File "C:\PYthon\function1.py", line 61, in add
    print(add(a))
  File "C:\PYthon\function1.py", line 61, in add
    print(add(a))
  File "C:\PYthon\function1.py", line 61, in add
    print(add(a))
  [Previous line repeated 1022 more times]
RecursionError: maximum recursion depth exceeded

====================== RESTART: C:\PYthon\function1.py ======================
Traceback (most recent call last):
  File "C:\PYthon\function1.py", line 63, in <module>
    print(add(a))
NameError: name 'a' is not defined

====================== RESTART: C:\PYthon\function1.py ======================
0

====================== RESTART: C:\PYthon\function1.py ======================
0
78
5
t=(1,2,3,4,5,6,7,89,9)
sum(t)
126
min(t)
1
max(t)
89
mean(t)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mean(t)
NameError: name 'mean' is not defined
avg(t)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    avg(t)
NameError: name 'avg' is not defined
dir(t)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
class(t)
SyntaxError: invalid syntax
count(t)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    count(t)
NameError: name 'count' is not defined. Did you mean: 'round'?
t.count(t)
0
t=(1,2,3,4,5,6,7,89,9)
t=(1,2,3,4,5,6,7,89,a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t=(1,2,3,4,5,6,7,89,a)
NameError: name 'a' is not defined
>>> t=(1,2,3,4,5,6,7,89,'a')
>>> mean(t)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    mean(t)
NameError: name 'mean' is not defined
>>> max(t)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> sum(t)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sum(t)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> t.count(5)
1
>>> len(t)
9
>>> t.count('a')
1
>>> dir(t)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t=[1,2,3,4,5,6,7,89,a]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t=[1,2,3,4,5,6,7,89,a]
NameError: name 'a' is not defined
>>> t=[1,2,3,4,5,6,7,89,'a']
>>> type(t)
<class 'list'>
