import tornado.web
import tornado.gen
import tornado.httpclient
import time

class GenAsyncHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.engine
	def get(self):
		s = time.time()
		http_client = tornado.httpclient.AsyncHTTPClient()
		response = yield tornado.gen.Task(http_client.fetch, 
			self.get_argument('uri',"http://example.com"))
		#print response, dir(response)
		#print response.error
		self.finish('Finish here with the data collected.')