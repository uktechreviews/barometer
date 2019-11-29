#!/bin/python3

from sense_hat import *
from time import sleep

sense = SenseHat()
sense.clear()

while True:
    bearing = sense.get_compass()
    print (bearing)
    if bearing >= 355 or bearing <=5:
        sense.clear(0,255,0)
    else:
        sense.clear(255,0,0)