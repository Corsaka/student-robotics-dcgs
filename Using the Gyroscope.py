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
               
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

print(getAngle) #Returns the current angle in degrees (nearest integer)
