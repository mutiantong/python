#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     7-2-raw用法
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 如果要打卡一个文件
myfile = open("C:\new\text.txt", "w")
# 这里面就有两个问题， \n和\t都会产生转义
myfile.close()

myfile = open(r'C:\new\text.txt', "w")
myfile.close()

