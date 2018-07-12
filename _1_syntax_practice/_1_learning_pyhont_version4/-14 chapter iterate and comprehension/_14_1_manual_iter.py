#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     14-1-manual-iter
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

L1 = [1, 2, 4, 5]
L2 = iter(L1)
print(L2.__next__())
print(L2.__next__())

print(L2 is iter(L1))  # list 并没有返回一个迭代，要手动来调用

f = open('test.txt', 'r')
print(f is iter(f)) # 文件对象本身就是可迭代的

# dict
print('*' * 20)
D = {
    'a': 1,
    'b': 2,
    'c': 3,
}

iterD = iter(D)
print(iterD.__next__())
print(iterD.__next__())
print(iterD.__next__())

# 可迭代对象一次性返回一个结果， 如果所有都返回，就要存放到一个list里面
