from sr.robot import *
from time import sleep
R = Robot.setup()

angle = 0

class CustomisedRuggeduino(Ruggeduino):
    def ultrasonicSensor(self):
        with self.lock:
            distance = self.command("u")
            print(distance)
            if distance < 10:
                R.power.beep(1000, 'a')    
    def getAngle(self):
        with self.lock:
            gyro = int(round(float(self.command("t").replace('\n', ''))))
            return gyro
            
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

for i in range(0, 500):
  angle += R.ruggeduinos["75230313833351618141"].getAngle()
newAngle = angle/500
print('Done: %d' % (newAngle))
