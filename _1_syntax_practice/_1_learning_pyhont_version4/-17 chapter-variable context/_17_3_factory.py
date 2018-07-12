#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17-3-factory
   Description :
   Author :      'Sam Yong'
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


def maker(N):
    def action(X):
        return X ** N   # 调用maker 生成一个次幂的函数

    return action


f = maker(2)    # 调用的时候，内嵌函数 action记住了N的值。尽管maker调用结束之后返回
val = f(3)      # 本地作用域N 作为被执行的状态的信息保留了下来
print(val)
