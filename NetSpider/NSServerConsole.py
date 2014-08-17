#!/usr/bin/python
# encoding=utf-8

import socket
import asyncore
import threading
import select
from cStringIO import StringIO

from NSLogger import NSLogger

# 负责接受Client socket的连接
class TelnetServer():
	TIMEOUT = 20

	def __init__(self, host, port):
		self.logger = NSLogger.get_logger('NSServerConsole.TelnetServer')
		self.logger.debug('__init__')
		self.host = host
		self.port = port
		self.client_id = 1

	def start(self):
		self.logger.debug('start')
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.try_bind()
			self.sock.listen(5)
		except socket.error as msg:
			self.sock.close()
			self.sock = None

		self.w_socks = []
		self.r_socks = [self.sock]
		self.e_socks = []
		self.connections = {}		

	def stop(self):
		pass	

	def try_bind(self):
		self.logger.debug('try_bind')
		while True:
			try:
				self.sock.bind((self.host, self.port))
				break
			except:
				self.port += 1
				if self.port > 2**16 - 1:
					raise StandardError('TelnetServer failed to find a port to bind')

	def process(self):
		self.logger.debug('process')
		readable , writable , exceptional = select.select(self.r_socks, self.w_socks, self.r_socks,TelnetServer.TIMEOUT)
		if not(readable, writable, exceptional):
			self.logger.debug('超时...')
			return
		for s in readable:
			print 'read s: ', s
			if s is self.sock:
				#主机
				#接受连接
				self.handle_accept()
			else:
				#发来消息
				self.connections[s].handle_read()
		for s in writable:
			print 'write s: ', s.getpeername()
			self.connections[s].handle_write()
		for s in exceptional:
			del self.connections[s]

	def handle_accept(self):
		pair = self.sock.accept()
		if pair is None:
			pass
		else:
			sock, addr = pair
			self.connections[sock] = TelnetConnection(self.client_id, sock)
			self.client_id += 1
			print 'connect from ', sock.getpeername()
			self.connections[sock].send_data('hello')
			#self.logger.debug('connect from %s' % sock.getpeername())

	def when_connect(self, clientid, clientsock):
		self.logger.debug('when_connect')
		return True

	def when_receive(self, clientsock, string):
		self.logger.debug('when_receive')
		print clientsock.clientname
		if string in self.clientnames:
			clientsock.send_data('%s is exited!!!\r\n', string)
		else:
			clientsock.clientname = string
			clientsock.send_data('Hello, %s!!!\r\n' % clientsock.clientname)
		return True


	def when_exit(self, clientsock):
		self.logger.debug('when_exit')
		self._del_client(clientsock)
		return True

	def _del_client(self, clientsock):
		self.logger.debug('_del_client')

	def _add_client(self, clientsock):
		self.logger.debug('_add_client')

class TelnetConnection(object):
	DEFAULT_RECV_BUFFER = 4096

	def __init__(self, clientid, sock):
		self.logger = NSLogger.get_logger('NSServerConsole.TelnetConnection')
		self.logger.debug('__init__')
		self.w_buffer = StringIO()
		self.r_buffer = StringIO()
		self.sock = sock
		self.clientid = clientid
		self.clientname = None


	def handle_read(self):
		self.logger.debug('handle_read')
		data = self.sock.recv(TelnetConnection.DEFAULT_RECV_BUFFER)
		if len(data) > 0:
			print 'recv : ', data

	def handle_write(self):
		self.logger.debug('handle_write')
		buff = self.w_buffer.getvalue()
		if buff:
			sent = self.sock.send(buff)
			self.w_buffer = StringIO()
			self.w_buffer.write(buff[sent:])

	def send_data(self, data):
		self.w_buffer.write(data)

	def test_writable(self):
		return self.w_buffer.getvalue()


