#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _udp_1_use
   Description :
   Author :      'Sam Yong'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import argparse
import random
import socket
import sys
from _datetime import datetime

MAX_BYTES = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 1

    sock.bind(('127.0.0.1', port))                           # 2 bind
    print('Listing at {}', sock.getsockname())

    while True:
        data, address = sock.recvfrom(MAX_BYTES)               # 3 revcfrom
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        message = 'Your data was {} bytes long'.format(len(data))
        sock.sendto(message.encode('ascii'), address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 1
    text = 'The time is {}'.format(datetime.now())
    #text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')  # 指定编码格式 asciis
    sock.sendto(data, ('127.0.0.1', port))                   # sendto
    print('The OS assigned me the address {}'.format(sock.getsockname())) # getsockname 查看ip 和端口号
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server says {!r}, address'.format(data.decode('ascii'), address))


if __name__ == '__main__':
    choices = {
        'client': client,
        'server': server,
    }

    # test
    value = datetime.now()
    print(value)

    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')

    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
