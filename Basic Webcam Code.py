#imports
from sr.robot import *
from time import sleep
R = Robot()

def markerSee():
    markers = R.see() # makes a list of markers it sees
    print("I can see"), len(markers), "markers:" #prints no. of markers
    for m in markers: 
        if m.info.marker_type in (MARKER_TOKEN_A, MARKER_TOKEN_B, MARKER_TOKEN_C):
          print(" - Marker #{0} is {1} metres away".format( m.info.code, m.dist )) #prints what markers are how far away

'''
#####OTHER WEBCAM COMMANDS#####
##These 3 print coordinates of a visiple point, p:
print("length", m.info.code.polar.length)
print("rot_x", m.info.code.polar.rot_x)
print("rot_y", m.info.code.polar.rot_y) 

##Resolution
errormarkers = R.see( res=(1280,1024) ) - chooses resolution of 1280x1024

##Helpful Information
The Logitech C500 has a field of view of 72° and the C270 has a field of view of 60°.

##Other commands aren't explained in use, so will take some figuring out...
'''
