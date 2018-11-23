from sr.robot import *
from time import sleep
R = Robot()

def motorTest():
  print('Testing motor[0].m0:')
  sleep(0.5)
  R.motors[0].m0.power = 100
  sleep(1.5)
  R.motors[0].m0.power = 0
  print('Testing motor[0].m1:')
  sleep(0.5)
  R.motors[0].m1.power = 100
  sleep(1.5)
  R.motors[0].m1.power = 0
  print('Testing motor[1].m0:')
  sleep(0.5)
  R.motors[1].m0.power = 100
  sleep(1.5)
  R.motors[1].m0.power = 0
  print('Testing motor[1].m1:')
  R.motors[1].m1.power = 100
  sleep(1.5)
  R.motors[1].m1.power = 0

while True:
  motorTest()
