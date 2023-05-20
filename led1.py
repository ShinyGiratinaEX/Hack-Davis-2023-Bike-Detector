import RPi.GPIO as GPIO
import time

# Define GPIO pins for the traffic light
GREEN_PIN1 = 8
YELLOW_PIN1 = 9
RED_PIN1 = 7

GREEN_PIN2 = 0
YELLOW_PIN2 = 2
RED_PIN2 = 3

GREEN_PIN3 = 12
YELLOW_PIN3 = 13
RED_PIN3 = 14

GREEN_PIN4 = 21
YELLOW_PIN4 = 22
RED_PIN4 = 23

BUTTON_PIN = 24

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN_PIN1, GPIO.OUT)
GPIO.setup(YELLOW_PIN1, GPIO.OUT)
GPIO.setup(RED_PIN1, GPIO.OUT)

GPIO.setup(GREEN_PIN2, GPIO.OUT)
GPIO.setup(YELLOW_PIN2, GPIO.OUT)
GPIO.setup(RED_PIN2, GPIO.OUT)

GPIO.setup(GREEN_PIN3, GPIO.OUT)
GPIO.setup(YELLOW_PIN3, GPIO.OUT)
GPIO.setup(RED_PIN3, GPIO.OUT)

GPIO.setup(GREEN_PIN4, GPIO.OUT)
GPIO.setup(YELLOW_PIN4, GPIO.OUT)
GPIO.setup(RED_PIN4, GPIO.OUT)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to control the traffic light sequence
def traffic_light():
    while running:
        # Traffic Light 1
        GPIO.output(GREEN_PIN1, GPIO.HIGH)
        GPIO.output(YELLOW_PIN1, GPIO.LOW)
        GPIO.output(RED_PIN1, GPIO.LOW)
        time.sleep(5)  # Green light duration

        GPIO.output(GREEN_PIN1, GPIO.LOW)
        GPIO.output(YELLOW_PIN1, GPIO.HIGH)
        time.sleep(2)  # Yellow light duration

        GPIO.output(YELLOW_PIN1, GPIO.LOW)
        GPIO.output(RED_PIN1, GPIO.HIGH)
        time.sleep(5)  # Red light duration

        # Traffic Light 2
        GPIO.output(GREEN_PIN2, GPIO.HIGH)
        GPIO.output(YELLOW_PIN2, GPIO.LOW)
        GPIO.output(RED_PIN2, GPIO.LOW)
        time.sleep(5)  # Green light duration

        GPIO.output(GREEN_PIN2, GPIO.LOW)
        GPIO.output(YELLOW_PIN2, GPIO.HIGH)
        time.sleep(2)  # Yellow light duration

        GPIO.output(YELLOW_PIN2, GPIO.LOW)
        GPIO.output(RED_PIN2, GPIO.HIGH)
        time.sleep(5)  # Red light duration

        # Traffic Light 3
        GPIO.output(GREEN_PIN3, GPIO.HIGH)
        GPIO.output(YELLOW_PIN3, GPIO.LOW)
        GPIO.output(RED_PIN3, GPIO.LOW)
        time.sleep(5)  # Green light duration

        GPIO.output(GREEN_PIN3, GPIO.LOW)
        GPIO.output(YELLOW_PIN3, GPIO.HIGH)
        time.sleep(2)  # Yellow light duration

        GPIO.output(YELLOW_PIN3, GPIO.LOW)
        GPIO.output(RED_PIN3, GPIO.HIGH)
        time.sleep(5)  # Red light duration

        # Traffic Light 4
        GPIO.output(GREEN_PIN4, GPIO.HIGH)
        GPIO.output(YELLOW_PIN4, GPIO.LOW)
        GPIO.output(RED_PIN4, GPIO.LOW)
        time.sleep(5)  # Green light duration

        GPIO.output(GREEN_PIN4, GPIO.LOW)
        GPIO.output(YELLOW_PIN4, GPIO.HIGH)
        time.sleep(2)  # Yellow light duration

        GPIO.output(YELLOW_PIN4, GPIO.LOW)
        GPIO.output(RED_PIN4, GPIO.HIGH)
        time.sleep(5)  # Red light duration

# Start and stop the traffic light sequence based on button press
def button_callback(channel):
    global running
    if running:
        running = False
    else:
        running = True
        traffic_light()

# Add button interrupt for the pushbutton
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)

running = False

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO
    GPIO.cleanup()
