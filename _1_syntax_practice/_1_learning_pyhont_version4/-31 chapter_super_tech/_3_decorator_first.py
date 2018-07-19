#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _3_decorator_first
   Description :
   Author :      'Sam Yong'
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class Tracer():
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args):
        self.calls += 1
        print('{} call , para {}, call counts {}'.format(self.func, args, self.calls))
        print('*arg = {}'.format(*(args))) # *args单独使用的是第一个值
        return self.func(*args) # 调用的时候进行了一次序列化的组合， # 即函数调用的时候使用解包参数将list打包

@Tracer
def spam(a, b, c):
        print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam(4, 5, 6)
    spam(7, 8, 9)