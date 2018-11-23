from sr.robot import *
from time import sleep
R = Robot()

#Example Function
def moveForwards():
  R.motors[0].m0.power = 100 #Motor board 0, motor 0, full speed forwards
  R.motors[0].m1.power = 100 #Motor board 0, motor 1, full speed forwards
  R.motors[1].m0.power = 100 #Motor board 1, motor 0, full speed forwards
  R.motors[1].m1.power = 100 #Motor board 1, motor 1, full speed forwards
  sleep(1) #Pauses the program for 1 second
  
'''
##General Use of the Code
This is an example line of code to tell a motor to move forwards at full speed:

R.motors[0].m0.power = 100

R.motors[0] --> This part of the code tells the robot we want to interact with motor board 0
m0 --> This part of the code tells the robot we want to interact with motor 0
power = 100 --> This part of the code tells the robot we want the motor to run at 100% speed

##Moving backwards
If you want to move a robot backwards, simply make the integer negative:

R.motors[0].m0.power = 75 --> This will move the motor FORWARDS at 75% speed
R.motors[0].m0.power = -75 --> This will move the motor BACKWARDS at 75% speed

##Turning
Each motor board controls the motors for a side of the robot: motor board 0 for left, motor board 1 for right.
If you want to turn, you stop the motors on one side moving while keeping the motors on the other side moving forwards.

If you wanted to turn left, turn on the motors on the right side and turn off the motors on the left side:
R.motors[1].m0.power = 100
R.motors[1].m1.power = 100
R.motors[0].m0.power = 0
R.motors[0].m1.power = 0

##Braking
There are two ways to brake which are fairly similar, it comes down to personal preference.

The first way is to set the speed of a motor to 0%:
R.motors[0].m0.power = 0

The second way is to use a separate braking function:
R.motors[0].m0.use_brake= True --> change to 'False' if you want the motor to move again
'''
