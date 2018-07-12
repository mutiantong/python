#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     9-2-file-object
   Description :
   Author :      'Sam Yong'
   date：          2018/7/6
-------------------------------------------------
   Change Activity:
                   2018/7/6:
-------------------------------------------------
"""
__author__ = 'Sam Yong'
X, Y, Z = 43, 44, 45
S = 'spam'
D = {
    'a': 1,
    'b': 2,
}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('{0},{1},{2}\n'.format(X, Y, Z))
F.write(str(L) + '$' + str(D) + "\n")
F.close()

# 采用pickle

F = open(r'dataPikle.txt', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('dataPikle.txt', 'rb')
E = pickle.load(F)
F.close()
print(E)

# struct 处理二进制数据？
# PySerial扩展

# 拷贝
# l = l1[:]
# D = d1.copy()
# 深层递归拷贝
# import copy
# x = copy.deepcopy(y)



# 相等 与 is
# is 表示对象相同，同一个内存地址
# 相等只是遍历值的内容相同

# None 有对象，有内存，一般用来判断