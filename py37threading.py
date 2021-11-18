#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import threading
import time

print('Hello python')

print(sys.argv[0])
print("====================")

class Messenger(threading.Thread):
    def run(self):
        tname = threading.currentThread().getName()

        lst = tname.split()
        print("tname:",lst[0],int(lst[1]),int(lst[2]))
        
        for i in range(int(lst[1]), int(lst[2])):
            print(i, lst[0])
            time.sleep(0.5)

m = Messenger(name="m1 0 10")
#run w/o using thread
#m.run()

#run with using thread
m.start()

#m2 = Messenger(name="m2 100 110")
m2 = Messenger()
m2.setName("m2 100 110")
m2.start()

#to show working Thread
print(threading.enumerate())
# the number of active Thread
print(threading.activeCount())

# which Thread call start()
print(threading.currentThread())

print("End...")
