import RPi.GPIO as GPIO
import time


doPin = 5;
GPIO.setmode(GPIO.BOARD);
GPIO.setup(doPin,GPIO.IN);


def main(): 
	value = 0;
	while True: 
		value = GPIO.gpio_function(doPin); 
		print("Input: " ,GPIO.input(doPin), " , Other function: ", value);
		
	

main();
