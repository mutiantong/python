#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19-4-map
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# map 将可迭代的对象中应用一个项
# map期待传的是一个函数

val = list(map(lambda x:x*x, [1, 2, 3,]))
print(val)

def pow(x, y):
    return x * y


val = list(map(pow, [1, 2, 3], [4, 5, 6]))
print(val)