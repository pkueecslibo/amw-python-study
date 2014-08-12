import socket
import sys
from NSLogger import NSLogger

class NSSpider:
    def __init__(self):
        self.logger = NSLogger.get_logger('Spider')

    def setup(self):
        self.logger.debug('debug message')
 

if __name__ == '__main__':
    spider = NSSpider()
    spider.setup()
