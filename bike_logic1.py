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
prev_max_ind = -1

#TURNS EVERYTHING INTO CRIMSON
for i in range(len(LED_pin)):
    board.digital[LED_pin[i][0]].write(1)
while True:
    #Waits for button click
    print(button.read())
    try:
        if button.read() > 0.5:
            tick +=1
    except:
        print("Error")
    
    #Resets number of bikes in each lane
    bike_num = []
    if tick%2 == 1:

        #Creates an array of number of bikes in each lane
        for i in range(3):
            move_servo(i*90)
            x=bikedetector.count_bikes()
            bike_num.append(x)
            print(f"We have {x} bikes in the picture.")
        move_servo(0)
        
        #Finds the maximum index that is not in the previous index array
        max_ind = bike_num.index(max(bike_num))
        if max_ind == prev_max_ind:
            temp_bike_num = bike_num
            temp_bike_num[max_ind] = -1
            max_ind = temp_bike_num.index(max(temp_bike_num))

        #Turns light yellow, then red
        if prev_max_ind>-1:
            board.digital[LED_pin[prev_max_ind][2]].write(0)
            board.digital[LED_pin[prev_max_ind][1]].write(1)
            time.sleep(1)
            board.digital[LED_pin[prev_max_ind][1]].write(0)
            board.digital[LED_pin[prev_max_ind][0]].write(1)

        #Makes current max green 
        board.digital[LED_pin[max_ind][0]].write(0)
        board.digital[LED_pin[max_ind][2]].write(1)
        time.sleep(1)

        prev_max_ind = max_ind
         
    time.sleep(0.01)
