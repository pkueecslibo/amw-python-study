#!/usr/bin/python
#!-*- coding:utf-8 -*-


import sys
import SocketServer

class Echo(SocketServer.BaseRequestHandler):
    
    def handle(self):
        # Get some bytes and echo them back to the client
        data = self.request.recv(1024)
        self.request.send(data)
        return

if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0)# Let the kernel give us a port
    server = SocketServer.TCPServer(address, Echo)
    ip, port = server.server_address # Find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send the data
    text = u'pi: π'
    len_sent = s.send(text)

    # Receive a respone
    respone = s.recv(len_sent)
    print repr(respone)

    #Clean up
    s.close()
    server.socket.close()
