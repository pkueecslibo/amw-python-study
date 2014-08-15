import socket
import sys
import asyncore
from NSLogger import NSLogger

class NSSpider:
    def __init__(self):
        self.logger = NSLogger.get_logger('NSSpider.NSSpider')


    def setup(self):
        self.logger.debug('debug message')
        self._startTelnetConsole()

    def _startTelnetConsole(self):
        self.logger.debug('_startTelnetConsole')
        #try:
        import NSServerConsole
        self.serverConsole = NSServerConsole.NSServerConsole(ip = '127.0.0.1', port = 30000)
        self.serverConsole.start()
        #asyncore.loop()
        #except Exception, e:
        #    #self.logger.error('initTelnet failed: ', str(e))
        #    print 'initTelnet failed: ', e

    def run(self):
        self.logger.debug('run....')
        while True:
            sleep(1)

        

if __name__ == '__main__':
    spider = NSSpider()
    spider.setup()
