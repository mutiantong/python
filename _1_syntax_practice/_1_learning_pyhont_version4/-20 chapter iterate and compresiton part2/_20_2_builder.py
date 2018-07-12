#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20-2-生成器
   Description :
   Author :      'Sam Yong'
   date：          2018/7/11
-------------------------------------------------
   Change Activity:
                   2018/7/11:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 生成器，迭代器是按需返回一个值，节省内存

# 生成器: 返回一个值，并从退出的地方继续的函数
# 生成器的性能更好
# 状态挂起，从yield 的地方继续，保存了内容

# 生成器的协议 send 和 next

val = (x * x for x in [1, 2, 3, 4]) # 生成器表达式
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print('*' * 20)
print(next(val))
