from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
r=[255,0,0]
wait = 10
sense.clear()

pressure = sense.pressure
print (pressure)