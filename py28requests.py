#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import requests
import json
print('Hello python')

print(sys.argv[0])
print("====================")

#shell script : curl
#http://192.168.133.1:8090/sh19json.txt

req = requests.get("http://192.168.133.1:8090/sh19json.txt")

print(req.content)
print("-----------------")

print(str(req.content,'utf-8'))
json_data = json.loads(str(req.content,'utf-8'))
print(json_data)
print(type(json_data))

for key in json_data:
    print(json_data[key])



print("-----------------")
print("====================")
print(req.status_code)
print(req.headers)





