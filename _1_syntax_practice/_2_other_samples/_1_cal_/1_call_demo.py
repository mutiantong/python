#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018年6月12日11:22:15

class X(object):
    def __init__(self, a, b, range):
        print('__init__')
        self.a = a
        self.b = b
        self.range = range

    def __call__(self, a, b):
        print('__call__')
        self.a = a
        self.b = b
        print('__call__ with （{}, {}）'.format(self.a, self.b))

    def __del__(self):
        print('__del__, 显示调用del')
        del self.a
        del self.b
        del self.range

XInstance = X(1,2,10)

Resutl  = XInstance(1,2)    # call必须实例化之后才能调用

print(Resutl)
print('hhh')