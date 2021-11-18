#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import threading
import time

print('Hello python')

print(sys.argv[0])
print("====================")

def test():
    print(threading.currentThread().getName())
    print(threading.enumerate())
    for i in range(10):
        print(i)
        time.sleep(0.3)

#test()

#run only test() using Thread
threading.Thread(target=test).start()

print("====================")

def test2(x,y):
    for i in range(x,y):
        print(i)
        time.sleep(0.3)

threading.Thread(target=test2,args=(100,110)).start()

print("====================")
print("End...")
