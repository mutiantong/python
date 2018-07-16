#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _5_callback
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class CallBack:
    def __init__(self, color):
        self.color = color

    def __call__(self, *args, **kwargs):
        print('turn', self.color)


if __name__ == '__main__':
    cb1 = CallBack('blue')
    cb2 = CallBack('green')

    cb1()
    cb2()