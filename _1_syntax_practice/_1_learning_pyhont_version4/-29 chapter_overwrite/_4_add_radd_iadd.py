#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _4_add_radd_iadd
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class Computer:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Computer(self.val + other)

    def __radd__(self, other):
        return Computer(other + self.val)

    def __iadd__(self, other):
        self.val += other
        return self


x = Computer(10)
y = Computer(20)
print((x + 1).val)
print((1 + y).val)
x += 1
print(x.val)