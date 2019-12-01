#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os
import socket

def protocol_of_url(url):
    index = url.index(':')
    protocal = url[:index]
    result = ''
    if protocal == 'http':
        result = 'http'
    elif protocal == 'https':
        result ='https'
    else:
        result = ''
    print(url)
    print('protocal = {}' .format(result))
    return result

def host_of_url(url):
    index = url.index('//')
    url


def get(url):

    pass


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'movie.douban.com'
    url = 'http://movie.douban.com/top250'
    port = 80
    s.connect((host, port))
    ip, port = s.getsockname()
    print('this machine ip {} and port  {}'.format(ip, port))


    r = get(url)
    print(r)

if __name__ == '__main__':
    result = protocol_of_url('http://movie.douban.com/top250')
    print('result = {}'.format(result))