#Spencer Organ - August 2019

from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
r=[255,0,0]
sense.clear()

while True:
    for c in range (0,8):
        pressure = sense.pressure
        print (pressure)
        graph_pressure = int(pressure / 150)
        print (graph_pressure)
        for i in range(graph_pressure):
            sense.set_pixel(c,i,r)
        print (c)
        sleep(2)
    sense.clear()