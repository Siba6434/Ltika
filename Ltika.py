# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

a = 0.5
COUNT = 10
PIN1 = 17
PIN2 = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)

for _ in xrange(COUNT):
	GPIO.output(PIN1,True)
	time.sleep(a)
	GPIO.output(PIN2,True)
	time.sleep(a)
	GPIO.output(PIN1,False)
	time.sleep(a)
	GPIO.output(PIN2,False)
	time.sleep(a)
	a = a - 0.05

GPIO.cleanup()
