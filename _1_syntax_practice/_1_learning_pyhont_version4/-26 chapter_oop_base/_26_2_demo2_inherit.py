#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _26_2_demo2_inherit
   Description :
   Author :      'Sam Yong'
   date：          2018/7/13
-------------------------------------------------
   Change Activity:
                   2018/7/13:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class FirstClass:
    x = 10

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = {0}'.format(self.data))


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return "thridclass : {}".format(self.data)

    def mul(self, other):
        self.data *= other

    def __call__(self, *args, **kwargs):
        print('hhhhhhhh')


a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
print(b)

a.mul(3)
print(a)
print("*" * 20)
a("dfdsfdsfdsfdsfsd")

print("*" * 20)
print(a.__class__)
print(dir(a))