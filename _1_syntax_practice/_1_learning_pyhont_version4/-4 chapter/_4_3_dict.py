#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     4-3-字典
   Description :
   Author :      'Sam Yong'
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

# 字典的创建方式
D = {
    'food':'haha',
    'quality':1,
    'colour':'pink'
}

print(D)

D['food'] = 'fish'
print(D)


# 嵌套的例子
D = {
    'name':'bob',
    'job':'dev',
    'age':40,
}
print(D)

D['name'] = {
    'first': 'bob',
    'last': 'Smith',
}
print(D)

#D['job'].append('nihao')  # 不能直接这么搞，

D['job'] = ['dev', 'mgr']
D['job'].append('nihao')  # 因为list 理论上是可以无限增长的，因此可以用这个
print(D)


# 键值的排序？        高级模块： pickle, shelve
D = {
    'c': 1,
    'a': 2,
    'b':3,
}
print(D)

## 如果我们要按顺序打印出来这个D的内容
### 第一种方式
ks = list(D.keys())
ks.sort()
for key in ks:
    print(key, '=>', D[key])


### 第二种方式
D = {
    'c': 1,
    'a': 2,
    'b':3,
}
print(D)
for key in sorted(D):
    print(key, '=>', D[key])

# 迭代和优化
# 在python中 列表解析相关的工具（map, filter)通常比for循环块两倍


# if 或其他方法来检测键值是否存在
D = {
    'c': 1,
    'a': 2,
    'b':3,
}

## 第1种，采用if
if 'f' not in D:
    print("f is missing")

## 第2中， 采用get
value = D.get('f', None)   # None 是获取不到的默认值
print(value)


value = D.get('c', 0)
print(value)
