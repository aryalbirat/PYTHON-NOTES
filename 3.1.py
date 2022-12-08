Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
if (a==10 and (a<=8))
SyntaxError: incomplete input
if (a==5):
    print("yes")
elif (a<5):
    print("a is less than 5")
else:
    print("a is greater than 5")

yes
a=4
if (a==5):
    print("yes")
elif (a<5):
    print("a is less than 5")
else:
    print("a is greater than 5")

    
a is less than 5
name="PYTHON"
'T'in name
True
for 'O' in name
SyntaxError: cannot assign to literal
for 'O' in name:
    
SyntaxError: cannot assign to literal
name="PYTHON"
'T'in name
True
for char in name:
    print(char)

    
P
Y
T
H
O
N
#for each character
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for k in range(10):
    print(k)

    
0
1
2
3
4
5
6
7
8
9
for k in range(10,100):
    if k>25:
        print(k+25)
    if k==50:
        print("fifty")
    if k==50:
        print("eighty")

        
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
fifty
eighty
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
for k in range(10,100):
    if k>25:
        print(k+"25")
    if k==50:
        print("fifty")
    if k==50:
        print("eighty")

        
Traceback (most recent call last):
  File "<pyshell#33>", line 3, in <module>
    print(k+"25")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for k in range(10,100):
    if k>25:
        print(str(i)+"25")
    if k==50:
        print("fifty")
    if k==50:
        print("eighty")

        
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
fifty
eighty
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
925
for k in range(10,100):
    if k>25:
        print(str(k)+"25")
    if k==50:
        print("fifty")
    if k==50:
        print("eighty")

        
2625
2725
2825
2925
3025
3125
3225
3325
3425
3525
3625
3725
3825
3925
4025
4125
4225
4325
4425
4525
4625
4725
4825
4925
5025
fifty
eighty
5125
5225
5325
5425
5525
5625
5725
5825
5925
6025
6125
6225
6325
6425
6525
6625
6725
6825
6925
7025
7125
7225
7325
7425
7525
7625
7725
7825
7925
8025
8125
8225
8325
8425
8525
8625
8725
8825
8925
9025
9125
9225
9325
9425
9525
9625
9725
9825
9925
for k in range(10,100):
    if k>25:
        print(str(k)+"25")
    if k==50:
        print("fifty")
    if k==80:
        print("eighty")

        
2625
2725
2825
2925
3025
3125
3225
3325
3425
3525
3625
3725
3825
3925
4025
4125
4225
4325
4425
4525
4625
4725
4825
4925
5025
fifty
5125
5225
5325
5425
5525
5625
5725
5825
5925
6025
6125
6225
6325
6425
6525
6625
6725
6825
6925
7025
7125
7225
7325
7425
7525
7625
7725
7825
7925
8025
eighty
8125
8225
8325
8425
8525
8625
8725
8825
8925
9025
9125
9225
9325
9425
9525
9625
9725
9825
9925
for k in range(10,100):
    if k>25:
        print(str(k)+"25")
    if k==50:
        print("fifty")
    if k==80:
    if k<=90:
        
SyntaxError: expected an indented block after 'if' statement on line 6
for k in range(10,100):
    if k>25:
        print(str(k)+"25")
    if k==50:
        print("fifty")
    if k==80:
        if k<=90:
            print(i)

            
2625
2725
2825
2925
3025
3125
3225
3325
3425
3525
3625
3725
3825
3925
4025
4125
4225
4325
4425
4525
4625
4725
4825
4925
5025
fifty
5125
5225
5325
5425
5525
5625
5725
5825
5925
6025
6125
6225
6325
6425
6525
6625
6725
6825
6925
7025
7125
7225
7325
7425
7525
7625
7725
7825
7925
8025
9
8125
8225
8325
8425
8525
8625
8725
8825
8925
9025
9125
9225
9325
9425
9525
9625
9725
9825
9925
for k in range(10,100):
    if k>25:
        print(str(k)+"----25")
    if k==50:
        print("fifty")
    if k==80:
        if k<=90:
            print(i)

            
26----25
27----25
28----25
29----25
30----25
31----25
32----25
33----25
34----25
35----25
36----25
37----25
38----25
39----25
40----25
41----25
42----25
43----25
44----25
45----25
46----25
47----25
48----25
49----25
50----25
fifty
51----25
52----25
53----25
54----25
55----25
56----25
57----25
58----25
59----25
60----25
61----25
62----25
63----25
64----25
65----25
66----25
67----25
68----25
69----25
70----25
71----25
72----25
73----25
74----25
75----25
76----25
77----25
78----25
79----25
80----25
9
81----25
82----25
83----25
84----25
85----25
86----25
87----25
88----25
89----25
90----25
91----25
92----25
93----25
94----25
95----25
96----25
97----25
98----25
99----25
for k in range(10,100):
    if k>25:
        print(str(k)+"----25")
    if k==50:
        print("fifty")
    if k==80:
        if k<=90:
            print(k)

            
