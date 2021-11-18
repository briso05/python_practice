#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
print('Hello python')

print(sys.argv[0])
print("====================")

#subprocess.call("ls -al|more",shell=True)

#subprocess.call("sh py22.sh",shell=True)
#subprocess.call("sh ../shellPro/sh21yad_alert.sh",shell=True)

lst = [11,22,33]
subprocess.call("echo {}".format(lst[0]),shell=True)

lst = ["py22.sh","py_default.py"]
value = "cat {}".format(lst[0])
subprocess.call(value,shell=True)







