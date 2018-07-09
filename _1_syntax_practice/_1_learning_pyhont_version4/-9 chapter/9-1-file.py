#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     9-1-file
   Description :
   Author :      'Sam Yong'
   date：          2018/7/6
-------------------------------------------------
   Change Activity:
                   2018/7/6:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 文件内容
myfile = open(r'myfile.txt', 'w')
myfile.write('hello\n')
myfile.write('nihao\n')
myfile.close()

myfile = open(r'myfile.txt', 'r')
print(myfile.readline())
myfile.close()

# 文件迭代器
print('*' * 30)
for line in open('myfile.txt'):
    print(line, end="") #
