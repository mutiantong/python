#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     manager
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

from person import Person  #


class Manager(Person):
    def __init__(self, name, pay): # 定制构造
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
        # 只是扩展接口，并不是重写
        # 类方法总是可以在事例中调用
        # instacne.method(args, ...)在Python中自动转换下面
        # class.method(instance, args...)


if __name__ == '__main__':
    tom = Manager('Tom jones' , 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print(tom)