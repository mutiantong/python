#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     13-1-while-else
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

a = 20
while a < 10:
    if a < 5:
        break
    print("this is if ", a)
    a = a - 1
else:
    print('this is while ', a)

# 不需要标志位的情况
# 20内是否存在15
print('*' * 20)
bFound = False
x = 20
while x <= 20:
    if x == 15:
        bFound = True
        break
    x -= 1

if bFound == True:
    print('found!111111111')
else:
    print('not found111111')

print('*' * 20)
x = 20
while x <= 20:
    if x == 15:
        print('found!222222')
        break
    x -= 1
else:
    print('not found!22222')   # 有break 就不会执行else
