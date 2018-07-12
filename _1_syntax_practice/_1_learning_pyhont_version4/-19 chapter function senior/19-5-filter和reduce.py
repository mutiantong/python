#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19-5-filter和reduce
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 函数式编程：对序列应用一些函数的工具

var = filter(lambda x : x > 0, [-1. -2. -3. -4. -5, 1, 2, 3, 4, 5])
print(var) # map ,filter 返回是一个迭代器
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))

# reduce 在python3.0 中
# 对list 求和
print('*' * 20)
from functools import reduce
val = reduce(lambda x ,y : x + y, [1, 2, 3, 4, 5,])  # reduce 是返回的一个值
print(val)