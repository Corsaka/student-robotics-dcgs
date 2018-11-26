from sr.robot import *
from time import sleep
import math
R = Robot.setup()

angle = 0
desiredAngle = 0

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("u")
            print(distance)
            if distance < 10:
                R.power.beep(1000, 'a')    
    def getAngle(self):
        with self.lock:
            gyro = int(math.floor(float(self.command("t").replace('\n', ''))))
            return gyro
            
def halfTurn():
    global desiredAngle
    gyro = R.ruggeduinos["75230313833351618141"].getAngle()    
    if gyro != desiredAngle:
        return False
    else:
        return True

def turnAround():
    if not halfTurn():
      R.motors[0].m0.power = 50
      R.motors[0].m1.power = 50
      R.motors[1].m0.power = 50
      R.motors[1].m1.power = 50
      turnAround()
    else:
      R.motors[0].m0.power = 0
      R.motors[0].m1.power = 0
      R.motors[1].m0.power = 0
      R.motors[1].m1.power = 0
      
def movement():
    global angle, desiredAngle
    angle = R.ruggeduinos["75230313833351618141"].getAngle()
    desiredAngle = angle + 180
    R.motors[0].m0.power = 100
    R.motors[0].m1.power = 100
    R.motors[1].m0.power = -100
    R.motors[1].m1.power = -100
    sleep(1.5)
    turnAround()
    angle = R.ruggeduinos["75230313833351618141"].getAngle()
    desiredAngle = angle + 180
    R.motors[0].m0.power = 100
    R.motors[0].m1.power = 100
    R.motors[1].m0.power = -100
    R.motors[1].m1.power = -100
    sleep(1.5)
    turnAround()
    
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

movement()
