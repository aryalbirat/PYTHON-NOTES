Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
10//2
5
10/5
2.0
67/8
8.375
67/8
8.375
67//8
8
8/4
2.0
8//4
2
64/8
8.0
65//8
8
65/8
8.125
9//2
4
9/2
4.5
5**8
390625
4**2
16
7**2
49
6**2
36
name="Python Programming"
name
'Python Programming'
type(name)
<class 'str'>
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
count(name)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    count(name)
NameError: name 'count' is not defined. Did you mean: 'round'?
round(name)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    round(name)
TypeError: type str doesn't define __round__ method
name.count
<built-in method count of str object at 0x00000163F7A738C0>
name.count()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name.count()
TypeError: count() takes at least 1 argument (0 given)
name.count(name)
1
\
name.count(P)
Traceback (most recent call last):\
  File "<pyshell#25>", line 1, in <module>
    name.count(P)
NameError: name 'P' is not defined
name="Python Programming"
name.count("P")
2
name.count(" ")
1
name.count("m")
2
name.count("y")
1
name.count("i")
1
name.count("o")
2
name.count("k")
0
name.count("p")
0
name.count("on")
1
name.count("Programming")
1
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(name.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

help(name.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

name.upper()
'PYTHON PROGRAMMING'
name.lower()
'python programming'
AGE=19
age=19
help(age)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      
 |      Also known as the population count.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder='big', *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.  Default is to use 'big'.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

age=19
\
type(age)
<class 'int'>
dir(age)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
age.imag()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    age.imag()
TypeError: 'int' object is not callable
name="Python Programming"
len(name)
18
name[0]
'P'
name[5]
'n'
name[6]
' '
name[-6]
'a'
name[-1]
'g'
name[-3]
'i'
name[-20]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    name[-20]
IndexError: string index out of range
name[-1]
'g'
name[-18]
'P'
name[0:2]
'Py'
name[0:1]
'P'
name="Python Programming"
name[0:2]
'Py'
name[0:1]
'P'
name[0:3]
'Pyt'
name[7:13]
'Progra'
name[8:14]
'rogram'
name[8:12]
'rogr'
name[-7:-11]
''
name[-11:-7]
'Prog'
\
name[8:12]
'rogr'
name[-7]
'r'
name[-12]
' '
name[-11]
'P'
name[-10]
'r'
name[-7:-10]
''
name[-7:-11]
''
name[-11:-7]
'Prog'
name[-10:-7]
'rog'
name[-10:-6]
'rogr'
name[-10:-6]
'rogr'
name[8:12]
'rogr'
name[5:]
'n Programming'
name="Python Programming"
name[-1:]
'g'
name[:-1]
'Python Programmin'
name[0:2:10]
'P'
name[0:3:10]
'P'
name[1:2:10]
'y'
name[4:2:10]
''
\
name[3:2:18]
''
name[5:2:18]
''
name[0:18:2]
'Pto rgamn'
name[0::2]
'Pto rgamn'
name[0:18:3]
'Ph oai'
name[0::3]
'Ph oai'
name[0::4]
'Poran'
name[0:18:7]
'PPm'
name[0::5]
'Pngi'
name[1::5]
'y rn'
name[0:10:2]
'Pto r'
name="Python Programming"
name[0:10:2]
'Pto r'
name[0]
'P'
name[10]
'g'
name[0]
'P'
name[2]
't'
name[4]
'o'
name[6]
' '
name[8]
'r'
name[0::]
'Python Programming'
name[0:]
'Python Programming'
name[-1::]
'g'
name[-13::]
'n Programming'
name[-18::]
'Python Programming'
\
name[-18::2]
'Pto rgamn'
name[-18:0:2]
''
name[-18:-1:2]
'Pto rgamn'
name[-1:-18:-2]
'gimroPnhy'
name[-1::-1]
'gnimmargorP nohtyP'
name[-1:-18:-1]
'gnimmargorP nohty'
name[::-1]
'gnimmargorP nohtyP'
name[:-1]
'Python Programmin'
name[::]
'Python Programming'
name[::-1]
'gnimmargorP nohtyP'
name[::-2]
'gimroPnhy'
name[::]
'Python Programming'
name[:-1]
'Python Programmin'
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
name="SCHOOL"
len(name)
6
name="Python Programming"
yes=True
type(yes)
<class 'bool'>
print(yes)
True
\
no=false
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    no=false
NameError: name 'false' is not defined. Did you mean: 'False'?
no=False
type(no)
<class 'bool'>
'P'in name
True
'P'not in name
False
"Prog" in name
True
"ppp" in not name
SyntaxError: invalid syntax
"ppp" not in name
True
if'P' in name
SyntaxError: expected ':'
"Python"is in name
SyntaxError: invalid syntax
'P'not in name
False
'P' not in name
False
'n' not in name
False
'n' in name
True
'a' in name
True
>>> x not in name
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    x not in name
NameError: name 'x' is not defined
>>> 'x'not in name
True
>>> 'P' is name
False
>>> "Python Programming" is name
False
>>> name="Python Programming"
>>> "Python Programming"is name
False
>>> 'Python Programming'is name
False
>>> "Python Programming"is name
False
>>> "Python Programming" is name
False
>>> name is "Python Programming"
False
>>> name="Python Programming"
>>> name is "Python Programming"
False
>>> name in "Python Programming"
True
>>> namee="PYTHON"
>>> nam="PYTHON"
>>> namee is nam
True
>>> a="abcd abcd"
>>> b="abcd abcd"
>>> a is b
False
>>> a in b
True
>>> a is not b
True
