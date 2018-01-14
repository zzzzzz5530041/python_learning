# -*- coding:UTF-8 -*-
def addAll(list):
    result = 0;
    for i in list:
        result = i + result;
        print(result)


list = [1, 2, 3, 4]
addAll(list);


def printAll(l):
    for i in l:
        print(i)


l = (1, 2, 3, 4)
printAll(l);


# a function with default param
def Cube(x=2):
    return x ** 3;


print(Cube())  # Cube() ,didnt pass params, since param default value is 2..print 8
print(Cube(3))  # Cube(3), param is 3..print 27


def Cube(x=1, y=2, z=3):
    return (x + y - z) ** 3;


print(Cube())
print(Cube(0))  # set x=0
print(Cube(0, 3))  # set x=0,y=3
print(Cube(0, 3, 5))  # set x=0,y=3,z=5
print(Cube(z=7))  # set x=0,y=3,z=5


# 可变长参数,使用可变长参数时,所有参数都保存在一个元组,参数前加*表示该参数时可变长参数
def mylistappend(*list):
    l = [];
    for i in list:
        l.extend(i);
    return l;


a = [1, 2, 3, 4];
b = [5, 6, 7, 8];
print(mylistappend(a, b));


# 用参数返回计算结果
def changeVal(x):
    x[0] = x[0] ** 2;


a = [2];
changeVal(a);
print(a);


# 变量作用域 全局变量
def fun(x):
    global a;
    return a + x;


a = 2;
print(fun(3))

# lambda lambda 参数:表达式
myfun = lambda x: x + 3;
myfun(3)


# lambda也可调用其他函数
def show(n):
    print('lambda' * n);


f = lambda x: show(x);
f(3)

# moduel import
# 支持import 和 from
# import math
# from math import sin ...引入math的sin函数或变量

from math import sin;

print(sin(30));
import math;

print(math.tan(45));

'''
import mymoduel;
mymoduel.show();
print(mymoduel.myname)
'''
from mymoduel import show;
from mymoduel import myname;

show();
print(myname)

import os;
import sys;

modulePath = os.getcwd() + "/module";  # /Users/zhuyang/projects/python_learning/hello_world/module
sys.path.append(modulePath);
import mymoduel;

mymoduel.show();
print(mymoduel.myname)
mymoduel.myname = 'zhuyang'
print(mymoduel.myname)

print(dir())
