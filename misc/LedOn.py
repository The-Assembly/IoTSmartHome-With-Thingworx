import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.OUT) #Set pin 11 to be an output pin and set initial value to low (off)

GPIO.output(11, GPIO.HIGH) # Turn on
print("LED ON")


    
