#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__=Sam Yong
# 2018/5/12 20：30

# from utils import log
import json


def save(data, path):
    # 把一个字典dict或者列表list写入文件, w是每次都重新写
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        f.write(s)

def load(path):
    """
    本函数从一个文件中载入数据并转化为 dict 或者 list
    path 是保存文件的路径
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        return json.loads(s)

def test():
    path = '../db/a.txt'
    l = {
        '1': "sfsdf"
    }
    save(l, path)


# 用于数据处理的基类
class Model(object):
    @classmethod
    def new(cls, form):
        m = cls(form)
        return m

    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path = 'db/{}.txt'.format(classname)
        return path

        # 有了数据我们还应该存起来， 存应该是属于基础功能
    def save_orign(self):  # 将注册写进文本
        # 因为我们用的是每次都重新写一遍，因此需要将所有的list或者dict获取出来，然后写进去
        path = self.db_path()  # 这个版本的问题在于每次会重新写，并不是保留所有的，这个地方就有问题
        l = []
        l.append(self.__dict__)
        print('db_path = {}'.format(path))
        print('list = {}'.format(l))
        save(l, path)

    @classmethod
    def find_by(cls, **kwargs):
        #1 拿到所有对象
        all = cls.all()
        #2 拿到单个字典的内容，这是一个key:value的字典中的某项。确实如此
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value

        for item in all:
            if item.__dict__[k] == v:
                return item
        return None

    @classmethod
    def all(cls):
        path = cls.db_path()
        module = load(path)
        ms = [cls.new(m) for m in module]#列表推倒式， 为每一个字典创建一个对象，并将对象构成列表
        return ms


    def save(self):
        #先打开，获取所有的list
        models = self.all()
        models.append(self) # 此时这个里面应该是个list, 是对象
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)


class Nane(Model):
    def __init__(self, form):
        self.username = form.get('username', '')  # 由于form是一个字典的表单，因此用这种方式来获取
        self.password = form.get('password', '')


if __name__ == "__main__":
    l = {
        'username':'111',
        'password':'222'
    }

    m = Nane.new(l)
    m.save_orign()