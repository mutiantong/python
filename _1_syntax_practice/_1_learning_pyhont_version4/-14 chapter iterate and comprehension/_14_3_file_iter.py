#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     14-3-file-iter
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 打卡一个文件，并把里面的\n去掉
f = open('test.txt')
lines = f.readlines()
print(lines)
print("*" * 20)
lines = [line.rstrip() for line in lines]
print(lines)

#如果有更简单的方式
line = [line.rstrip() for line in open('test.txt')] # 因为文件是迭代器
# 对于大的文件，列表解析就会很快
print(line)