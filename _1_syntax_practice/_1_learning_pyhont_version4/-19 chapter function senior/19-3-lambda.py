#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19-3-lambda
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# lambda 是表达式, 不是类似def 的一些语句？
# lambda 是 生成一个函数， def 是将生成的函数赋值一个变量

f = lambda x: x*5
val = f(5)
print(val)

print('*' * 20)
# 为什么用lambda
# 回调处理器
# 编写跳转表（jump table）
# lambda 行内零时函数

# example:
L = [lambda x: x * 2,
     lambda x: x * 3,
     lambda x: x * 4, ]
for func in L:
    print(func(2))

# 如果用def
print('*' * 20)
def f1(x):
    return x * 2

def f2(x):
    return x * 3

def f3(x):
    return x * 4

L1 = [f1, f2, f3]
for func in L1:
    print(func(2))

#
print('*' * 20)
lower = lambda x, y: x if x < y else y
val = lower('ab', 'cc')
print(val)


