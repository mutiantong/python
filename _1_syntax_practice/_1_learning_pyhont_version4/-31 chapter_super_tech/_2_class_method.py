#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _2_class_method
   Description :
   Author :      'Sam Yong'
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Spam:
    numInstances = 0

    @classmethod
    def __count(cls):
        cls.numInstances += 1

    def __init__(self):
        Spam.numInstances += 1
        self.__count()

    def __del__(self,):
        Spam.numInstances -= 1

    @staticmethod
    def display():
        print('Spam static create = {}'.format(Spam.numInstances))


    @classmethod
    def print(cls,):
        print('{} create = {}'.format(cls, cls.numInstances))



class Sub(Spam):
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numInstances = 0


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    Spam.print()
    b.display()

    print('*' * 20)
    y1 = Sub()
    y2 = Sub()
    Sub.print()
    z1 = Other()
    z2 = Other()
    z3 = Other()
    z1.print()   # 类可以有层级的部分内容
