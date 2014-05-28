import socket
import sys

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port


class Spider:
    def __init__(self):
        self.sock = None

    def setup(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print 'Socket created'
        try:
            self.sock.bind((HOST, PORT))
        except socket.error , msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

        print 'Socket bind complete'

        self.sock.listen(10)    
        print 'Socket now listening'
        self.sock.setblocking(0)
    
    def run(self):
        read_list = [self.sock]
        while True:
            print 'ready to accept...'
            readable, writable, errored = self.sock.select(read_list, [], [])

            for s in readable:
                #display client information 
                print 'Connected with ' + addr[0] + ':' + str(addr[1])

if __name__ == '__main__':
    spider = Spider()
    spider.setup()
    spider.run()
