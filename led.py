#!/usr/bin/env python
from time import sleep
from random import randrange as rand
from threading import Thread
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

def blink(color, count=3):
    for i in range(count):
        turn_on(color)
        sleep(0.8)
        turn_off()
        sleep(0.8)
    turn_off()

def gay():
    turn_on()
    sleep(1)
    for d0 in range(10):
        for i,c in enumerate(['red','green','blue','cyan','magenta','yellow']):
            Thread(target=turn_on, args=(c,d0*1.2+i*0.2)).start()
    turn_off(10)

if __name__=='__main__':
    gay()
    blink('red')
    blink('green')
    blink('blue')
