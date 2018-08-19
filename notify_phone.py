#!/usr/bin/python3
from sense_hat import SenseHat
import sys
import requests
import json
import os


def main():
    sense = SenseHat()
    sense.clear()
    temp = round(sense.get_temperature(), 1)

    if(temp < 15):
        #ip_address = os.popen('hostname -I').read()
        send_notification_via_pushbullet("Temperature: %d" % temp, "From Raspberry Pi")


def getKey(location):
    apifile = open(location, "r")
    key = apifile.read()
    apifile.close()

    return key


ACCESS_TOKEN = getKey('/home/pi/IOTASS1/api.key')

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#Execute
main()

