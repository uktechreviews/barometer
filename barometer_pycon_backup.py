#Spencer Organ - August 2019

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r=[255,0,0]
wait = 60
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
        sleep(wait)
    sense.clear()