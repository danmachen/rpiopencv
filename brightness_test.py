#Author: Dan Machen
# Date: 12/02/2017

#Script opens up camera window and scrolls through brightness range

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(100):
	camera.brightness = i
	sleep(0.1)
camera.stop_preview()
