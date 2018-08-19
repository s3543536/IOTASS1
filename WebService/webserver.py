#!/usr/bin/env python3
import os, sys
import sqlite3 as lite
import datetime
from flask import Flask, render_template, request, Markup
from sense_hat import SenseHat

app = Flask(__name__)

'''Uncomment if you dont want to see console print out'''
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

@app.route("/testchart")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('testchart.html', values=values, labels=labels)

@app.route("/linechart")
def linechart():
    labels = ["January","February","March","April","May","June","July"]
    values = [10,9,8,7,6,4,7]
    return render_template('pressure_display.html', numsteps=len(labels), maxval=max(values), values=values, labels=labels)

def getHillDecent():
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
    dbase = lite.connect('/home/pi/IOTASS1/data/sensehat.db')
    with dbase:
        cur  = dbase.cursor()
        cur.execute(query, (start, end))
        data = cur.fetchall()

    dbase.close()

    times = [val[0] for val in data]
    pressures = [val[1] for val in data]

    #dictlist = []
    #for time, pressure in data:
    #    dictlist.append({"t": time, "y": pressure})

    return times, pressures
    #return dictlist, times, pressures


@app.route("/mountain_decent")
def mountaindecent():
    times, pressures = getHillDecent()
    return render_template('pressure_display.html', numsteps=len(times), maxval=(max(pressures) + 20), values=pressures, labels=times)

def getData():
    time = datetime.now().strftime("%H:%M:%S")
    sense = SenseHat()
    temp = round(sense.get_temperature(), 1)
    return time, temp

# main route 
@app.route("/currenttemp")
def index():	
	time, temp = getData()
	templateData = {
		'time': time,
		'temp': temp
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host=host, port=80, debug=False)
