from sr.robot import *
from time import sleep
R = Robot()

R.ruggeduinos["75230313833351618141"].pin_mode(13, OUTPUT) #Sets pin 13 to an output

#Example Function
def ledBlink():
    R.ruggeduinos["75230313833351618141"].digital_write(13, True) #Turns on pin 13
    sleep(1)
    R.ruggeduinos["75230313833351618141"].digital_write(13, False) #Turns off pin 13
    sleep(1)

'''
##Setting up Pins
To set up a pin, you would use this line of code:

R.ruggeduinos["75230313833351618141"].pin_mode(1, INPUT)

R.ruggeduinos["75230313833351618141"] --> This part of the code tells the robot we want to control the ruggeduino with the serial number of 75230313833351618141
pin_mode(1, INPUT) --> This tells the robot we want to set pin 1 of the ruggeduino as an input (ie if we connected it to a sensor)

##Turning on Pins
If we want to turn on a pin, we nee to use a line of code that looks something like this:

R.ruggeduinos["75230313833351618141"].digital_write(1, True)
digital_write(1, True) --> This command tells the robot we want to turn on pin 1 (if we wanted to turn it off, we'd change 'True' to 'False')
'''
