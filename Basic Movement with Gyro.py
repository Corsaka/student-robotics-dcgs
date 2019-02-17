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

def turnAround(angle):
    while float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')) <= angle + 180:
      R.motors[0].m0.power = 50
      R.motors[0].m1.power = 50
      R.motors[1].m0.power = 50
      R.motors[1].m1.power = 50
  R.motors[0].m0.power = 0
  R.motors[0].m1.power = 0
  R.motors[1].m0.power = 0
  R.motors[1].m1.power = 0
      
def movement():
    R.motors[0].m0.power = -100
    R.motors[0].m1.power = -100
    R.motors[1].m0.power = 100
    R.motors[1].m1.power = 100
    sleep(1)
    try:
        startAngle = float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    except ValueError:
        startAngle = 0.00
    print(startAngle)
    turnAround(startAngle)
    R.motors[0].m0.power = -100
    R.motors[0].m1.power = -100
    R.motors[1].m0.power = 100
    R.motors[1].m1.power = 100
    sleep(1)
    try:
        startAngle = float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    except ValueError:
        startAngle = 0.00
    print(startAngle)
    turnAround(startAngle)
    
movement()
