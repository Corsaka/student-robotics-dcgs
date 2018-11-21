#imports
from sr.robot import *
from time import sleep
R = Robot()
motor=R.motors[0].m1.power #shortens motors

#servos
R.servos[0][1] = 0 #pos = 0
R.servos[0][1]=(R.servos[0][1])+5 #turn 5* clockwise (dont turn too far or youll break the servo) #goes drom -100 to 100

#motors
motor=R.motors[0].m1.power #shortens that long part so you don't have to rewrite it
motor.power = 100 #motor board 0 channel 1 full forward. works same as servos 
motor.use_brake= False #when true, turns on the brakes
sleep(1) #for pauses when you need them
#print("m0.use_brake = {0}".format(motor.use_brake)) #this is supposed to be printing the braking mode, but it doesn't work

#ruggeduino
# set Ruggeduino board 0's pin 2 to output
R.ruggeduinos[0].pin_mode(2, OUTPUT)
# set Ruggeduino board 0's pin 3 to input
R.ruggeduinos[0].pin_mode(3, INPUT)
# set Ruggeduino board 0's pin 4 to input and enable pull-up resistor
R.ruggeduinos[0].pin_mode(4, INPUT_PULLUP)

#vision
while True: # a program that prints no. of markers and their distance away
    markers = R.see() # makes a list of markers it sees
    print("I can see"), len(markers), "markers:" #prints no. of markers
    for m in markers: 
        if m.info.marker_type in (MARKER_TOKEN_A, MARKER_TOKEN_B, MARKER_TOKEN_C):
          print(" - Marker #{0} is {1} metres away".format( m.info.code, m.dist )) #prints what markers are how far away
#errormarkers = R.see( res=(1280,1024) ) #chooses resolution of 1280x1024
#The Logitech C500 has a field of view of 72° and the C270 has a field of view of 60°.
print("length", m.info.code.polar.length) #these 3 print coordinates of a visiple point, p
print("rot_x", m.info.code.polar.rot_x)
print("rot_y", m.info.code.polar.rot_y) 
#other commands aren't explained in use, so will take some figuring out
