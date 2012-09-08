#!/usr/bin/python
#!-*- coding:utf-8 -*-

import asynchat
import logging
import socket

class EchoClient(asynchat.async_chat):
    """Sends message to the server and receives respones
    """

    # Artificially reduce buffer sizes to illustrate 
    # sending and receiving partial messages.
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64

    def __init__(self, host, port, message):
        self.message = message
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        return

    def handle_connect(self):
        self.logger.debug('handle_connect()')
        # Send the command
        self.push('ECHO %s\n' % len(self.message))
        # Send the data
        self.push_with_producer(EchoProducer(self.message, buffer_size = self.ac_out_buffer_size))
        # We expect the data to come back as-is
        # so set a length-based terminator
        self.set_terminator(len(self.message))

    def collect_incoming_data(self, data):
        """Reading an incoming message from the client and put it into our outgoing queue"""
        self.logger.debug('collect_incoming _data() -> (%d)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEIVED COPY OF MESSAGE')
        else:
            self.logger.debug('ERROR IN TRANSMISSION ')
            self.logger.debug('EXPECTED "%s"', self.message)
            self.logger.debug('RECEIVED "%s"', self.received_message)
        return

class EchoProducer(asynchat.simple_producer):

    logger = logging.getLogger('EchoProducer')

    def more(self):
        respone = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%d bytes)\n"""%s"""', len(respone), respone)
        return respone


