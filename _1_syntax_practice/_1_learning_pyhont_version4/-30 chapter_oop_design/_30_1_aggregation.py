#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _30_1_aggregation
   Description :
   Author :      'Sam Yong'
   date：          2018/7/17
-------------------------------------------------
   Change Activity:
                   2018/7/17:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader   # 通过组合的方式实现
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys

    obj = Uppercase(open('1.txt'), sys.stdout)
    obj.process()
