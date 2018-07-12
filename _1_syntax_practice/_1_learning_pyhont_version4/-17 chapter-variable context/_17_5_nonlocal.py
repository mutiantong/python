#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17-5-nonlocal
   Description :
   Author :      'Sam Yong'
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

def testr(start):
    state = start
    def nested(lable):
        print(lable, state)
    return nested


F = testr(0)
F('spam')


###
print('*' * 20)
def testr1(start):
    state = start
    def nested(lable):
        nonlocal state
        print(lable, state)
        #state += 1 默认情况是不能修改state的内容，因为已经被引用了
        # 必须声明nolocal

        state += 1
    return nested


F = testr1(0)
F('spam')
F('spam1')

# nonlocal 边界情况
# nonlocal 必须是已经赋值过的，不能单独赋值