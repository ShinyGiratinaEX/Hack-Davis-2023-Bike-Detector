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
prev_max_ind = []
prev_three = []
prev_one = 0
reset_lights = 0

def turn_yellow_then_red(ind): #From green, initiate stop sequence
    board.digital[LED_pin[ind][2]].write(0)
    board.digital[LED_pin[ind][1]].write(1)
    time.sleep(2)
    board.digital[LED_pin[ind][1]].write(0)
    board.digital[LED_pin[ind][0]].write(1)

def turn_green(ind): #from red, goes to green
    board.digital[LED_pin[ind][0]].write(0)
    board.digital[LED_pin[ind][2]].write(1)


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
        
        if (len(prev_three) == 3):
            prev_three = []
        if (bike_num.index(max(bike_num)) not in prev_three) and (bike_num.index(max(bike_num)) != prev_one):
            turn_yellow_then_red(prev_one)
            turn_green(bike_num.index(max(bike_num)))
            prev_three.append(bike_num.index(max(bike_num)))
            prev_one = bike_num.index(max(bike_num))
        elif (bike_num.index(max([bike_num[i] for i in len(bike_num) if i != bike_num.index(max(bike_num))])) not in prev_three) and (bike_num.index(max([bike_num[i] for i in len(bike_num) if i != bike_num.index(max(bike_num))])) != prev_one):
            turn_yellow_then_red(prev_one)
            turn_green(bike_num.index(max([bike_num[i] for i in len(bike_num) if i != bike_num.index(max(bike_num))])))
            prev_three.append(bike_num.index(max([bike_num[i] for i in len(bike_num) if i != bike_num.index(max(bike_num))])))
            prev_one = bike_num.index(max([bike_num[i] for i in len(bike_num) if i != bike_num.index(max(bike_num))]))
        else:
            turn_yellow_then_red(prev_one)
            turn_green(bike_num.index(min(bike_num)))
            prev_three.append(bike_num.index(min(bike_num)))
            prev_one = bike_num.index(min(bike_num))
            

        #Finds the maximum index that is not in the previous index array

        


        # print(prev_max_ind)
        # for ind in range(len(bike_num)):
        #     if (ind not in prev_max_ind) and (max(bike_num[0:ind+1]) == ind):
        #         max_ind = ind
        #         print(max(bike_num[0:ind+1]))

        # #Turns light yellow, then red
        # if len(prev_max_ind)>0:
        #     board.digital[LED_pin[prev_max_ind[-1]][2]].write(0)
        #     board.digital[LED_pin[prev_max_ind[-1]][1]].write(1)
        #     time.sleep(1)
        #     board.digital[LED_pin[prev_max_ind[-1]][1]].write(0)
        #     board.digital[LED_pin[prev_max_ind[-1]][0]].write(1)
        
        # #Resets prev max ind after 3 rounds
        # if reset_lights%3 == 0 and len(prev_max_ind) >0:
        #     prev_max_ind =[]

        # #Makes current max green 
        # board.digital[LED_pin[max_ind][0]].write(0)
        # board.digital[LED_pin[max_ind][2]].write(1)
        # time.sleep(1)

        # prev_max_ind.append(max_ind)
        # reset_lights +=1
         
    time.sleep(0.01)