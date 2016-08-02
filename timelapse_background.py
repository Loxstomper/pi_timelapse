# Created by Lochie Ashcroft

from picamera import PiCamera
from os import system
from time import sleep

# Camera Setup
camera = PiCamera()
camera.resolution = (1920, 1080)  # can go more but 1080p is good

# read delay.txt for delay value
delay_config = open("delay.txt", "r")
delay = int(delay_config.read())

i = 0
while True:
    camera.capture('./photos/image{0:05d}.jpg'.format(i))
    i += 1  # because not using a for loop
    sleep(delay)



