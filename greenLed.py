import RPi.GPIO as GPIO
import time

# Define GPIO pins for the traffic light
GREEN_PIN1 = 8
GREEN_PIN2 = 9
GREEN_PIN3 = 7

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN_PIN1, GPIO.OUT)
GPIO.setup(GREEN_PIN2, GPIO.OUT)
GPIO.setup(GREEN_PIN3, GPIO.OUT)

# Function to control the traffic light sequence
def traffic_light():
    while running:
        # Traffic Light 
        GPIO.output(GREEN_PIN1, GPIO.HIGH)
        time.sleep(5)  # Green light duration

        GPIO.output(GREEN_PIN1, GPIO.LOW)
        GPIO.output(GREEN_PIN2, GPIO.HIGH)
        time.sleep(2)  # Yellow light duration

        GPIO.output(GREEN_PIN2, GPIO.LOW)
        GPIO.output(GREEN_PIN3, GPIO.HIGH)
        time.sleep(5)  # Red light duration

