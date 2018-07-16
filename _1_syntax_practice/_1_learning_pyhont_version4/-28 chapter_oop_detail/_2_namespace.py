#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _2_namespace
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

X = 11


def f():
    print('f() = {}'.format(X))


def g():
    X = 22
    print('g() = {}'.format(X))


class C:
    X = 33

    def m(self):
        X = 44  # 函数内部的变量，并不会产生改变
        self.X = 55  # 只是改变实例的属性X, 不改变类属性


class D(C):
    def haha(self):
        print('this D , haha')


if __name__ == '__main__':
    print(X)  # 11
    f()  # 11
    g()  # 22
    print(X)  # 11

    print('*' * 10)
    obj = C()
    print(obj.X)  # 33

    obj.m()
    print(obj.X)  # 55
    print(C.X)  # 33
    # print(C.m.X) 只能在调用的时候看见，平常无法访问

    print('*' * 10)

    c = C()
    d = D()
    print(d.__class__)
    print(d.__class__.__bases__)
    dir(d)
    # print(d.__dict__.keys())
