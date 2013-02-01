import tornado.ioloop
import tornado.web
import tornado.httpserver
from genasynchandler import GenAsyncHandler
from longpooling import LongPoolingHandler
import os

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
		
application = tornado.web.Application([
	(r"/gen-async", GenAsyncHandler),
	(r"/long-pool", LongPoolingHandler),
	(r"/", MainHandler)
])

if __name__ == '__main__':
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(int(os.environ.get('PORT',5000)))
	tornado.ioloop.IOLoop.instance().start()
