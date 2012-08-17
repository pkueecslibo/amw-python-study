#!/usr/bin/python
#!-*- coding:utf-8 -*-

import sys
import codecs
import SocketServer

class Echo(SocketServer.BaseRequestHandler):

    def handle(self):
        # Get some bytes and echo them back to the client. There 
        # no need to decode them, since they are not used.
        data = self.request.recv(1024)
        self.request.send(data)
        return

class PassThrough(object):

    def __init__(self, other):
        self.other = other
    
    def write(self, data):
        print 'Writing :', repr(data)
        return self.other.write(data)

    def read(self, size=-1):
        print 'Reading :',
        data = self.other.read(size)
        print repr(data)
        return data

    def flush(self):
        return self.other.flush()

    def close(self):
        return self.other.close()

if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0) # Let the kernel give us a port
    server = SocketServer.TCPServer(address, Echo)
    ip, port = server.server_address # Find out what port we were give

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # don't hang on exit
    t.start()

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Wrap the socket with a reader and writer.
    incoming = codecs.getreader('utf-8')(PassThrough(s.makefile('r')))
    outgoing = codecs.getwriter('utf-8')(PassThrough(s.makefile('w')))

    # Send the data
    text = u'pi: π'
    print 'Sending: ', repr(text)
    outgoing.write(text)
    outgoing.flush()

    # Receive a respone
    respone = incoming.read()
    print 'Received: ', repr(respone)

    # Clean up
    s.close()
    server.socket.close()


