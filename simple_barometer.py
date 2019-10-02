from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
while True:
pressure = sense.pressure
if pressure >=970 and pressure <991:
print ("Stormy weather")
if pressure >=991 and pressure <1000:
print ("Rain on the way")
if pressure >=1000 and pressure <1020:
print ("Normal")
if pressure >=1020 and pressure <=1031:
print ("Fair")
if pressure >=1031 and pressure <=1060.9:
print ("Very dry")
time.sleep(60)
