#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     7-6-string替换
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'
str = "{0}, {1}, {2}".format('mu', "tian", "tong")
print(str)

str1 = "{food}, {type}".format(food="hahaha", type="new")
print(str1)

# next
print("-" * 128)
## 高级用法1
import sys

str1 = 'My {1[spam]} runs on {0.platform}'.format(sys, {'spam': "laptop"})
# 这里面0，代表是元组里面的sys, 1代表的就是字典
print(str1)

print("-" * 128)
str1 = 'My {config[spam]} runs on {0.platform}'.format(sys, config={'spam': "laptop"})
print(str1)

print("#"*20)
print("-" * 128)
str = '{0:.2f}'.format(1/3)
print(str)