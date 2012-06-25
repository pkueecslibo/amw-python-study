#!/usr/bin/env python
import os
import sys

#f=raw_input("C/C++ File:");
f = 'test.c'
#out=raw_input("Output file:");
out = 'test'
sys.stdout.write("Trying to Complie C File using gcc...\n");
sys.stdout.write("---------------------------------------------------------\n");
if out=='' or out==None:
    os.system("gcc "+f +" -L/usr/lib/python2.6/config -lpython2.6 -lpthread -lm -ldl -lutil");
else:
    os.system("gcc "+f +" -L/usr/lib/python2.6/config -lpython2.6 -lpthread -lm -ldl -lutil "+"-o "+out);
    
sys.stdout.write("---------------------------------------------------------\n");
sys.stdout.write("Done!\n");
