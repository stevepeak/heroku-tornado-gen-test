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

application.librato = librato.LibratoConnection('app11478021@heroku.com', 'be8a47364abd1c426a83628fb8b37cef6efc78abf00afd98692176812ed3e171')

if __name__ == '__main__':
	print """
python-sample

http://localhost:5000/
	gen-async
		?uri=<http://example.com>
	long-pool
		?sleep=<10>
	"""
	try:
		http_server = tornado.httpserver.HTTPServer(application)
		http_server.listen(int(os.environ.get('PORT',5000)))
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		tornado.ioloop.IOLoop.instance().stop()
