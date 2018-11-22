print("Robot online!")
# did the script work?
from sr.robot import *
from time import sleep
R = Robot.setup()
#imports

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("u")
            print "Distance: " + str(distance) + " cm away"
            return distance
        # prints distance away from wherever the camera is pointed

def move(command,speed):
    backleft,backright,frontleft,frontright=R.motors[0].m1,R.motors[0].m0,R.motors[1].m1,R.motors[1].m0 #I put all this on one line like I had below
    if command=='turn': #positive is left, negative is right, zero stops it 
        frontleft.power,backleft.power,frontright.power,backright.power = speed,speed,speed,speed
    if command=='straight':#positive is forward, negative is right, zero is stop
        backright.power,backright.power,frontleft.power,backleft.power = speed,speed,-speed,-speed
    # each of these if statements takes side as an input
    # defined by the while loop below
    # and then adjusts the speed of the motors accordingly

R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

while True:
    distanceAway = int(R.ruggeduinos["75230313833351618141"].ultrasonicSensor())
    print str(distanceAway)
    if distanceAway < 10:
        move('straight',0)
        # stops the robot
    else:
        move('straight',75)
        # moves the robot forward
# todo:
# left/right turns
# adjustable speed, perhaps based on distance
