#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     4-6-其他类型
   Description :
   Author :      'Sam Yong'
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

from decimal import Decimal

value = 1 / 3
print('value = %s' % (value))


print(Decimal(value).quantize(Decimal('1.000'))) # 十进制的操作的方法


# 破坏代码灵活性
L = [1, 2, 3, ]
print(L)
print(type(L))

# 三种方法来验证是否是对象类型，妨碍了代码的灵活性
print(type(L) == list)
print(type(L) == type([]))
print(isinstance(L, list))

