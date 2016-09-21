#! /usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

try:

 GPIO.output(27, GPIO.HIGH)
 while True:
    GPIO.output(22, GPIO.OUT)
    input_state = GPIO.input(18)
    if input_state == False:
       GPIO.output(22, GPIO.HIGH)
       utc_ts = datetime.datetime.utcnow()
       utc_string = utc_ts.strftime('%Y-%m-%d-%H%M%SZ')
       mystring ='raspistill -t 3000 -o /home/pi/pics/IMG-' + utc_string + '.jpg'
       #print(mystring)
       os.system(mystring)
       


finally:
   print('GPIO Cleanup') 
   GPIO.cleanup()