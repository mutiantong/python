#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__=Sam Yong
# 2018/5/12 20：30

from model import Model


class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')  # 由于form是一个字典的表单，因此用这种方式来获取
        self.password = form.get('password', '')

    def show(self):
        print('self.username = {}, slef.passwd = {}'.format(self.__dict__['username'], self.__dict__['password']))

    def validate_login(self):
        #这个地方就要从model里面把数据都取出来，然后self是否在里面
        m = User.find_by(username = self.username) # 这里是调用类方法？

        return m is not None and m.password==self.password

    def validate_register(self):  # 验证注册的有效性
        return len(self.username) > 2 and len(self.password) > 2
