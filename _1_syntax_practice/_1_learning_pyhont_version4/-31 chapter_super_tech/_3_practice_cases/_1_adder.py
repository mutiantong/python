#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _1_adder
   Description :
   Author :      'Sam Yong'
   date：          2018/7/19
-------------------------------------------------
   Change Activity:
                   2018/7/19:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Adder():
    def add(self, x, y):
        print('Not Implimentd')


class ListAdder(Adder):
    def add(self, x, y):
        #  print("x = {}, y = {}".format(x, y))
        print("x = {}, y = {}".format(list(x), list(y)))  # list函数将tupleb编程list, 原先是list也还是list

        # # method 1
        # tmp = x[:]
        # for val in y:
        #     if val not in tmp:
        #         tmp.append(val)
        # return tmp

        # method2     #  x[:] + [x for x in y if x not in x[:]]
        tmp = x[:]  # TypeError: 'int' object is not subscriptable 如果用上面就会出现这个问题， 推导式里面不可以出现式子

        return tmp + [x for x in y if x not in tmp]


class DictAdder(Adder):
    def add(self, x, y):
        print("x = {}, y = {}".format(dict(x), dict(y)))
        temp = x
        print("temp = {}".format(temp))

        # method 1
        # for k in y:
        #     if k not in temp:
        #         temp[k] = y[k]
        # return temp

        # method 2
        # 这里不应该用嵌套，这里是hash
        new = {}
        for k in x: new[k] = x[k]
        for k in y: new[k] = y[k]
        return new


class AdderMore():
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        print('Not Implimentd')


class ListAdderMore(AdderMore):
    def __add__(self, other):
        return self.data[:] + [x for x in other if x not in self.data]


class DictAdderMore(AdderMore):
    def __add__(self, other):
        new = {}
        for k in self.data: new[k] = self.data[k]
        for k in other: new[k] = other[k]
        return new


if __name__ == '__main__':
    type = Adder()
    type.add([1, 2, 3], [4, 5, 6, 1])

    print('*' * 20)
    print('ListAdder')
    listType = ListAdder()
    value = listType.add([1, 2, 3], [4, 5, 6])
    print(value)

    print('*' * 20)
    print('DictAdder')
    dictType = DictAdder()
    value = dictType.add({'name': 'mutiantong', 'age': 29}, {'jos': 'dev', 'locate': 'ShangHai'})
    print(value)

    print('#' * 20)
    typeMore = AdderMore([0])
    print(typeMore + [0, 1])

    print('*' * 20)
    print('ListAdderMore')
    listTypeMore = ListAdderMore([1, 2, 3, 4, 5, 6])
    print(listTypeMore + [2, 3, 4, 5, 6, 7, 8, 9])

    print('*' * 20)
    print('DictAdderMore')
    dictType = DictAdderMore({'name': 'mutiantong', 'age': 29})
    value = dictType + {'jos': 'dev', 'locate': 'ShangHai'}
    print(value)
