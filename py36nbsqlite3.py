#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sqlite3

print('Hello python')

print(sys.argv[0])
print("====================")

conn = sqlite3.connect("py36notebook.db")

sql_create_table = '''
create table if not exists notebook(
num integer primary key autoincrement,
model text,
price integer,
color text)
'''

conn.execute(sql_create_table)
