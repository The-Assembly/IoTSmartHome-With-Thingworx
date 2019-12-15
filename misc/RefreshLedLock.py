import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN) 
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
servoPIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)

#while True:
if GPIO.input(11) == False and GPIO.input(12) == False:
    print "1"
    GPIO.output(11,GPIO.LOW)
    sleep(0.5)
    p.start(2.5)
    GPIO.output(12,GPIO.LOW)
    sleep(0.5)
    p.stop()

elif GPIO.input(11) == True and GPIO.input(12) == False:
    print "2"
    GPIO.output(11,GPIO.HIGH)
    sleep(0.5)
    p.start(2.5)
    GPIO.output(12,GPIO.LOW)
    sleep(0.5)
    p.stop()

elif GPIO.input(11) == False and GPIO.input(12) == True:
    print "3"
    GPIO.output(11,GPIO.LOW)
    sleep(0.5)
    p.start(10)
    GPIO.output(12,GPIO.HIGH)
    sleep(0.5)
    p.stop()

elif GPIO.input(11) == True and GPIO.input(12) == True:
    print "4"
    GPIO.output(11,GPIO.HIGH)
    sleep(0.5)
    p.start(10)
    GPIO.output(12,GPIO.HIGH)
    sleep(0.5)
    p.stop()
   
