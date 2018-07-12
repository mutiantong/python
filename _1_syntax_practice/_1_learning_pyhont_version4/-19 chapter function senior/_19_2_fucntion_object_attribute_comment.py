#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19-2-函数对象，属性和注解
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# python 的 函数即对象， 函数自身储存在内存中

def func(sum):

    print(sum)

func.cout = 1  # 属性与对象相关，与作用域无关
val = func(10)
print(dir(func))
print(val)