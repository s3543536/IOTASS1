#!/usr/bin/python3
import sqlite3 as lite
import sys


dbase = lite.connect('data/sensehat.db')
with dbase:
    cur = dbase.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name VARCHAR(255), addr VARCHAR(20))")

