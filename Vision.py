lastx=''
lasty=''
direction=''
from sr.robot import *
R = Robot()
changetogrid={27:'6.y.w',26:'5.y.w',25:'4.y.w',24:'3.y.w',23:'2.y.w',22:'1.y.w',21:'0.y.w',20:'0.x.s',19:'1.x.s',18:'2.x.s',17:'3.x.s',16:'4.x.s',15:'5.x.s',14:'6.x.s',13:'0.y.e',12:'1.y.e',11:'2.y.e',10:'3.y.e',9:'4.y.e',8:'5.y.e',7:'6.y.e',6:'6.x.n',5:'5.x.n',4:'4.x.n',3:'3.x.n',2:'2.x.n',1:'1.x.n',0:'0.x.n'}
corner:{28:'NW',29:'NE',30:'SW',31:'SE'}
'''
while True: # a program that prints no. of markers and their distance away
    markers = R.see() # makes a list of markers it sees
    print("I can see"), len(markers), "markers:" #prints no. of markers
    for m in markers: 
        if m.info.marker_type in (MARKER_TOKEN_A, MARKER_TOKEN_B, MARKER_TOKEN_C):
          print(" - Marker #{0} is {1} metres away".format( m.info.code, m.dist )) #prints what markers are how far away
          if m.info.code > 27:
              print('i see the'+corner[m.info.code]+' corner')
          elif m.info.code < 28:
              print('i see'+ changetogrid[m.info.code])
'''
def findplace():
    markers=R.see()
    shortval=999
    for m in markers:
        if m.info.code < markers:
            shortval=m
    near= changetogrid[markers[shortval].info.code].split('.')
    near.append(markers[shortval].distance)
    direction=near[2]
    if near[1]=y:
        lasty=int(near[0])
        if direction='w':
            lastx=8-int(near[0])
        elif direction='e':
            lastx=int(near[0])
    if near[1]=x:
        lastx=int(near[0])
        if direction='n':
            lasty=8- int(lastx)
        elif direction='s':
            lasty= int(lastx)
    #then make the camera turn and figure out the other coordinate properly*
    #*(it does work out the other co-ordinate somewhat, though not perfectly if not aligned with it, so it needs to turn the camera)
