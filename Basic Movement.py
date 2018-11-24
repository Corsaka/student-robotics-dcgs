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
    def gyroTurn(self):
        with self.lock:
            gyro = self.command("t")
            print(gyro)
                
R.ruggeduino_set_handler_by_fwver("SRcustom", CustomisedRuggeduino)
R.init()
R.wait_start()

def basicMovement():
  R.motors[0].m0.power = 100
  R.motors[0].m1.power = 100
  R.motors[1].m0.power = -100
  R.motors[1].m1.power = -100
  sleep(1)
  gyroTurn()

while True:
  basicMovement()
