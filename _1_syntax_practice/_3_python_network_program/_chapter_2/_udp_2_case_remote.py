#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _udp_2_case_remote
   Description :
   Author :      'Sam Yong'
   date：          2018/7/24
-------------------------------------------------
   Change Activity:
                   2018/7/24:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import socket
import random
from _datetime import datetime
import argparse

MAX_SIZE = 65535


def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print("listing at {}".format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(MAX_SIZE)
        if random.random() < 0.5:
            print("drop this address:{} value".format(address))
            continue

        text = data.decode('ascii')
        print('The client sayed : {}'.format(text))
        message = 'Your data was {} bytes long'.format(len(text))
        sock.sendto(message.encode('ascii'), address)


def client_nodelay(hostname, port):   #未设置超时时间，客户端就会一直卡在那里
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port))

    data = 'This is client, time = {}'.format(datetime.now())
    text = data.encode('ascii')
    sock.send(text)

    data = sock.recv(MAX_SIZE)
    print('The client recv {}'.format(data.decode('ascii')))


def client(hostname, port):   # 设置超时时间
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port)) # connect 将连接地址写入操作系统内存
    print('*' * 20)
    print(sock.getsockname())
    print('*' * 20)

    while True:
        sock.settimeout(5)
        data = 'This is client, time = {}'.format(datetime.now())
        text = data.encode('ascii')
        sock.send(text)

        try:
            data = sock.recv(MAX_SIZE)
        except socket.timeout:
            #raise RuntimeError('connect timeout')
            print('connect timeout')
        else:
            print('The client recv {}'.format(data.decode('ascii')))
            break



if __name__ == '__main__':
    chioses = {
        'server': server,
        'client': client,
    }

    parse = argparse.ArgumentParser(description='Please input ip and port')
    parse.add_argument('role', choices=chioses, help = 'input your choice')
    parse.add_argument('-p', type=int, default=8000, metavar='PORT')
    parse.add_argument('host', help="input your ip")

    args = parse.parse_args()
    function = chioses[args.role]
    function(args.host, args.p)