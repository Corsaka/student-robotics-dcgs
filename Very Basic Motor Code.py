from sr.robot import *
from time import sleep
R = Robot()
motor = R.motors[0].m1.power #shortens motors

def motorMove():
  motor.power = 100 #motor board 0 channel 1 full forward. works same as servos 
  motor.use_brake= False #when true, turns on the brakes
  sleep(1) #for pauses when you need them
