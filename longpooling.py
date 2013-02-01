from time import sleep
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, asynchronous, RequestHandler
from multiprocessing.pool import ThreadPool
 
_workers = ThreadPool(10)
 
def run_background(func, callback, args=(), kwds={}):
	def _callback(result):
		IOLoop.instance().add_callback(lambda: callback(result))
	_workers.apply_async(func, args, kwds, _callback)
 
# blocking task like querying to MySQL
def blocking_task(n):
	sleep(n)
	return n
 
class LongPoolingHandler(RequestHandler):
	@asynchronous
	def get(self):
		run_background(blocking_task, self.on_complete, (int(self.get_argument('sleep',10)),)
 
	def on_complete(self, res):
		self.write("Test for sleeping {0} seconds finished.<br/>".format(res))
		self.finish()