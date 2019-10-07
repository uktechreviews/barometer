#!/bin/python3

from sense_hat import *
from time import sleep

sense = SenseHat()
sense.clear()

while True:
    bearing = sense.get_compass()
    if bearing >= 355 or bearing <=5:
        print ("N")
    if bearing >=40 and bearing <=50:
        print ("NE")
    if bearing >=85 and bearing <=95:
        print ("E")
    if bearing >=130 and bearing <=140:
        print ("SE")
    if bearing >=175 and bearing <=185:
        print ("S")
    if bearing >=220 and bearing <=230:
        print ("SW")
    if bearing >=265 and bearing <=275:
        print ("W")
    if bearing >=310 and bearing <=320:
        print ("NW")