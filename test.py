from sense_hat import SenseHat
import sqlite3 as lite
import sys

sense = SenseHat()
sense.clear()

dbase = lite.connect('data/sensehat.db')
with dbase:
    cur = dbase.cursor()
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC)")

pressure = sense.get_pressure()
print(pressure)

#def mytestfunc():
#    print("Hello World")
#
#mytestfunc()
