#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _26_1_demo1_first_class
   Description :
   Author :      'Sam Yong'
   date：          2018/7/13
-------------------------------------------------
   Change Activity:
                   2018/7/13:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class FirstClass:
    x = 10

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()
x.setdata('nihao')
y.setdata('haha')
x.display()
y.display()
print('*' * 20)
print(x.x)
print(y.x)
x.x = 100
print('*' * 20)
print(x.x) # 100
print(y.x) # 10
print('*' * 20)
FirstClass.x = 30
print(x.x) # 100 x 由于赋值过x,x就在自己的命名空间里。搜索元素的最小方式
print(y.x) # 30 , y并没有赋值过x,因此还调用以前类对象的内容
