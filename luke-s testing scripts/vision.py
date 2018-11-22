from sr.robot import *
R = Robot()

while True:
    markers = R.see()
    print "I can see", len(markers), "markers:"
    for m in markers:
        print " - Marker #{0} is {1} metres away".format( m.info.code, m.dist )
