#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     13-3-zip and map
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# zip 构建 两个list 对应的元祖
L1 = [1, 2, 3, 4, 5]
L2 = [5, 6, 7, 8, 9]
L3 = zip(L1, L2)
print(list(L3))

# 创建字典
D = dict(zip(L1, L2))
print(D)

# enumerate
print("#" * 30)
S = 'spam'
for (offset, item) in enumerate(S):
    print(offset, item)
