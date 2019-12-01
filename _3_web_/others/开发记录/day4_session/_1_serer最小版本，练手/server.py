#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__=Sam Yong
#2018/5/12 20：30

import socket
from utils import log

def run(host = '127.0.0.1', port = 3000):
    with socket.socket() as s:
        s.bind((host, port))

        while True:
            s.listen(5)
            connection, address = s.accept()    # 这里是表示开始监听
            request = connection.recv(1024)     # 收到响应
            request = request.decode('utf-8')
            if len(request.split()) < 2:
                continue

            log('request = {}\n'.format(request))

            response = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n <h1>hello world<h1>'
            connection.sendall(response.encode('utf-8'))
            connection.close()

def main():
    run()


if __name__ == '__main__':
    main()