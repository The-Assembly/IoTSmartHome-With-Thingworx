# Importing all the necessary libraries 
from picamera import PiCamera
import datetime
import time 

camera = PiCamera()

date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

camera.start_preview()
time.sleep(1)
camera.capture('/home/pi/Desktop/microserver/images/camera.jpg')
camera.stop_preview()

print(date)
