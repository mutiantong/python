#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20-1-comprehension-1
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 求字符串的 Ascii
val = map(ord, 'abcdefg')
print(list(val))

val = [ord(x) for x in 'abcedfg']
print(val)

#  列表解析，多重循环
var = [(x, y)for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0 for y in[1, 2, 3, 4, 5, 6] if y % 2 == 1]
print(var)
