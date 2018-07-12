#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17-2-nest
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 开始
x = 99


def f1():
    x = 88

    def f2():
        print(x)

    f2()


f1()
# 结果打印了88

##
print('*' * 20)


def f1():
    x = 99

    def f2():
        print(x)

    return f2


action = f1()
action()
