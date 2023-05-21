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

global servo_pin

def move_servo(angle):
    servo_pin.write(angle)

# i = 0
# while True:
#     board.digital[i%12+2].write(1)
#     time.sleep(1)
#     board.digital[i%12+2].write(0)
#     time.sleep(1)
#     i += 1

# # Create bunch of useful variables
button = board.analog[0]

button.enable_reporting()

while True:
    print(button.read())
    try:
        if button.read() > 0.5:
            break
    except:
        print("Error") 

servo_pin = board.get_pin('d:2:s')
move_servo(0)
time.sleep(3)
# for i in range(1,91):
#     move_servo(i)
move_servo(90)
x = bikedetector.count_bikes()
print(f"We have {x} bikes in the picture.")
time.sleep(3)
move_servo(180)
