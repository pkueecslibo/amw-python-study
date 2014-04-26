#!/usr/bin/python

import logging
import Queue
import threading

class AsyncQueue(Queue.Queue):
	def __init__(self):
		Queue.Queue.__init__(self)

	def put(self, func, callback, *args, **kwargs):
		Queue.Queue.put(self, {
				 "function" : func, 
				 "callback" : callback,
				 "args" : args,
				 "kwargs" :kwargs}, 
				 True, 1)
		print Queue.Queue.qsize(self)

	def _task_queue_consumer(self):
		while True:
			try:
				task = Queue.Queue.get(self)
				function = task.get("function")
				callback = task.get("callback")
				args = task.get("args")
				kwargs = task.get("kwargs")
				try:
					if callback:
						callback(function(*args, **kwargs))
				except Exception as ex:
					if callback:
						callback(ex)
				finally:
					Queue.Queue.task_done(self)
			except Exception as ex:
				logging.warning(ex)

def func_1(a, b):
	return a + b

def func_2():
	print 'just print'

def handle_result(result):
	print type(result), result

if __name__ == "__main__":

	q = AsyncQueue()
	q.put(func_1, handle_result, 1, 2)
	q.put(func_2, handle_result)


	t = threading.Thread(target = q._task_queue_consumer)
	t.daemon = True
	t.start()