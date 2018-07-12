#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     4-1-demo
   Description :
   Author :      'Sam Yong'
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 数字对象内容
import math
print(math.pi)


# list 序列操作

s = 'spam'

print('s len = {}'.format(len(s)))

# 切片操作
str = 'mutiantong'
print(str[1:4])
print(str[:4])
print(str[4:])
print(str[:-1])

# 字符串支持 + 操作，和 * 操作

str = 'mutianton'
str = 'mutiantong' + '_best'
print(str)

str = 'mutiantong' * 3
print(str)

#str = 'mutiantong' - 'tong' # 没有减法操作

# 字符串是常量，不能显示改变字符串单个字符内容
# str = 'mutiantong'
# str[1] = 'z'


# 字符串提供查找操作
str = 'mutiantong'
val = str.find('mu')
print(val) # 返回的是一个偏移

# 字符串提供替换

str = 'mutiantongmu'
val = str.replace('mu','MU')
val1 = str.replace('mu','MU',1)  # count是替换第几个
print('val = {}, val1 = {}'.format(val, val1))


line = 'aa,bb,cc,dd'
print(line.split(','))


# 格式化字符串
str = '{}'.format('mutiantong')
str1 = '%s' % ('mutiantong1')
print('str = ', str)
print('str1 = ', str1)

# 查看内容
help(str.replace)