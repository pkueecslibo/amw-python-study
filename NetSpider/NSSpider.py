import socket
import sys
from NSLogger import NSLogger

class NSSpider:
    def __init__(self):
        self.logger = NSLogger.get_logger('Spider')

        self.initTelnet()

    def setup(self):
        self.logger.debug('debug message')

    def initTelnet(self):
        #try:
        import NSServerConsole
        self.serverConsole = NSServerConsole.NSServerConsole(ip = '127.0.0.1', port = 30000)
        self.serverConsole.start()
        #except Exception, e:
        #    #self.logger.error('initTelnet failed: ', str(e))
        #    print 'initTelnet failed: ', e

if __name__ == '__main__':
    spider = NSSpider()
    spider.setup()
