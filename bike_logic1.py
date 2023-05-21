#First index is leftmost, second Index is middle left, third index is middle right, and fourth index is right

#Sense the button
from pyfirmata import Arduino
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

# i = 0
# while True:
#     board.digital[i%12+2].write(1)
#     time.sleep(1)
#     board.digital[i%12+2].write(0)
#     time.sleep(1)
#     i += 1

print("Communication Successfully started")

# Create bunch of useful variables
button = board.get_pin('a:1:i')
LED1 = board.digital[9]
LED2 = board.digital[10]
LED3 = board.digital[11]
LED4 = board.digital[12]
LEDs = [LED1, LED2, LED3, LED4] 
LED_index = 0
previous_button_state = 0

# Start iterator to receive input data
it = pyfirmata.util.Iterator(board)
it.start()

# Setup LEDs and button

for LED in LEDs:
    LED.write(0)

while True:
    print(button.read)