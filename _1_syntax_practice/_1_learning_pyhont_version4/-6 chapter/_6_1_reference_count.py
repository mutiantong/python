#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     6-1-引用计数
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

a = 1
a = [1, 2, 4]  # 执行到这一句， 1的引用计数为0， 对象回收
a = 'list'     # 执行到这一句，list的引用计数为0， 对象回收

# 在python中
a = 2
b = a
a = 3
print("a = {}".format(a))
print("b = {}".format(b))
# a=3, b =2, 由于a 与b 只是引用的赋值。a 换了引用的对象，但是b却没有换。这里要注意。
# python 的变量是指向该对象，并不能修改该对象的内容

# 共享引用和原处修改 list
L1 = [1, 2, 3, 4]
L2 = L1
print('L1 = {}'.format(L1))
print('L2 = %s' % L2)

L1 = 3
print('-----2----')
print('L1 = {}'.format(L1))
print('L2 = %s' % L2)


print('-----3----')
L1 = [1, 2, 3, 4]
L2 = L1
L1[1] = 6  # 如果修改了一个元素的值，其他引用的内容都会改变
print('L1 = {}'.format(L1))
print('L2 = %s' % L2)

print('-----4----')
L1 = [1, 2, 3, 4]
L2 = L1[:]  # 这里最好采用深拷贝的方式
L1[1] = 6  # 如果修改了一个元素的值，其他引用的内容都会改变
print('L1 = {}'.format(L1))
print('L2 = %s' % L2)

### 判断相等
L = [1, 2, 4]
M = L
print(L == M)
print(L is M)

import sys
s1 = 333
print(sys.getrefcount(s1))


