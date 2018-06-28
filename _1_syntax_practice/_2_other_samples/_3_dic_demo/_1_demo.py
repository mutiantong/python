#!/usr/bin/python
# -*- coding:utf-8 -*-

class Demo(object):
    name = 'sam'
    age = 29


demo_user = Demo
temp = {
    'name' : 'bob',
    'age':45,
}

demo_user.update(temp)

print('demo_user.name = {}, demo_usr.age = {}'.format(demo_user.name, demo_user.age))
print('end')