# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17-4-作用域循环变量
   Description :
   Author :      'Sam Yong'
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts


actions = makeActions()
print(actions[0](2))
print(actions[1](2))
print(actions[2](2))
print(actions[3](2))
# 这些值都是16， 因为嵌套函数lambda作用域的变量i， 在被调用的时候才进行查找
# 实际调用的时候就是记得最后一次迭代循环中循环变量的值


#######
print('*' * 20)
# 为了解决上面的情况，就要用默认参数，让嵌套函数在创建的时候评估，而不是在调用的时候
def makeActions2():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts


actions = makeActions2()
print(actions[0](2))
print(actions[1](2))
print(actions[2](2))
print(actions[3](2))