26----25
27----25
28----25
29----25
30----25
31----25
32----25
33----25
34----25
35----25
36----25
37----25
38----25
39----25
40----25
41----25
42----25
43----25
44----25
45----25
46----25
47----25
48----25
49----25
50----25
fifty
51----25
52----25
53----25
54----25
55----25
56----25
57----25
58----25
59----25
60----25
61----25
62----25
63----25
64----25
65----25
66----25
67----25
68----25
69----25
70----25
71----25
72----25
73----25
74----25
75----25
76----25
77----25
78----25
79----25
80----25
80
81----25
82----25
83----25
84----25
85----25
86----25
87----25
88----25
89----25
90----25
91----25
92----25
93----25
94----25
95----25
96----25
97----25
98----25
99----25
for k in range(10,100):
    if k>25:
        print(str(k)+"----25")
    if k==50:
        print("fifty")
    if k>=80:
        if k<=90:
            print(k)

            
26----25
27----25
28----25
29----25
30----25
31----25
32----25
33----25
34----25
35----25
36----25
37----25
38----25
39----25
40----25
41----25
42----25
43----25
44----25
45----25
46----25
47----25
48----25
49----25
50----25
fifty
51----25
52----25
53----25
54----25
55----25
56----25
57----25
58----25
59----25
60----25
61----25
62----25
63----25
64----25
65----25
66----25
67----25
68----25
69----25
70----25
71----25
72----25
73----25
74----25
75----25
76----25
77----25
78----25
79----25
80----25
80
81----25
81
82----25
82
83----25
83
84----25
84
85----25
85
86----25
86
87----25
87
88----25
88
89----25
89
90----25
90
91----25
92----25
93----25
94----25
95----25
96----25
97----25
98----25
99----25
for(i) in the range(10,100)
SyntaxError: invalid syntax
for(i)in the range(10):
    
SyntaxError: invalid syntax
for i in the range(10):
    
SyntaxError: invalid syntax
for i in range(10):
    if(i%2==0)
    
SyntaxError: incomplete input
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in the range(i);
        
SyntaxError: invalid syntax
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in the range(i):
            
SyntaxError: invalid syntax
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)

            
**
0
**
2
++
0
++
1
**
4
++
0
++
1
++
2
++
3
**
6
++
0
++
1
++
2
++
3
++
4
++
5
**
8
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)

        
**
0
**
2
**
4
**
6
**
8
for x in range(i):
            print("++")
            print(x)

            
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
++
8
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)

**
0
**
2
++
0
++
1
**
4
++
0
++
1
++
2
++
3
**
6
++
0
++
1
++
2
++
3
++
4
++
5
**
8
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)
        else
        
SyntaxError: incomplete input
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)
        else:
            print("fail)
                  
SyntaxError: incomplete input

for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)
        else:
            print("fail++++++"+str(i))

            
**
0
fail++++++0
**
2
++
0
++
1
fail++++++2
**
4
++
0
++
1
++
2
++
3
fail++++++4
**
6
++
0
++
1
++
2
++
3
++
4
++
5
fail++++++6
**
8
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
fail++++++8
for x in range(i):
            print("++")
            print(x)
        else:
            print("fail++++++"+str(i))

SyntaxError: unindent does not match any outer indentation level
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)
        else:
            print("fail++++++",i)

            
**
0
fail++++++ 0
**
2
++
0
++
1
fail++++++ 2
**
4
++
0
++
1
++
2
++
3
fail++++++ 4
**
6
++
0
++
1
++
2
++
3
++
4
++
5
fail++++++ 6
**
8
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
fail++++++ 8
for i in range(10):
    if(i%2==0):
        print("**")
        print(i)
        for x in range(i):
            print("++")
            print(x)
    else:
         print("fail++++++",i)

         
**
0
fail++++++ 1
**
2
++
0
++
1
fail++++++ 3
**
4
++
0
++
1
++
2
++
3
fail++++++ 5
**
6
++
0
++
1
++
2
++
3
++
4
++
5
fail++++++ 7
**
8
++
0
++
1
++
2
++
3
++
4
++
5
++
6
++
7
fail++++++ 9
for num in range(1,101):
    if(a%2==0):
        print("even------"+str(num))
    else:
        print("odd------"+str(num))

        
even------1
even------2
even------3
even------4
even------5
even------6
even------7
even------8
even------9
even------10
even------11
even------12
even------13
even------14
even------15
even------16
even------17
even------18
even------19
even------20
even------21
even------22
even------23
even------24
even------25
even------26
even------27
even------28
even------29
even------30
even------31
even------32
even------33
even------34
even------35
even------36
even------37
even------38
even------39
even------40
even------41
even------42
even------43
even------44
even------45
even------46
even------47
even------48
even------49
even------50
even------51
even------52
even------53
even------54
even------55
even------56
even------57
even------58
even------59
even------60
even------61
even------62
even------63
even------64
even------65
even------66
even------67
even------68
even------69
even------70
even------71
even------72
even------73
even------74
even------75
even------76
even------77
even------78
even------79
even------80
even------81
even------82
even------83
even------84
even------85
even------86
even------87
even------88
even------89
even------90
even------91
even------92
even------93
even------94
even------95
even------96
even------97
even------98
even------99
even------100
for num in range(1,101):
    if(num%2==0):
        print("even------"+str(num))
    else:
        print("odd------"+str(num))

