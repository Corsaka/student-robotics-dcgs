from sr.robot import *
from time import sleep
R = Robot.setup()

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            return self.command("x")  
    def getAngle(self):
        with self.lock:
            return self.command("t")
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

while True:
    print(R.ruggeduinos["75230313833351618141"].ultrasonicSensor())
    sleep(1)
