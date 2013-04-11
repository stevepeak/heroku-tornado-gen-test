import tornado.ioloop
import tornado.web
import tornado.httpserver
from genasynchandler import GenAsyncHandler
from longpooling import LongPoolingHandler
import os
import librato

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
		
application = tornado.web.Application([
	(r"/gen-async", GenAsyncHandler),
	(r"/long-pool", LongPoolingHandler),
	(r"/", MainHandler)
])

application.librato = librato.LibratoConnection(os.environ.get('LIBRATO_USER'), os.environ.get('LIBRATO_TOKEN'))

if __name__ == '__main__':
	try:
		http_server = tornado.httpserver.HTTPServer(application)
		http_server.listen(int(os.environ.get('PORT',5000)))
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		tornado.ioloop.IOLoop.instance().stop()
