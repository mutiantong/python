#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     18-3-解包参数
   Description :
   Author :      'Sam Yong'
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

def func(a, b, c, d):
    print(a, b, c, d)

arg = [1, 2, 3, 4]
func(*arg) # 通过* 将arg解包一个list 传给函数

args = {'a':1, 'b':2, 'c':3, 'd':4,}
func(**args) # 通过** 将args包解压一个dict