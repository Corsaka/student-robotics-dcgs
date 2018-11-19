print("Hello World!")
#imports
from sr.robot import *
from time import sleep
R = Robot()

while True:
 #   R.servos["sr0VY24"][0] = 0
  #  for i in range(19):
   #     R.servos["sr0VY24"][0] = (R.servos["sr0VY24"][0])+5
#        sleep(0.05)
 #   for i in range(19):
  #      R.servos["sr0VY24"][0] = (R.servos["sr0VY24"][0])-5
   #     sleep(0.05)
    markers = R.see(res=(1280,720)) # makes a list of markers it sees
    print("I can see"), len(markers), "markers:" #prints no. of markers
    for m in markers: 
        if m.info.marker_type in (MARKER_TOKEN_A, MARKER_TOKEN_B, MARKER_TOKEN_C):
          print(" - Marker #{0} is {1} metres away".format( m.info.code, m.dist )) #prints what markers are how far away
