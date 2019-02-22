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
R.ruggeduinos["75230313833351618141"].ultrasonicSensor()
R.ruggeduinos["75230313833351618141"].ultrasonicSensor()

while True:
    distance = R.ruggeduinos["75230313833351618141"].ultrasonicSensor()
    if distance < 10:
        print('Too Close!!!')
    sleep(0.5)
    
