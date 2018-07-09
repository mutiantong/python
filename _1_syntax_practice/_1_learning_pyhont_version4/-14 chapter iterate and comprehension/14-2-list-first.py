#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     14-2-list-first
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

L = [1, 2, 3, 4, 5]
L1 = [x + 5 for x in L]
print(L1)

L2 = [(x + 5) for x in L]  # 列带解析是在解释器内部以C语言的速度运行
print(L2)

