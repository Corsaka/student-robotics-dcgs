from sr.robot import *
from time import sleep
R = Robot.setup()

class CustomisedRuggeduino(Ruggeduino):  
    def getAngle(self):
        with self.lock:
            return self.command("t")
            
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()
                   
def turn(angle, desired):
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
  
def backwards(time):
  R.motors[0].m0.power = 100
  R.motors[0].m1.power = 100
  R.motors[1].m0.power = -100
  R.motors[1].m1.power = -100
  sleep(time)

def left(angle):
  R.motors[0].m0.power = 30
  R.motors[0].m1.power = 30
  R.motors[1].m0.power = 30
  R.motors[1].m1.power = 30
  while float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')) <= angle + 90:
     sleep(0.00000000000000001)
  R.motors[0].m0.power = 0
  R.motors[0].m1.power = 0
  R.motors[1].m0.power = 0
  R.motors[1].m1.power = 0
  
def right(angle):
  R.motors[0].m0.power = -30
  R.motors[0].m1.power = -30
  R.motors[1].m0.power = -30
  R.motors[1].m1.power = -30
  while float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')) > angle - 90:
     sleep(0.00000000000000001)
  R.motors[0].m0.power = 0
  R.motors[0].m1.power = 0
  R.motors[1].m0.power = 0
  R.motors[1].m1.power = 0
  
def turnAround(angle):
  R.motors[0].m0.power = 30
  R.motors[0].m1.power = 30
  R.motors[1].m0.power = 30
  R.motors[1].m1.power = 30
  while float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')) <= angle + 180:
     sleep(0.00000000000000001)
  R.motors[0].m0.power = 0
  R.motors[0].m1.power = 0
  R.motors[1].m0.power = 0
  R.motors[1].m1.power = 0     
 
R.ruggeduinos["75230313833351618141"].getAngle()
R.ruggeduinos["75230313833351618141"].getAngle()

forwards(1)
backwards(1)
left(float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')))
right(float(R.ruggeduinos["75230313833351618141"].getAngle().replace('\n', '')))

