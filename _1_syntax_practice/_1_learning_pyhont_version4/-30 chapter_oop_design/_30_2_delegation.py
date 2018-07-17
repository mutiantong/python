#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _30_2_delegation
   Description :
   Author :      'Sam Yong'
   date：          2018/7/17
-------------------------------------------------
   Change Activity:
                   2018/7/17:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 控制器对象内 嵌套其他对象。 控制器管理，其他对象实际操作(运算）

class wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print('Trace: ', item)
        return getattr(self.wrapped, item)


if __name__ == '__main__':
    x = wrapper([1, 2, 3, 4]) #
    x.append(4) # 实际调用的是list的append, wrapper对象的append委托list的append来实现
