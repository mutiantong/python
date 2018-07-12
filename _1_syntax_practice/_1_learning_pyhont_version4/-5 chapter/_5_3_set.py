#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     5-3-set
   Description :
   Author :      'Sam Yong'
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

y = set('abcdef')
print(y)

x = set('ab')

# set 是无序操作，可以使用减法
z = y -x
print(z)

w = set('ghi')
v = z ^ w  # 并集
print(v)

# 创建结合的方式是set([]) 由于string 本身是一个[]
# 集合是不变量的内容
u = set([1, 2, 16, 5])
print(u)

# 集合解析
t = { x * x for x in u}
print(t)

# 集合的用处
## 过滤重复
l = [1, 2, 3, 4, 1, 2, 3, 4]
newL = list(set(l))
print(newL)

## 记录访问过的位置

## 处理交集共有的对象？


