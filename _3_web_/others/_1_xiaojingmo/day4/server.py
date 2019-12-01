#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__=Sam Yong
#2018/5/12 20：30

import socket
import urllib.parse
from utils import log
from routes import routes_dict
from routes import route_error
from routes import route_static


class Request(object):
    def __init__(self):
        self.body = ''
        self.path = ''
        self.method = ''
        self.header = {}
        self.query = {}

    def show(self):
        log('body：{}\n, path = {}\n, action = {}, header = {}'.format(self.body,
                                                                      self.path,
                                                                      self.method,
                                                                     self.header))
    def form(self):  # 对于post 放在body 里的表单我们要解析
        body = urllib.parse.unquote(self.body)
        print('body = {}'.format(body))
        if body is None:
            return None
        log('body = {}'.format(body))
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f


request = Request()


#由于出现了get方法里出现这个 path = /static?file=doge.gif，因此需要解析
def parse_for_path(path):
    if '?' in path:
        path, queery_string = path.split('?', 1)
        args = queery_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v

    else:
        path = path
        query = {}

    #log('path = {}, query = {}'.format(path, query))
    return path, query



def response_for_path(path):
    r = {
        '/static': route_static,   # 这个的地方是字典的错误。搞了这么久
    }
    r.update(routes_dict)
    path, query = parse_for_path(path)
    request.path = path
    request.query = query
    # if request.path in routes_all:     # 这样写容易误导
    #     return routes_all[request.path]()
    #log('r = {}'.format(r))
    response = r.get(path, route_error)  # 如果request.path 为空就会报“AttributeError: 'set' object has no attribute 'get'
    return response(request)



def run(host = '127.0.0.1', port = 8000):
    with socket.socket() as s:
        s.bind((host, port))

        while True:
            s.listen(3)
            connection, address = s.accept()    # 这里是表示开始监听
            recv_value = connection.recv(8192)     # 收到响应
            recv_value = recv_value.decode('utf-8') # 怀疑是浏览器的问题
            log('recv_value = {}'.format(recv_value))
            if len(recv_value.split()) < 2:
                continue

            #log('原始请求：{}\n'.format(recv_value))
            # 解析request
            request.body = recv_value.split('\r\n\r\n', 1)[1]
            #log('request.body = ', request.body)
            path = recv_value.split()[1]
            request.method = recv_value.split()[0]
            log('request.method = ', request.method)
            log('path = {}\n'.format(path))
            request.header = recv_value.split('\r\n\r\n', 1)[0].split('\r\n', 1)[1:]
            #request.show()

            #用路由函数进行解析
            response = response_for_path(path)

            #response = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n <h1>hello world<h1>'
            connection.sendall(response)
            connection.close()

def main():
    run()


def test_parse_path():
    path = '/static?file = doge1.jpg'
    parse_for_path(path)
    request.show()

def test_response_for_path():
    path = '/'
    response_for_path(path)

if __name__ == '__main__':
    main()
   # test_parse_path()
   # test_response_for_path()