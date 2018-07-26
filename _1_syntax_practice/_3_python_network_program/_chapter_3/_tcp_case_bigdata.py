#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _tcp_case_bigdata
   Description :
   Author :      'Sam Yong'
   date：          2018/7/26
-------------------------------------------------
   Change Activity:
                   2018/7/26:
-------------------------------------------------
"""
__author__ = 'Sam Yong'


import socket
import argparse
import sys

BYTE_COUNT = 1024

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))

    sock.listen(1)

    n = 0
    while True:
        sock_client, sock_client_name = sock.accept()
        print('The client socket name is ', sock_client_name)

        while True:
            data = sock_client.recv(1024)
            if not data:
                break

            print('recv client {} mess {}'.format(sock_client.getsockname(), data.decode('ascii')))

            text = data.decode('ascii').upper().encode('ascii')
            sock_client.sendall(text)
            n += len(text)
            print('\r  %d bytes processed so far' % (n,), end=' ')
            sys.stdout.flush()
        print()
        sock_client.close()
        print('socket close')


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    print('The client socket name is ', sock.getsockname())

    sent = 0
    message = b'This is client'
    while sent < BYTE_COUNT:
        data = '{}'.format(sent)
        message += data.encode('ascii')
        sock.sendall(message)
        sent += len(message)
        print('\r  %d bytes sent' % (sent,), end=' ')
        sys.stdout.flush()
    print()
    sock.shutdown(socket.SHUT_WR)

    print('Receiving all the data the server sends back')

    recived = 0
    while True:
        data = sock.recv(42)
        if not recived:
            print(' The first data received says', repr(data))

        if not data:
            break

        recived += data
        print('\r  %d bytes received' % (recived,), end=' ')
    print()
    sock.close()


if __name__ == '__main__':
    choises = { 'server':server, 'client':client,}
    parser = argparse.ArgumentParser(description='This is bigdata')
    parser.add_argument('role', choices=choises, help='input server or client')

    args = parser.parse_args()

    function = choises[args.role]
    function("127.0.0.1", 8000)