odd------1
even------2
odd------3
even------4
odd------5
even------6
odd------7
even------8
odd------9
even------10
odd------11
even------12
odd------13
even------14
odd------15
even------16
odd------17
even------18
odd------19
even------20
odd------21
even------22
odd------23
even------24
odd------25
even------26
odd------27
even------28
odd------29
even------30
odd------31
even------32
odd------33
even------34
odd------35
even------36
odd------37
even------38
odd------39
even------40
odd------41
even------42
odd------43
even------44
odd------45
even------46
odd------47
even------48
odd------49
even------50
odd------51
even------52
odd------53
even------54
odd------55
even------56
odd------57
even------58
odd------59
even------60
odd------61
even------62
odd------63
even------64
odd------65
even------66
odd------67
even------68
odd------69
even------70
odd------71
even------72
odd------73
even------74
odd------75
even------76
odd------77
even------78
odd------79
even------80
odd------81
even------82
odd------83
even------84
odd------85
even------86
odd------87
even------88
odd------89
even------90
odd------91
even------92
odd------93
even------94
odd------95
even------96
odd------97
even------98
odd------99
even------100
for num in range(1,101):
    if(num%2==0):
    else:
        print("odd------"+str(num))
        
SyntaxError: expected an indented block after 'if' statement on line 2
for num in range(1,101):
    if(num%2!0):
        print("odd------"+str(num))
        
SyntaxError: invalid syntax
for num in range(1,101):
    if(num%2!=0):
        print("odd------"+str(num))

        
odd------1
odd------3
odd------5
odd------7
odd------9
odd------11
odd------13
odd------15
odd------17
odd------19
odd------21
odd------23
odd------25
odd------27
odd------29
odd------31
odd------33
odd------35
odd------37
odd------39
odd------41
odd------43
odd------45
odd------47
odd------49
odd------51
odd------53
odd------55
odd------57
odd------59
odd------61
odd------63
odd------65
odd------67
odd------69
odd------71
odd------73
odd------75
odd------77
odd------79
odd------81
odd------83
odd------85
odd------87
odd------89
odd------91
odd------93
odd------95
odd------97
odd------99
for num in range(1,101):
    if(num%2!=0):
        print("odd------",num)

                  
odd------ 1
odd------ 3
odd------ 5
odd------ 7
odd------ 9
odd------ 11
odd------ 13
odd------ 15
odd------ 17
odd------ 19
odd------ 21
odd------ 23
odd------ 25
odd------ 27
odd------ 29
odd------ 31
odd------ 33
odd------ 35
odd------ 37
odd------ 39
odd------ 41
odd------ 43
odd------ 45
odd------ 47
odd------ 49
odd------ 51
odd------ 53
odd------ 55
odd------ 57
odd------ 59
odd------ 61
odd------ 63
odd------ 65
odd------ 67
odd------ 69
odd------ 71
odd------ 73
odd------ 75
odd------ 77
odd------ 79
odd------ 81
odd------ 83
odd------ 85
odd------ 87
odd------ 89
odd------ 91
odd------ 93
odd------ 95
odd------ 97
odd------ 99
for num not in range(1,101):
    if(num%2!=0):
        print("odd------",num)
        
SyntaxError: invalid syntax
't' not in "PYTHON"
True
for num in range(10):
        print(num)

        
0
1
2
3
4
5
6
7
8
9
help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
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
 |  start
 |  
 |  step
 |  
 |  stop

[range(10)]
[range(0, 10)]
print([range(10)])
[range(0, 10)]
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(0,10,2))
[0, 2, 4, 6, 8]
list(range(1,100,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
list(range(0,101,10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list(range(10,101,10))
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list(range(2,100,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
list(range(1,100,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
nums=[1,1,5,8,9,5,2,3]
for x in nums
SyntaxError: incomplete input
for x in nums:
    print(x)

    
1
1
5
8
9
5
2
3
dir(nums)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> type(nums)\
... type(nums)
SyntaxError: invalid syntax
>>> type(nums)
<class 'list'>
>>> nums
[1, 1, 5, 8, 9, 5, 2, 3]
>>> len(nums)
8
>>> count.nums(1)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    count.nums(1)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> len(nums)
8
>>> for k in nums:
...     print(k)
... 
...     
1
1
5
8
9
5
2
3
>>> nums[0]
1
>>> nums[1]
1
>>> nums[6]
2
>>> a=[1,2,3,4,5,6,7,8,9,0]
>>> a[7]
8
