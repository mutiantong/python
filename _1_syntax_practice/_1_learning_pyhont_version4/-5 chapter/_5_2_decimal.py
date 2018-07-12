#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     5-2-decimal
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'
# 设置精度 从实验结果来看不对？python3 的问题？
import decimal
decimal.getcontext().prec = 4 # 设置精度为4
vale = decimal.Decimal(3.333333)
print(vale)

# 分数
from fractions import Fraction
y = Fraction(4,6)
print(y)