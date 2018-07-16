#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     specialize
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Super:
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replace.method')


class Extender(Super):
    def method(self):
        print('strart Extender method')
        Super.method(self)
        print('strart Extender method')


class Provider(Super):
    def action(self):
        print('in Provider.action') # 子类往超类填空的方法。


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__) # __name__ 就是类名
        klass().method()

    print('\nProvider:...')
    x = Provider()
    x.delegate()
