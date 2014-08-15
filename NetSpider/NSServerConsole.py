#!/usr/bin/python
# encoding=utf-8

import socket
import asyncore
import threading
from code import InteractiveConsole
from cStringIO import StringIO

from NSLogger import NSLogger

# 负责接受Client socket的连接
class TelnetServer(asyncore.dispatcher):
	def __init__(self, host, port, accept_handler):
		asyncore.dispatcher.__init__(self)
		self.logger = NSLogger.get_logger('NSServerConsole.TelnetServer')
		self.logger.debug('__init__')
		self.accept_handler = accept_handler
		self.host = host
		self.port = port
		self.client_id = 1

		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.try_bind()
		self.listen(5)

	def try_bind(self):
		self.logger.debug('try_bind')
		while True:
			try:
				self.bind((self.host, self.port))
				break
			except:
				self.port += 1
				if self.port > 2**16 - 1:
					raise StandardError('TelnetServer failed to find a port to bind')

	def handle_accept(self):
		pair = self.accept()
		if pair is None:
			pass
		else:
			sock, addr = pair
			if self.accept_handler(self.client_id, sock):
				self.client_id += 1

	def handle_close(self):
		asyncore.dispatcher.handle_close(self)

	def handle_expt(self):
		asyncore.dispatcher.handle_expt(self)

	def handle_error(self):
		asyncore.dispatcher.handle_error(self)

class TelnetConnection(asyncore.dispatcher):
	DEFAULT_RECV_BUFFER = 4096

	def __init__(self, clientid, sock, encoding, receive_handler, disconnect_handler):
		asyncore.dispatcher.__init__(self, sock)
		self.logger = NSLogger.get_logger('NSServerConsole.TelnetConnection')
		self.logger.debug('__init__')
		self.w_buffer = StringIO()
		self.r_buffer = StringIO()
		self.sock = sock
		self.clientid = clientid
		self.encoding = encoding
		self.receive_handler = receive_handler
		self.disconnect_handler = disconnect_handler
		self.clientname = None


	def handle_read(self):
		self.logger.debug('handle_read')
		data = self.recv(TelnetConnection.DEFAULT_RECV_BUFFER)
		if len(data) > 0:
			print 'recv : ', data

	def handle_write(self):
		buff = self.w_buffer.getvalue()
		if buff:
			sent = self.send(buff)
			self.w_buffer = StringIO()
			self.w_buffer.write(buff[sent:])

	def handle_close(self):
		asyncore.dispatcher.handle_close(self)
		self.disconnect_handler(self)

	def send_data(self, data):
		self.w_buffer.write(data)

	def test_writable(self):
		return self.w_buffer.getvalue()

class TelnetConsole(InteractiveConsole):
	def __init__(self, client, locals = None, filename = "<console>"):
		InteractiveConsole.__init__(self, locals, filename)
		self.logger = NSLogger.get_logger('NSServerConsole.TelnetConsole')

		self.client = client

	def interact(self, banner = None):
		try:
			sys.ps1
		except AttributeError:
			sys.ps1 = '>>> '
		try:
			sys.ps2
		except AttributeError:
			sys.ps2 = '... '
		cprt = 'Type help'
		if banner is None:
			pass
		else:
			pass

	def write(self, data):
		self.logger.debug('write')
		data = data.replace('\r\n', '\n').replace('\n', '\r\n')
		self.client.send_data(data)

class NSServerConsole(object):
	def __init__(self, ip = '127.0.0.1', port = 9113, encoding = 'utf-8'):
		super(NSServerConsole, self).__init__()
		self.logger = NSLogger.get_logger('NSServerConsole.NSServerConsole')

		self.hostname = ip
		self.port = port
		self.encoding = encoding
		self.clients = {}
		self.clientnames = {}
		self.consoles = {}

	def start(self):
		self.logger.debug('start')
		self.telnetServer = TelnetServer(self.hostname, self.port, self.when_connect)

	def stop(self):
		self.logger.debug('stop')
		clients = self.clients.values()
		self.clients = {}
		self.clientnames = {}
		self.consoles = {}

		for client in clients:
			client.close()
		if self.telnetServer is not None:
			self.telnetServer.close()
			self.telnetServer = None

	def when_connect(self, clientid, clientsock):
		self.logger.debug('when_connect')
		con = TelnetConnection(clientid, clientsock, self.encoding, self.when_receive, self.when_exit)
		con.send_data('^] -> set crlf :')
		return True

	def when_receive(self, clientsock, string):
		self.logger.debug('when_receive')
		print clientsock.clientname
		if string in self.clientnames:
			clientsock.send_data('%s is exited!!!\r\n', string)
		else:
			clientsock.clientname = string
			clientsock.send_data('Hello, %s!!!\r\n' % clientsock.clientname)
			self.consoles[clientsock] = TelnetConsole(clientsock)
			self.consoles[clientsock].interact()
			self._add_client(clientsock)
		return True


	def when_exit(self, clientsock):
		self.logger.debug('when_exit')
		self._del_client(clientsock)
		return True

	def _del_client(self, clientsock):
		self.logger.debug('_del_client')
		del self.clients[clientsock.client_id]
		del self.clientnames[clientsock.clientname]
		del self.consoles[clientsock]

	def _add_client(self, clientsock):
		self.logger.debug('_add_client')
		self.clients[clientsock.client_id] = clientsock
		self.clientnames[clientsock.clientname] = clientsock.client_id
