#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     7-5-字符串转换
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

str = "mutiantong"
print(str)

# join操作
str1 = "".join(str)
print(str1)

# 格式化字典
s = "%(n)d %(x)s" % {"n": 1, "x": "mutiantong"}
print(s)
