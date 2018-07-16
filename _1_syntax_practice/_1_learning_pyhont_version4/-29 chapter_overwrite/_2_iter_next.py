#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _2_iter_next
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 自定义迭代器

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


if __name__ == '__main__':
    for i in Squares(1, 10):
        print(i)