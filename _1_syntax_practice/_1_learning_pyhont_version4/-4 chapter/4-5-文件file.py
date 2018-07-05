#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     4-5-文件file
   Description :
   Author :      'Sam Yong'
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


# 写文件
# f = open('4-5-demo.txt', 'a+')   # w 是覆盖， a 是追加
# f.write("hello world")
# f.close()


# 读文件
# f = open('4-5-demo.txt', 'r+')
# help(f)
# text = f.read()
# print(text)
# f.close()

# 管道、先进先出队列（FIFO）、套接字、通过键访问文件、对象持久、基于描述符的文件
# 关系数据库
# 面对对象数据库接口

filename1 = "4-5-demo.txt"
filename = r'{0}'.format(filename1)
f = open(filename, 'a+')   # w 是覆盖， a 是追加
f.write("hello world")
f.close()