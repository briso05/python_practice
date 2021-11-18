#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sqlite3
print('Hello python')

print(sys.argv[0])
print("====================")
#sudo apt install -y sqlite3

#1.connection 
conn = sqlite3.connect("py34test.db")

#to confirm that there is any table
#ls
#sqlite3 py34test.db ".tables"

#2. create table
sql_create_table = '''
create table if not exists test(
num integer primary key autoincrement,
fname text,
lname text)
'''

conn.execute(sql_create_table)


#3. insert
def insert():
    sql_insert = '''
    insert into test(fname, lname) values(?,?)
    '''

    #data -> tuple type
    values = ('Gildong', 'Hong')
    conn.execute(sql_insert,values)

    #it doesn't support auto commit, so you must commit after execute sql query
    conn.commit()
#insert()

#4.selectAll
def selectAll():
    print("====selectAll======")
    sql_selectAll = '''
    select * from test order by num desc
    '''

    cursor = conn.execute(sql_selectAll)
    rows = cursor.fetchall()

    print("len(rows):",len(rows))

    for row in rows:
        #print(row)
        for data in row:
            print(data,end=" ")
        print()
selectAll()


#5. selectOne
def selectOne():
    print("====selectOne======")

    num = "2"
    num = [2]
    num = list(("2"))
    sql_selectOne = '''
    select * from test where num = ?
    '''

    cursor = conn.execute(sql_selectOne, num)
    rows = cursor.fetchall()

    print("selectOne len(rows):",len(rows))
    for row in rows:
        #print(row)
        for data in row:
            print(data,end=" ")
        print()
    
selectOne()

#6. update
def update():
    print("====update======")
    sql_update = '''
    update test set fname = ?, lname = ? where num = ?
    '''
    values = ("SoonShin", "Lee", 2)

    conn.execute(sql_update, values)
    conn.commit()
    print("updateOk")
    selectAll()

#update()


#7. delete
def delete():
    print("====delete======")
    sql_delete = '''
    delete from test where num = ?
    '''
    num = [1]

    conn.execute(sql_delete, num)
    conn.commit()

    print("deleteOK")
    selectAll()

#delete()
