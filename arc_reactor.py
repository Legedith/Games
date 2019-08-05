from adafruit_circuitplayground.express import cpx
import random
from time import sleep
cpx.pixels.brightness = 0.25
cpx.pixels.fill((0,0,0))
for i in range(2):
    for i in range(10):
        for j in range(5):
            cpx.pixels[i] = (50,50,255)
            sleep(0.01)
            cpx.pixels[i] = (0,0,0)
            sleep(0.01)
            cpx.pixels[i] = (50,50,255)
        sleep(0.15)
    cpx.pixels.fill((0,0,0))

while True:
    cpx.pixels.brightness = 0.25
    for i in range(10):
        cpx.pixels.fill((100-i*5,100-i*5,255-i*10))
        cpx.pixels.brightness = 0.10
        sleep(0.10)



