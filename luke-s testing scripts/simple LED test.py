#imports
from sr.robot import *
from time import sleep
R = Robot()

R.ruggeduinos["75230313833351618141"].pin_mode(13, OUTPUT)

while True:
    R.ruggeduinos["75230313833351618141"].digital_write(13, True)
    sleep(1)
    R.ruggeduinos["75230313833351618141"].digital_write(13, False)
    sleep(1)
