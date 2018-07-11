#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     18-2-参数传递
   Description :
   Author :      'Sam Yong'
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

def f(a, b, c):
    print(a, b, c)

f(1, 2, 3) # 通过位置调用
f(a=1, c=3, b=2) # 通过关键字参数调用
# f(6, a=1, c=3)  # 先位置后关键字 ， 产生了歧义


## 默认参数在关键字参数后面

#### 任意参数

#1 def 函数定义的时候里有*
def f(*arg):
    print(arg)

f(1)
f(1, 2, 3, 4)


#2 def 函数定义的时候里有**
print('*' * 20)
def f(**arg):
    print(arg)

f(a=1, b= 2)  # ** 里面是字典参数
f(c=3)

# 一般 *pargs在前， **kargs在后

