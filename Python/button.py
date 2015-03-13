import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# Set pin 21 as the LED
GPIO.setup(21, GPIO.OUT)

# Set up pin 22 as the button
GPIO.setup(22,GPIO.IN)

# Turn on the LED when the button is pressed
while True:
  GPIO.output(21,GPIO.input(22))
  time.sleep(0.05)
