from sr.robot import *
from time import sleep
R = Robot.setup()

def move(side,speed):
    backleft=R.motors[0].m1
    backright=R.motors[0].m0
    frontleft=R.motors[1].m1
    frontright=R.motors[1].m0
    if side=='right':
        frontright.power,backright.power,frontleft.power,backleft.power = -speed,-speed,-speed,-speed
    if side=='left':
        frontleft.power,backleft.power,frontright.power,backright.power = speed,speed,speed,speed
    if side=='both':
        backright.power,backright.power,frontleft.power,backleft.power = speed,speed,-speed,-speed
    if side=='none':
        backright.power,backright.power,frontleft.power,backleft.power = 0,0,0,0
#forward = forward('both',75)
#stop = forward('none',0)
