#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _1_getitem_setitem
   Description :
   Author :      'Sam Yong'
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Indexer(): # 索引和分片，应该用 __setitem__
                   # 这个不是首选方法，这个是退而求其次
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, key, value):
        self.data[key] = value


if __name__ == '__main__':
    x = Indexer()
    print(x[2])

    print(x[2:4])

    x[3] = 10 # 通过索引设置值
    print(x[:])

