#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19-1-递归
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

def mysum(L):
    first, *rest = L  # 这里面用了函数的解释参数的语法，简洁
    return first if not rest else first + mysum(rest)

val = mysum([1, 2, 3, 4, 5])
print(val)

# 嵌套递归
def sumtree(L):
    sum = 0
    for x in L:
        if isinstance(x, list):
            sum += sumtree(x)
        else:
            sum += x
    return sum

L = [1, 2, [3, [4, 5, 6]], [7, [8, 9], 10]]
val = sumtree(L)
print(val)