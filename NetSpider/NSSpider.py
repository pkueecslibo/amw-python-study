import socket
import sys
import time
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
        self.telnetServer = NSServerConsole.TelnetServer(host = '127.0.0.1', port = 30000)
        self.telnetServer.start()
        #asyncore.loop()
        #except Exception, e:
        #    #self.logger.error('initTelnet failed: ', str(e))
        #    print 'initTelnet failed: ', e

    def run(self):
        self.logger.debug('run....')
        while True:
            time.sleep(1)
            self.telnetServer.process()

        

if __name__ == '__main__':
    spider = NSSpider()
    spider.setup()
    spider.run()
