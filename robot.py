print("Robot online!")

from sr.robot import *
from time import sleep
R = Robot.setup()

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("u")
            print "Distance: " + str(distance) + " cm away"
            return distance
 

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

R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

while True:
    distanceAway = int(R.ruggeduinos["75230313833351618141"].ultrasonicSensor())
    print str(distanceAway)
    if distanceAway < 10:
        move('none',0)
    else:
        move('both',75)
