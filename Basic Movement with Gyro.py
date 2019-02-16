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

def halfTurn(startAngle):
    try:
        newAngle = float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    except ValueError:
        newAngle = float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    if newAngle >= startAngle + 180 or newAngle <= startAngle - 180:
        return True
        print(newAngle)
    else:
        return False

def turnAround(angle):
    if not halfTurn(angle):
      R.motors[0].m0.power = 50
      R.motors[0].m1.power = 50
      R.motors[1].m0.power = 50
      R.motors[1].m1.power = 50
      turnAround(angle)
    else:
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
        startAngle = int(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
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
        startAngle = int(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', ''))
    print(startAngle)
    turnAround(startAngle)
    
movement()
