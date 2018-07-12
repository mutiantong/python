#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     5-1-num-const
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

print('8进制：', 0o7)
print('16进制', 0x12)
print('10进制', 12)

# 除法
print(10/3)
print(10//3)
print(10%3)

# 格式化位数
print(10/3)
num = 10/3
print('%e'% num)
print('%4.2f'% num)
print('{0:4.2f}'.format(num))

# 连续比较
print(1<3<4)

# 10进制转8进制 oct; 10转16 hex; 10转2 bin

# eval 将 字符串转化数字
print(eval('1234'))

