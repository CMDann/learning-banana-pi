import RPi.GPIO as GPIO
import time
import os

# Set up the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

print "l : left"
print "r : right"
print "m : middle"
print "t : test"
print "q : exit"

while True:

	Servo = GPIO.PWM(11, 50)						

	Servo.start(2.5)

	input = raw_input("Selection: ") 
	
	if(input == "t"):
		Servo.ChangeDutyCycle(7.5)
		time.sleep(1)
		Servo.ChangeDutyCycle(12.5)
		time.sleep(1)
		Servo.ChangeDutyCycle(2.5)
		time.sleep(1)
		Servo.stop()

	# right
	if(input == "r"):
	
		steps = raw_input("steps (1 - 10): ") 
		
		stepslength = 12.5 / int(steps)
		
		for Counter in range(int(steps)):
			Servo.ChangeDutyCycle(stepslength * (Counter + 1))
			print stepslength * (Counter + 1)
			time.sleep(0.5)
			
		time.sleep(1)
		Servo.stop()

	elif(input == "m"):
		Servo.start(7.5)
		time.sleep(1)
		Servo.stop()
	
	# move to the left
	elif(input == "l"):
		Servo.start(12.5)
		# how many steps...
		steps = raw_input("steps (1 - 10): ") 
		stepslength = 12.5 / int(steps)
		for Counter in range(int(steps)):
			Servo.ChangeDutyCycle(12.5 - (stepslength * (Counter + 1)))
			time.sleep(0.5)
		
		time.sleep(1)
		Servo.stop()
	
	elif(input == "q"):
		os._exit(1)
		Servo.stop()
		GPIO.cleanup()
		
	else:
		print "Input not recognized"
