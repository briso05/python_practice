#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

print('Hello python')

print(sys.argv[0])
print("====================")

os.system("pwd")
os.system("ls -l")


print("====================")
result = os.path.exists("/home/pi/pythonPro")
print("exists:",result)

result = os.path.exists("/home/pi/pythonPro/py_default.py")
print("exists:",result)

print("====================")
result = os.path.isdir("/home/pi/pythonPro")
print("isdir:",result)

result = os.path.isfile("/home/pi/pythonPro/py_default.py")
print("isfile:",result)

#https://docs.python.org/





