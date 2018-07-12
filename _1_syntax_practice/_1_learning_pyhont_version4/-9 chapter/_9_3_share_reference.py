#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     9-3-共享引用
   Description :
   Author :      'Sam Yong'
   date：          2018/7/6
-------------------------------------------------
   Change Activity:
                   2018/7/6:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 理解共享引用
L = [1, 2, 3]
M = ['X', L, 'Y']
print(M)
print("*" * 30)
L[1] = 'haha'
print(M)

# 重复多次
L = [1, 2, 3]
X = L * 4
print(X)   # X 并没与L 共享引用
Y = [L] * 4
print(Y)   # Y 与L 共享引用


# 不可变类型不可以在原处修改
T = (1, 2, 3)
T = T[:2] + (4,)
print(T)