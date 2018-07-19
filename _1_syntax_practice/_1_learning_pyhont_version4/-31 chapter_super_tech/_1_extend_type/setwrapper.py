#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setwrapper
   Description :
   Author :      'Sam Yong'
   date：          2018/7/17
-------------------------------------------------
   Change Activity:
                   2018/7/17:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def interset(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):              return len(self.data)
    def __getitem__(self, item):    return self.data[item]
    def __and__(self, other):       return self.interset(other)
    def __or__(self, other):        return self.union(other)
    def __repr__(self):             return 'Set:' + repr(self.data)



if __name__ == '__main__':
    x = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(x.union(Set([11, 12, 1, 3, 4, 5])))
    print(x | Set([1, 2, 3, 4, 11, 234]))
    print(x.__class__)
    print(type(x))   # 一个实例的类型是其类
    print(type(Set)) # 一个类的类型是type