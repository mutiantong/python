#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     15-1-doc-class
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class Help():
    '''
    this is help
    '''
    pass

print(Help.__doc__)   # 直接打印 注释内部的内容

print("*" * 20)
print(help(Help))