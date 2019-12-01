#!/usr/bin/python

import eventlet
import eventlet.wsgi
import greenlet

class Server(object):
	def __init__(self, app, hostname = "127.0.0.1", port = 0):
		self._pool = eventlet.GreenPool(10)
		self.app = app
		self._sock = eventlet.listen((hostname, port), backlog = 10)
		(self.hostname, self.port) = self._sock.getsockname()
		print "listening on %s: %d" % (self.hostname, self.port)
		print "Upload test"

	def Start(self):
		self._server = eventlet.spawn(eventlet.wsgi.server, self._sock, self.app, protocol = eventlet.wsgi.HttpProtocol, custom_pool=self._pool) 
	
	def Stop(self): 
		if self._server is not None: 
			self._pool.resize(0) 
	
	def Wait(self): 
		try: 
			self._server.wait() 
		except greenlet.GreenletExit: 
			print 'WSGI server has stopped.'
