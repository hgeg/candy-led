#!/usr/bin/env python
from time import sleep
from random import randrange as rand
import sys

#todo: create a device finder
devpath = '/dev/hidraw0'

colors = {
        'red': 0x01,
        'green': 0x02,
        'blue': 0x03,
        'cyan': 0x06,
        'magenta': 0x05,
        'yellow': 0x04,
        'black': 0x08,
        'white': 0x07
        }

chsum = lambda b0, b1, b3: (21*b0**2 + 19*b1 - 3*b3) % 255

def turn_on(color='white',delay=0.0):
    sleep(delay)
    cmd = bytearray.fromhex('ff'*64)
    cmd[0] = 0x11
    cmd[1] = colors[color]
    cmd[3] = rand(255)
    cmd[2] = chsum(cmd[0], cmd[1], cmd[3])
    with open(devpath, 'wb') as device:
        device.write(str(cmd))

def turn_off(delay=0.0):
    turn_on('black',delay)

def blink(color, count=1, delay=0.4):
    for i in range(count):
        turn_on(color, delay)
        turn_off(delay)
    turn_off()

def gay():
    for i,c in enumerate(['red','green','blue','cyan','magenta','yellow']):
        turn_on(c,0.1)
    turn_off(0.2)

if __name__=='__main__':
    try: 
        col, dur = sys.argv[1:3]
        blink(col,dur)
    except: blink("white")

