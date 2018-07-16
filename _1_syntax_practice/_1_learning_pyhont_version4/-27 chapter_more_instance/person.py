#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     person
   Description :
   Author :      'Sam Yong'
   date：          2018/7/13
-------------------------------------------------
   Change Activity:
                   2018/7/13:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Person:

    def __init__(self, name, job=None, pay=0):  # 这一行是本地变量
        # 这里面是实例对象属性
        # self 是新创建的实例对象
        self.name = name  # name, job， pay 是状态信息
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent): # self 对应一个实例，在调用的时候就是把实例直接传进去
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return "[Person: {0}， pay = {1}]".format(self.name, self.pay)


# if __name__ == '__main__':
#     # test code
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='dev', pay=100000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)
#     print(bob.lastName(), sue.lastName())
#     sue.giveRaise(.10)
#     print(sue.pay)
#     print(bob)
#     print(sue)
