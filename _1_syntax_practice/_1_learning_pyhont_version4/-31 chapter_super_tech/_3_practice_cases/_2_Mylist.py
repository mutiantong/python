#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _2_Mylist
   Description :
   Author :      'Sam Yong'
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

class Mylist():
    def __init__(self,data):
        self.data = list(data)

    def __add__(self, other):
        return Mylist((self.data + list(other)))

    def __repr__(self): # 返回一个string
        return 'value = {}'.format(list(self.data))

    def __getitem__(self, item):
        return self.data[item]


class MylistSub(Mylist):
    count = 0

    def __repr__(self):
        print("cout call = {}".format(MylistSub.count))


if __name__ == '__main__':
    mylist1 = Mylist((1,2,3,4))
    print(mylist1)

    vaule = mylist1 + [5,6,7,8]
    print(vaule)
    print(type(vaule))
    print(vaule[1])