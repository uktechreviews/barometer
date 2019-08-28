#Spencer Organ - August 2019

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r=[255,0,0]
g=[0,255,0]
b=[0,0,255]
wait = 30
sense.clear(0,0,0)

while True:
    for c in range (0,8):
        pressure = sense.pressure
        print (pressure)
        graph_pressure = 0
        if pressure >=970 and pressure <991:
            print ("Stormy weather")
            colour = b
            graph_pressure =2
        if pressure >=991 and pressure <999:
            print ("Rain on the way")
            colour = b
            graph_pressure =4
        if pressure >=999 and pressure <1020:
            print ("Normal but it could rain")
            colour = g
            graph_pressure =5
        if pressure >=1020 and pressure <=1031:
            print ("Fair")
            colour = r
            graph_pressure =6
        if pressure >=1031 and pressure <=1060.9:
            print ("Very dry")
            colour = r
            graph_pressure =6
            
        for i in range(graph_pressure):
            sense.set_pixel(c,i,colour)
        sleep(wait)
    sense.clear()
