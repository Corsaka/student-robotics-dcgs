from sr.robot import *
from time import sleep
R = Robot.setup()

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("u")
            if distance < 10:
                R.power.beep(1000, 'a')
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
ultrasonicSensor() = R.ruggeduinos["75230313833351618141"].ultrasonicSensor()
R.init()
R.wait_start()

ultrasonicSensor()
