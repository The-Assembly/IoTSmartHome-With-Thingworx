import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
servoPIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

p.start(2.5)
print("Door Close")
GPIO.output(12,GPIO.LOW)

sleep(1)
p.stop()
