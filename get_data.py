#!/usr/bin/env python3
import os, sys
import sqlite3 as lite
import datetime
#from datetime import datetime


def main():
    data = []
    query = """
    SELECT timestamp, press
    FROM SENSEHAT_data
    WHERE timestamp BETWEEN ? AND ?
    ORDER BY timestamp;
    """
    
    tz = datetime.timezone(datetime.timedelta(0,0,0,0,0,10))


    start = datetime.datetime(2018,8,17,14,0,0,0,tz)
    end = datetime.datetime(2018,8,17,20,0,0,0,tz)
    print("start: %s" % start)
    print("end: %s" % end)
    dbase = lite.connect('/home/pi/IOTASS1/data/sensehat.db')
    with dbase:
        cur  = dbase.cursor()
        cur.execute(query, (start, end))
        data = cur.fetchall()

    dbase.close()

    print(data)

    print("times: %s" % [val[0] for val in data])


main()
