#!/usr/bin/python

import loader
import server

class WSGIService(object):
	def __init__(self, configname, appname):
		self.loader = loader.Loader(configname, appname)
		self.app = self.loader.loadapp_file()
		self.server = server.Server(self.app, "127.0.0.1", 8000)
	
	def Start(self):
		self.server.Start()

	def Wait(self):
		self.server.Wait()

	def Stop(self):
		self.server.Stop()

if __name__ == "__main__":
	configname = "api-paste.ini"
	appname = "main"

	server = WSGIService(configname, appname)
	server.Start()
	server.Wait()
	
	while(1):
		sleep(1)
