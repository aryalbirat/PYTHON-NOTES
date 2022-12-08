Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import Counter
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"

print("Sentence is: ",sentence)
Sentence is:  the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat
print(dict(counter(semtence)))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(dict(counter(semtence)))
NameError: name 'counter' is not defined. Did you mean: 'Counter'?
print(dict(counter(sentence)))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(dict(counter(sentence)))
NameError: name 'counter' is not defined. Did you mean: 'Counter'?
print(dict(Counter(sentence)))
{'t': 18, 'h': 9, 'e': 8, ' ': 26, 'c': 3, 'a': 15, 's': 2, 'o': 2, 'n': 6, 'm': 3, 'w': 4, 'i': 4, 'r': 4, 'd': 2, 'p': 3, 'l': 1, 'y': 2, 'g': 1}
count=Counter(sentence)
print("OCCURENCES OF CAT::",counts['cat']

 print("OCCURENCES OF CAT::",count['cat']
       
SyntaxError: '(' was never closed
print("OCCURENCES OF CAT::",counts['cat'])
       
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("OCCURENCES OF CAT::",counts['cat'])
NameError: name 'counts' is not defined. Did you mean: 'count'?
print("OCCURENCES OF CAT::",count['cat'])
       
OCCURENCES OF CAT:: 0
#
       



#DATE AND TIME
       
from datetime import datetime
       
import time
help(time.ctime())
No Python documentation found for 'Tue Dec  6 08:12:50 2022'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

dir(datetime)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
datetime.today()
datetime.datetime(2022, 12, 6, 8, 14, 40, 974523)
print(datetime.today())
2022-12-06 08:15:01.061325
datetime.astimezone()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    datetime.astimezone()
TypeError: unbound method datetime.astimezone() needs an argument
datetime.minute()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    datetime.minute()
TypeError: 'getset_descriptor' object is not callable
datetime.now()
datetime.datetime(2022, 12, 6, 8, 16, 14, 678707)
print(datetime.now())
2022-12-06 08:16:31.454039
import os
import sys
print(sys.version)
3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]
print(os.sep)
\
print(os.sep)
\
dir(os)
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
print(os.path)
<module 'ntpath' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ntpath.py'>
print(sys.path)
['', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
sys.exit(1)

========================== RESTART: C:/VENOM/7.2.py =========================
Match 1 was found at 4-7: cat
Match 2 was found at 8-11: sat
Match 3 was found at 19-22: mat

========================== RESTART: C:/VENOM/7.2.py =========================
Match 1 was found at 4-7: cat
Match 2 was found at 8-11: sat
Match 3 was found at 19-22: mat
Match 1 was found at 0-4: 2022
Group 1 found at 0-4: 2022

========================== RESTART: C:/VENOM/7.2.py =========================
Match 1 was found at 0-4: 2022
Group 1 found at 0-4: 2022

========================== RESTART: C:/VENOM/7.2.py =========================
Match 1 was found at 30-39: language.
Group 1 found at 30-38: language


squares = []
for num in range(10):
    squares.append(num**2)
print("Squares :",squares)
SyntaxError: invalid syntax
    print("Squares :",squares)
    
SyntaxError: unexpected indent
print("Squares :",squares)
Squares : []


squares=[]
for num in range(10)
SyntaxError: incomplete input
squares=[]
for num in range(10):
    
SyntaxError: multiple statements found while compiling a single statement
squares=[]
for num in range(10):
    squares.append(num**2)
    print("Squares :",squares)

    
Squares : [0]
Squares : [0, 1]
Squares : [0, 1, 4]
Squares : [0, 1, 4, 9]
Squares : [0, 1, 4, 9, 16]
Squares : [0, 1, 4, 9, 16, 25]
Squares : [0, 1, 4, 9, 16, 25, 36]
Squares : [0, 1, 4, 9, 16, 25, 36, 49]
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64]
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


squares=[]
for num in range(10):
    squares.append(num**2)
print("Squares :",squares)
SyntaxError: multiple statements found while compiling a single statement




squares=[]
or num in range(10):
    
SyntaxError: invalid syntax




squares=[]
for num in range(10):
    squares.append(num**2)
    print("Squares :",squares)

    
Squares : [0]
Squares : [0, 1]
Squares : [0, 1, 4]
Squares : [0, 1, 4, 9]
Squares : [0, 1, 4, 9, 16]
Squares : [0, 1, 4, 9, 16, 25]
Squares : [0, 1, 4, 9, 16, 25, 36]
Squares : [0, 1, 4, 9, 16, 25, 36, 49]
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64]
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares=[]
for num in range(10):
    squares.append(num**2)

    

print("Squares :",squares)
Squares : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


even_comp = [x for x in range(20) if x % 2 == 0]

print(even_comp)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
cube_squares = [x**2 if x % 2 == 0 else x**3 for x in range(10)]
print(cube_squares)
[0, 1, 4, 27, 16, 125, 36, 343, 64, 729]



l=list(range(1,100,4))
for key,value in enumerate(l):
    print(key," :: ",value)

    
0  ::  1
1  ::  5
2  ::  9
3  ::  13
4  ::  17
5  ::  21
6  ::  25
7  ::  29
8  ::  33
9  ::  37
10  ::  41
11  ::  45
12  ::  49
13  ::  53
14  ::  57
15  ::  61
16  ::  65
17  ::  69
18  ::  73
19  ::  77
20  ::  81
21  ::  85
22  ::  89
23  ::  93
24  ::  97
>>> 
>>> 
>>> print("\nDict CUBES : ",{x: x**3 for x in range(10)})

Dict CUBES :  {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> print("Dict CUBES EVEN: ",{x: x**3 for x in range(10) if x**3 % 2 == 0})
Dict CUBES EVEN:  {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
>>> 
>>> 
>>> 
>>> i = (str(i) for i in range(10))
>>> print(list(i))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print([str(i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> 
>>> 
>>> 
>>> print([i for i in range(10)])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
