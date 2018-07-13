#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _25_1_class_tree
   Description :
   Author :      'Sam Yong'
   date：          2018/7/13
-------------------------------------------------
   Change Activity:
                   2018/7/13:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class C2(object):
    print('this is C2')


class C3(object):
    print('this si C3')


class C1(C2, C3):
    x = 10
    print('this is C1')


T1 = C1()
T1.x = 12
print(T1.x)
print('*' * 20)
T2 = C1()
print(T2.x)

# output:
# this is C2       类是一个实例工厂，只会创建一次。但是实例有很多个
# this si C3
# this is C1
# 12
# ********************
# 10