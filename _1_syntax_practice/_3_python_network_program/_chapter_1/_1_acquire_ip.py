#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _1_acquire_ip
   Description :
   Author :      'Sam Yong'
   date：          2018/7/23
-------------------------------------------------
   Change Activity:
                   2018/7/23:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import socket

if __name__ == '__main__':
    hostname = "www.baidu.com"
    addr = socket.gethostbyname(hostname)
    #
    print(addr)