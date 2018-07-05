#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-1-基本操作
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

L = ['ni']
print(L)
L2 = L * 4
print(L2)

L.append("haha")      # append会修改原始的list, 而 + 会新生成一个list
L1 = L + ["haHHH"]
print(L)
print(L1)

# sort 排序
print("*"*124)
L = ['abc', 'efg', 'acd', 'ABC']
print(L)
L.sort()
print(L)
L.sort(key=str.lower)
print(L)
L.sort(reverse=True)
print(L)