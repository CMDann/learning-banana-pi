#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#Use BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM,True)
While True:

	GPIO.output(PIN_NUM,True)

	time.sleep(1)
	GPIO.output(PIN_NUM,False)
	time.sleep(1)
