#!/usr/bin/python
#!-*- coding:utf-8 -*-

import fileinput
import sys
import time
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# Establish the RSS and channel nodes
rss = Element('rss', {'xmlns:dc':"http://purl.org/dc/elements/1.1", 'version':'2.0',
    })
channel = SubElement(rss, 'channel')
title = SubElement(channel, 'title')
title.text = 'Sample podcast feed'
desc = SubElement(channel, 'description')
desc.text = 'Generated for PyMOTW'
pubdata = SubElement(channel, 'pubdata')
pubdata.text = time.asctime()
gen = SubElement(channel, 'generator')
gen.text = 'http://www.doughellmann/PyMOTW'

for line in fileinput.input(sys.argv[1:]):
    mp3filename = line.strip()
    if not mp3filename or mp3filename.startwith('#'):
        continue
    item = SubElement(rss, 'item')
    title = SubElement(title, 'title')
    title.text = mp3filename
    encl = SubElement(item, 'enclosure', {'type':'auto/mpeg', 'url':mp3filename})

rough_string = tostring(rss)
reparsed = minidom.parseString(rough_string)
print reparsed.toprettyxml(indent=" ")
