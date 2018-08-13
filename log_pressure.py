from sense_hat import SenseHat
import sqlite3 as lite
import sys
from datetime import datetime, timezone, timedelta

sense = SenseHat()
sense.clear()

time = datetime.now(timezone(timedelta(0,0,0,0,0,10)))
print(time.time())
pressure = sense.get_pressure()

dbase = lite.connect('data/sensehat.db')
with dbase:
    cur = dbase.cursor()
    #cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, press NUMERIC)")
    cur.execute("INSERT INTO TABLE SENSEHAT_data(created, press) VALUES (?, ?)",
            (time,
                pressure))

#print(pressure)

#def mytestfunc():
#    print("Hello World")
#
#mytestfunc()
