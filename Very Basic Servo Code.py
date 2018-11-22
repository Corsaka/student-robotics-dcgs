from sr.robot import *
from time import sleep
R = Robot()

def servoWiggle():
  R.servos[0][1] = 0 #pos = 0
  R.servos[0][1]=(R.servos[0][1])+5 #turn 5* clockwise (dont turn more than 5* at a time or you'll break the servo) #goes from -100 to 100
