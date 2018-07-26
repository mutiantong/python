#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _udp_4_case_broadcast
   Description :
   Author :      'Sam Yong'
   date：          2018/7/25
-------------------------------------------------
   Change Activity:
                   2018/7/25:
-------------------------------------------------
"""
__author__ = 'Sam Yong'

import socket
import argparse

BUFFER_SIZE = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening for datagrams at {}'.format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(BUFFER_SIZE)
        text = data.decode('ascii')
        print('The client says{}, address = {}'.format(text, address))


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    text = 'Broadcast datagram!'
    sock.sendto(text.encode('ascii'), ('192.168.3.255', port))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parse = argparse.ArgumentParser(description='This is broadcast case')
    parse.add_argument('role', choices=choices)
    parse.add_argument('-p', type=int, metavar='PORT', default=1060)

    args = parse.parse_args()
    function = choices[args.role]
    function(args.p)

