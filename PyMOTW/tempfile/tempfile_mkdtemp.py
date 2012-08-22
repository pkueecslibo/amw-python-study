#!/usr/bin/python

import os
import tempfile

directory_name = tempfile.mkdtemp()
print directory_name
# Clean up the directory yoursef
os.removedirs(directory_name)
