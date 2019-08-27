#Spencer Organ - August 2019

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r=[255,0,0]
g=[0,255,0]
b=[0,0,255]
wait = 180
sense.clear()

while True:
    for c in range (0,8):
        pressure = sense.pressure
        graph_pressure = int(pressure / 150)
        for i in range(graph_pressure):
            if i<=2:
                colour = b
            if i>2:
                colour = g
            if i>5:
                colour = r
            sense.set_pixel(c,i,colour)
        sleep(wait)
    sense.clear()