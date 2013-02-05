import time
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, asynchronous, RequestHandler
from multiprocessing.pool import ThreadPool
 

"""
The number of workers in the thread pool will effect
the response rate.
"""
_workers = ThreadPool(40)


 
def run_background(func, callback, args=(), kwds={}):
	def _callback(results):
		IOLoop.instance().add_callback(lambda: callback(*results))
	_workers.apply_async(func, args, kwds, _callback)


# blocking task like querying to MySQL
def blocking_task(n, t):
	time.sleep(n)
	return n, t
 
class LongPoolingHandler(RequestHandler):
	@asynchronous
	def get(self):
		sleepfor, t = int(self.get_argument('sleep',10)), time.time()
		self.write('Waiting for %d seconds...' % sleepfor)
		self.flush()
		run_background(blocking_task, self.on_complete, (sleepfor,t))
 
	def on_complete(self, sleepfor, t):	
		#_workers.apply_async(self.application.librato.send_gauge_value, 
		#	('py-test-gauge', (time.time()-t-float(sleepfor))*100))
		self.write("\n\t%d seconds fin buffer: +%s" % (sleepfor, str(time.time()-t-sleepfor)))
		self.finish()
