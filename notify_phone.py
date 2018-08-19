#!/usr/bin/python3
from sense_hat import SenseHat
import sqlite3 as lite
import sys
from datetime import datetime, timezone, timedelta

sense = SenseHat()
sense.clear()

#utc + 10
tz = timezone(timedelta(0,0,0,0,0,10))

time = datetime.now(tz)
#print("Logging pressure at %s" % time.time())

pressure = sense.get_pressure()
#print("Pressure millibars/hectopascal: %s" % pressure)

dbase = lite.connect('/home/pi/IOTASS1/data/sensehat.db')
with dbase:
    cur = dbase.cursor()
    cur.execute("INSERT INTO SENSEHAT_data (timestamp, press) VALUES (?,?);", (time, pressure))

dbase.commit()
dbase.close()

#print(pressure)

#def mytestfunc():
#    print("Hello World")
#
#mytestfunc()
