#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     18-4-keyword-only参数
   Description :
   Author :      'Sam Yong'
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

def kwonly(a, *b, c):
    print(a, b, c) # *b 后面的c , 必须使用关键字参数才能调用

kwonly(1, 22, 33, c=2)


def kwonly1(a, *b, c=12, d=13):
    print(a, b, c, d) # *b 后面的c , 必须使用关键字参数才能调用

kwonly1(1, 22, 33, c=2, 11) # key word only 后面的调用必须是以关键字调用