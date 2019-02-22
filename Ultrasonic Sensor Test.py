from sr.robot import *
from time import sleep
R = Robot.setup()

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("x")
            distance = self.command("x")
            distance = self.command("x")
            return distance  
    def getAngle(self):
        with self.lock:
            return self.command("t")
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

ultrasonicSensor = R.ruggeduinos["75230313833351618141"].ultrasonicSensor()

while True:
    print(ultrasonicSensor)
    sleep(1)
