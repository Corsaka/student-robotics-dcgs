from sr.robot import *
from time import sleep
R = Robot.setup()
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

while True:
  R.motors[0].m1.power = 50
  sleep(1.5)
  R.motors[0].m1.power = -50
  sleep(1.5)
