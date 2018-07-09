#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17-1-global
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

var = 99
def local():
    var = 0

def glob1():
    global var
    var += 1

print(var)
local()
print(var)
glob1()
print(var)
