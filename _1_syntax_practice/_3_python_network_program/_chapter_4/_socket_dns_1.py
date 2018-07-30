# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _socket_dns_1
   Description :
   Author :       Sam Yong
   date：          2018/7/30
-------------------------------------------------
   Change Activity:
                   2018/7/30:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import socket
from pprint import pprint

infolist = socket.getaddrinfo('baidu.com', 'www')
pprint(infolist)

print('*' * 20)
info = infolist[0]
pprint(info)
print('*' * 20)
print(info[0:3])  # 构造的时候要用这个返回值的前三项来进行构造socket

sock = socket.socket(*info[0:3])