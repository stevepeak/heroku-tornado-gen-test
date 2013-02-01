import tornado.ioloop
import tornado.web

from genasynchandler import GenAsyncHandler
from longpooling import LongPoolingHandler

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
	

application = tornado.web.Application([
    (r"/gen-async", GenAsyncHandler),
    (r"/long-pool", LongPoolingHandler),
    (r"/", MainHandler)
])
 
if __name__ == "__main__":
    application.listen(int(os.environ.get('PORT', 5000)))
    tornado.ioloop.IOLoop.instance().start()