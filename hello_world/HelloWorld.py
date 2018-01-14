# -*- coding:UTF-8 -*-
print('hello');
a = -1;
b = -2;
if a > b:
    print(a)  # if a larger than b ,then print a
else:
    print(b);
# if statement
if a > b:
    if a == 1:
        print(a)
    else:
        if a == 0:
            print(a)
        else:
            pass
elif a == b:
    print(a, b);
else:
    print(b)

# comment. use ''' or """ to comment
'''
if a>b:
    if a==1:
        print(a)
    else:
        if a==0:
            print(a)
        else:
            pass
elif a==b:
    print(a,b);
else:
    print(b)
'''

"""
if a>b:
    if a==1:
        print(a)
    else:
        if a==0:
            print(a)
        else:
            pass
elif a==b:
    print(a,b);
else:
    print(b)
"""

# use " '
a = "what's ur name?";
b = 'i say : "what is your name?"';
print(a, b);

# use \ to wrap
x = 1;
y = 2;
# below equals to z = x*2+y*3
z = x * 2 \
    + y \
      * 3;
print(z);

# input function
# name = input('Input ur name here:');
# print(name)

# print
arr = [1, 2, 3]
print(arr)
arrStr = ['a', 'b']
print(arrStr)
# loop
for i in arrStr:
    print(i)

print(" 你好,支持中文")

# encode string
str = '''
在python中使用中文
需要注意编码问题,可以使用的字符编码有:
UTF-8,CP936,GB2312,ISO-8859-1
''';
print(str)
# simple caculation
print(3 * 5 / 2)
print(2 ** 4);  # equals to 2*2*2*2

# math module
# import math module
import math

print(math.sin(30))
print(math.tan(1))
# big integer suport
print(99 ** 999)
