#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import datetime

print('Hello python')

print(sys.argv[0])
print("====================")
print(time.time())
for i in range(10):
    print(i)
    if i==5 : 
        time.sleep(3)

print("==================")
for i in range(10):
    print(i)
    time.sleep(1)
print("==================")

print(datetime.datetime.now())










