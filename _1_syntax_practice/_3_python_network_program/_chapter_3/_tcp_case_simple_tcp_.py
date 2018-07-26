#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _tcp_case_simple_tcp_
   Description :
   Author :      'Sam Yong'
   date：          2018/7/25
-------------------------------------------------
   Change Activity:
                   2018/7/25:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


import argparse
import socket


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                       ' %d bytes before the socket closed'
                       % (length, len(data)))
        data += more
    return data

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SO_REUSEADDR 指定可以使用的客户端之前连接的正在关闭的端口
    sock.bind((host, port)) # bind 不一定只能用于服务端调用，只是指定一个端口
    sock.listen(1) # listen调用无法撤销；会彻底改变套接字角色，就是监听
                   # listen整数是等待连接的最大数目
    print('listing at : {}'.format(sock.getsockname()))

    while True:
        sock_client, sock_hostname = sock.accept() # accept 也是监听， 一个新客户端连接产生一个新的套接字
        print('we have accepeted a connection form'.format(sock_hostname))
        print(' sockname = ', sock_client.getsockname())
        print(' sockpeer = ', sock_client.getpeername())
        message = recvall(sock_client, 16)
        print('  Incoming sixteen-octet message:', repr(message))
        sock_client.sendall(b'Farewell, client')
        sock_client.close()
        print('  Reply sent, socket closed')


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('The client connect success, and socket = {}'.format(sock.getsockname()))
    sock.sendall(b'Hi there, server') # sendall 实现了全部发送， P43， 这里16就表示这个发送的是16个字符，实际并不是这么写
    reply = recvall(sock, 16)
    print('The server said', reply)
    sock.close()


if __name__ == '__main__':
    choises = { 'server': server, 'client': client,}
    parser = argparse.ArgumentParser(description='This is a test of tcp demo')

    parser.add_argument('role', choices=choises, help='please input your choise')
    parser.add_argument('-host', default='127.0.0.1', help='input your host')
    parser.add_argument('-port', type=int, metavar='PORT', default=8000, help='please input your port')

    args = parser.parse_args()

    function = choises[args.role]
    function(args.host, args.port)
