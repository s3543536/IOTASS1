#!/usr/bin/env python3
import bluetooth
import os
import time
from sense_hat import SenseHat
import sqlite3 as lite

# Main function
def main():

    loop = True
    while(loop):
        loop = False

        user_name = input("Enter your name (or blank to go straight to search): ")
        device_name = input("Enter the name of your phone (likewise): ")

        if(user_name != "" and device_name != ""):
            dbase = lite.connect('/home/pi/IOTASS1/data/sensehat.db')
            with dbase:
                cur = dbase.cursor()
                cur.execute("SELECT * FROM users WHERE name = ?;", (user_name,))
                temp = cur.fetchall()
                if(len(temp) == 0):
                    cur.execute("INSERT INTO users (name, phone_name) VALUES (?,?);", (user_name, device_name))
                    dbase.commit()
                else:
                    print("User with that name already exists")
                    loop = True

            dbase.close()

    search()

def getUsers():
    dbase = lite.connect('/home/pi/IOTASS1/data/sensehat.db')
    users = []
    with dbase:
        cur = dbase.cursor()
        cur.execute("SELECT name, phone_name FROM users;")
        users = cur.fetchall()
    dbase.close()

    return users

# Search for device based on device's name
def search():
    users = getUsers()
    current_name = ""
    current_dev_name = ""

    while True:
        device_address = None
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()

        for mac_address in nearby_devices:
            for name, device_name in users:
                if device_name == bluetooth.lookup_name(mac_address, timeout=5):
                    current_name = name
                    current_dev_name = device_name
                    device_address = mac_address
                    break
        if device_address is not None:
            sense = SenseHat()
            temp = round(sense.get_temperature(), 1)
            sense.show_message("Hi {}! Current Temp is {}*c".format(current_name, temp), scroll_speed=0.05)
            print("Hi {}! Your phone ({}) has the MAC address: {}".format(current_name, current_dev_name, device_address))
            print("Hi {}! Current Temp is {}*c".format(current_name, temp))
        else:
            print("Could not find any registered devices nearby...")

#Execute program
main()
