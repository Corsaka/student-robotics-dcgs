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

while True:
  R.motors[0].m0.power = 50
  sleep(1.5)
  R.motors[0].m0.power = -50
  sleep(1.5)
