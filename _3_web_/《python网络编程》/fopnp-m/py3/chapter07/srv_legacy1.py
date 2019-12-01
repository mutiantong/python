#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/srv_legacy1.py
# Uses the legacy "socketserver" Standard Library module to write a server.

from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
import zen_utils

class ZenHandler(BaseRequestHandler):
    def handle(self): # 特定客户端会话的handle
        zen_utils.handle_conversation(self.request, self.client_address)

class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1 # 打开套接字，并接受连接
    # address_family = socket.AF_INET6  # uncomment if you need IPv6

if __name__ == '__main__':
    address = zen_utils.parse_command_line('legacy "SocketServer" server')
    server = ZenServer(address, ZenHandler)
    server.serve_forever()
# 最好限制最终线程的数量，否则容易被攻击者得手