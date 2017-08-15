# -*- coding: utf-8 -*-
from __future__ import unicode_literals

sum = 0

# for x in [1,2,3,4,5,6,7,8,9]:
# 	sum = sum+x
# 	print sum

#比如range(5)生成的序列是从0开始小于5的整数：
# range(5)
# print(range(6))

# sum = 0
# for x in range(101):
# 	sum = sum+x
# 	print(sum)

# sum = 0
# n = 99
# while n>0:
# 	sum += n
# 	n -= 2
# 	print sum

# birth = input('birth: ')
# birth = 111
# if birth < 2000:
# 	print '00qian'
# else:
# 	print '00hou'

#dictionary类型
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Adam'] = 67

# print 'hiwin' in d


# print abs(100)

# print cmp(1,2)

# print int(12.89)

# print unicode(100)

# #函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

# a = abs # 变量a指向abs函数
# print a(-1) # 所以也可以通过a调用abs函数


# def first_fun(x):
# 	if not isinstance(x , (int, float)):
# 		raise TypeError('bad operand type')
# 		return 'hehe'
# 	if x>=0:
# 		return x
# 	else:
# 		return -x
# first_fun(123123)



# def nop():
# 	pass#占位符

# print first_fun('A')	



import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

r = move(100,100,60,math.pi/6)
print r


def square(x , y):
     s = x**y
     return s
print square(5,3)

def power(x,n = 2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s
print power(10)

def add_end(L=None):
    if L is None:
        L = []
        L.append('End')
    return L
print add_end()
print add_end()


# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
#参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def clac(*num):
    sum = 0
    for n in num:
        sum = sum + n*n
    return sum
print clac(1,2,3)
print clac()
nums = [3,4,5];
print clac(*nums)

def person(name ,age , **kw):
    print 'name: ',name ,'age: ',age,'other: ',kw
person('hiwin',18)
person('Bob', 35, city='Beijing')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('hiwin' , 18 , **kw)

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

args = (3,4,5,6,8)
kw = {'x':909}
func(*args , **kw)

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(3)

#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
#尾递归函数，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# def new_fact(n):
#     return fact_iter(n,1)

# def fact_iter(num , product):
#     if num == 1:
#         return product
#     return fact_iter(num-1 , num*product)

# print new_fact(3)

# L = []
# n = 1
# while n<=99:
#     L.append(n)
#     n = n+2
# print L

#python 切片操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print L[0:3]
print L[:3]

K = range(100)
print K[-10:]
print K[:10:2]
print K[::10]
print K[::]

T = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print T[:3]