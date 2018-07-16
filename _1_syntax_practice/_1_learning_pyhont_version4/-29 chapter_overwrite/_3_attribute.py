#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _3_attribute
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class empty:
    def __getattr__(self, item):
        if item == 'age': # 对于未定义的进行拦截，定义的不拦截
            return 40
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value # 只能用这种方式赋值
        else:
            raise AttributeError



X = empty()
#print(X.age)
X.age = 60
print(X.age)