#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11-1-序列
   Description :
   Author :      'Sam Yong'
   date：          2018/7/6
-------------------------------------------------
   Change Activity:
                   2018/7/6:
-------------------------------------------------
"""
__author__ = 'Sam Yong'
A, B = [1, 2]
print(A, B)

[C, D] = [A, B]
print(C, D)

# *通配符，赋值结果是一个[]
# 出现在边界也是一个[]， 或者是一个空[]
L = [1, 2, 3, 4]
a, *b, c = L
print(a, b, c)

# extend 要比 + 更快
# + 新创建一个， extend是原地扩展

L1 = [5, 6, 7, 8]


# print = sys.stdout.write()
import sys
sys.stdout = open('log.txt', 'a+') #这样做好之后，print就会打到文件里