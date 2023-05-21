#First index is leftmost, second Index is middle left, third index is middle right, and fourth index is right

#Sense the button
from pyfirmata import Arduino
import pyfirmata
import time
import takepicture 
import bikedetector
""" servo pyfirmata"""

board = pyfirmata.Arduino('COM3')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

#Servo pins
global servo_pin

def move_servo(angle):
    servo_pin.write(angle)

servo_pin = board.get_pin('d:2:s')

#LED Pins
LED_pin = [[3, 4, 5], [6, 7, 8], [9, 10, 11]]

button = board.analog[0]

button.enable_reporting()

#Button pins
button = board.analog[0]

button.enable_reporting()

tick = 0

while True:
    print(tick%2)
    print(button.read())
    try:
        if button.read() > 0.5:
            tick +=1
    except:
        print("Error")
    
    bike_num = []
    if tick%2 == 1:
        for i in range(3):
            move_servo(i*90)
            x=bikedetector.count_bikes()
            bike_num.append(x)
            print(f"We have {x} bikes in the picture.")
        move_servo(0)
        
        max_ind = bike_num.index(max(bike_num))

        max_pins = LED_pin[max_ind]

        for i in max_pins:
            board.digital[i].write(1)
            time.sleep(1)
            board.digital[i].write(0)
            time.sleep(1)
        
    time.sleep(0.01)
