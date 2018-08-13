#!/usr/bin/python3
import sqlite3 as lite
import sys


dbase = lite.connect('data/sensehat.db')
with dbase:
    cur = dbase.cursor()
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(id INTEGER PRIMARY KEY, timestamp DATETIME, press NUMERIC)")
    #cur.execute("CREATE TABLE SENSEHAT_data(created timestamp, press NUMERIC)")
    #cur.execute("CREATE TABLE SENSEHAT_data(created timestamp, press REAL)")

