from sr.robot import *
from time import sleep
R = Robot.setup()
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

def dualMotorTest():
  print('Testing motor[0]:')
  sleep(0.5)
  R.motors[0].m0.power = 100
  R.motors[0].m1.power = 100
  sleep(1.5)
  R.motors[0].m0.power = 0
  R.motors[0].m1.power = 0
  print('Testing motor[1]:')
  sleep(0.5)
  R.motors[1].m0.power = -100
  R.motors[1].m1.power = -100
  sleep(1.5)
  R.motors[1].m0.power = 0
  R.motors[1].m1.power = 0
  sleep(0.5)

while True:
  dualMotorTest()
