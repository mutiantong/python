#!/usr/bin/python

from webob.dec import *
from webob import Request, Response
import webob.exc

from routes import Mapper,middleware
import controller

class Router(object):
	def __init__(self):
		self.mapper = Mapper()
		self.add_routes()
		self.router = middleware.RoutesMiddleware(self._dispatch, self.mapper)

	@wsgify
	def __call__(self, req):
		return self.router
	
	def add_routes(self):
		tempController = controller.Controller()

		self.mapper.connect('/instances', controller = tempController, action = 'create', conditions = {'method': ['POST']})
		self.mapper.connect('/instances', controller = tempController, action = 'index', conditions = {'method': ['GET']})
		self.mapper.connect('/instances/{instance_id}', controller = tempController, action = 'show', conditions = {'method': ['GET']})
		self.mapper.connect('/instances/{instance_id}', controller = tempController, action = 'update', conditions = {'method': ['PUT']})
		self.mapper.connect('/instances/{instance_id}', controller = tempController, action = 'delete', conditions = {'method': ['DELETE']})
	
	@staticmethod
	@wsgify
	def _dispatch(req):
		match = req.environ['wsgiorg.routing_args'][1]
		
		if not match:
			return webob.exc.HTTPNotFound()

		app = match['controller']
		return app

def app_factory(global_config, **local_config):
	return Router()
