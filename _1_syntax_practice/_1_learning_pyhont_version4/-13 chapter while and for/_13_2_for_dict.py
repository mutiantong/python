#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     13-2-for-dict
   Description :
   Author :      'Sam Yong'
   date：          2018/7/9
-------------------------------------------------
   Change Activity:
                   2018/7/9:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

D = {
    'name': 'sam',
    'age': 29,
    'sex': 'male',
}

for (key, value) in D.items():
    print("{0}:{1}".format(key, value))

for key in D:
    print("{0}:{1}".format(key, D[key]))

#
print('*' * 20)
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

# 2
print('*' * 30)
for ((a, b), c) in  [((1, 2), 3), ((4, 5), 6), ('ha', 7)]:  # 字符串只能2个，如果是hha, 就会报错
    print(a, b, c)

# 3
# 为了解决2 中的多个字符的问题，可以用* 通配符来解决
for ((a, *b), c) in  [((1, 2), 3), ((4, 5), 6), ('hahahhha', 7)]:
    print(a, b, c)

#
print(range(3))
