#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__=Sam Yong
# 2018/5/12 20：30

from model.user import User

session = {} #session是我们内部用的保留客户端与浏览器一一对应的连接记录


def templeate(name):
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:   # 文本是utf-8
        return f.read()


def route_index(request):
    header = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n'
    body = templeate('index.html')
    response = header + '\r\n' + body
    return response.encode('utf-8')


def route_error(request):
    response = 'HTTP/1.1 404 OK\r\nContent-type: text/html\r\n\r\n <h1>Not Found<h1>'
    return response.encode('utf-8')


def route_static(request):
    filename = request.query.get('file', 'doge.gif')
    path = 'static/' + filename
    with open(path, 'rb') as f:    # 图片直接是b
        header = b'HTTP/1.1 200 OK\r\nContent-type: image/gif\r\n'
        img = header + b'\r\n' + f.read()
        return img


def route_login(request):
    #这里要做一个过滤，如果不是post方法就不处理内容
    header = {
        'Content - type': 'text / html',
    }
    if request.method == 'POST':
        #cookie的作用是可以告诉我们current user是谁



        form = request.form() # form 就是request的body中获得的字典
        print('form = {}'.format(form))
        #那么我们在这里就要处理关于post的表单的内容
        #我们要处理就是要处理user, user是属于数据，都可以用model里面的来用
        u = User.new(form)
        if u.validate_login():
            #如果登录成功我们要发一个session给客户端，用来我们交互的凭证
            session[u.username] = u.username
            header['Set-Cookie'] = 'user={}'.format(u.username)
            result = "login success"
        else:
            result = '登录失败'
    else:
        result = ''

    header_first = 'HTTP/1.1 200 OK\r\n'
    header_second = ''.join(['{}: {}\r\n'.format(k, v)
                                    for k, v in header.items()]) # join就是将列表里面的元素连接成字符串，中间用''隔开
    header = header_first + header_second
    body = templeate('login.html')
    body = body.replace('{{result}}', result)
    response = header + '\r\n' + body
    return response.encode('utf-8')



def route_register(request):
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_register():
            result = '有效数据成功'
            u.save()
        else:
            result = '无效失败'
    else:
        result = ''

    header = "HTTP/1.1 200 OK \r\n Content-type: text/html\r\n"
    body = templeate('register.html')
    print('result = ', result)
    body = body.replace('{{result}}', result)
    response = header + '\r\n' + body
    return response.encode('utf-8')

routes_dict = {
    '/': route_index,
    '/login': route_login,
    '/register' : route_register,
}
