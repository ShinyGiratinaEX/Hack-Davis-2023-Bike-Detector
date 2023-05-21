#First index is leftmost, second Index is middle left, third index is middle right, and fourth index is right

#Sense the button
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

i = 0
while True:
    board.digital[i%12+2].write(1)
    time.sleep(1)
    board.digital[i%12+2].write(0)
    time.sleep(1)
    i += 1