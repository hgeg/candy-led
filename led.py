#!/usr/bin/env python
from time import sleep
from threading import Thread

devpath = '/dev/hidraw0'
colors = {}
chsum = lambda b0, b1, b3: (21*b0**2 + 19*b1 - 3*b3) % 255

def turn_on(color='white'): pass

def turn_off():
    turn_on('black')

def blink(color='white',count=1,delay=1.0): pass
