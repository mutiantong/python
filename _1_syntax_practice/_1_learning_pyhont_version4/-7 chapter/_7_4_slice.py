#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     7-4-切片
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

str = "abcdefg"
print(str)

str1 = str[::-1] # 实际是翻转
print(str1)

str2 = str[::2] # 步进长度
print(str2)

line = "12 34 56 79\n"
print(line)

line1 = line.rstrip() # 去除换行符
print(line1)
print(line)