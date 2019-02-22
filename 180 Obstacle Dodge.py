from sr.robot import *
from time import sleep
R = Robot.setup()

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("u")
            print(distance)
            if distance < 10:
                R.power.beep(1000, 'a')    
    def getAngle(self):
        with self.lock:
            return self.command("t")
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

def turnAround(angle, desired):
    R.motors[0].m0.power = 30
    R.motors[0].m1.power = 30
    R.motors[1].m0.power = 30
    R.motors[1].m1.power = 30
    while float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')) <= angle + desired:
     sleep(0.0000000000001)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    R.motors[1].m0.power = 0
    R.motors[1].m1.power = 0
    
def forwards(time):
    R.motors[0].m0.power = -100
    R.motors[0].m1.power = -100
    R.motors[1].m0.power = 100
    R.motors[1].m1.power = 100
    sleep(time)
    
def sentry():
    startAngle = R.ruggeduinos["75230313833351618141"].getAngle()
    startAngle = R.ruggeduinos["75230313833351618141"].getAngle()
    forwards(1)
    startAngle = float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    turnAround(startAngle, 180)
    forwards(1)
    startAngle = float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    turnAround(startAngle, 180)
    
sentry()
