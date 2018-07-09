#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     8-2-dict操作
   Description :
   Author :      'Sam Yong'
   date：          2018/7/5
-------------------------------------------------
   Change Activity:
                   2018/7/5:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

D1 = {
    "name": "mutiantong",
    "age": 29,
}

print(len(D1))
print('age' in D1)
print('haha' in D1)
print(D1.keys())

D1.pop('age')
print(D1)

#字典用于实现 稀疏数据结构

# 字典很容易访问不存在的key,触发Missing-key错误
D2 = {
    "name": "mutiantong",
    "age": 29,
}

if 'haha' in D2:
    print(D2['haha'])
else:
    print("else erroro")

try:
    print(D2['hhhh'])
except KeyError:
    print("key error")

print(D2.get('haha', 'meiyou'))

# python3 特有
D = {x:x**2 for x in [1, 2, 3, 4]}

# 字典视图
# keys, values, items 返回视图对象
# 视图对象， 可迭代
print(D)
list
k = D.keys()
print(list(k))
v = D.values()
print(v)
print(list(v))

print(list(D.items()))


