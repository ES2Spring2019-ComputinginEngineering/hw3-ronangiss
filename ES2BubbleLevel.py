from microbit import *
import math


def tilt(xTilt, yTilt, zTilt):
    ydegrees = int(math.atan2(yTilt, math.sqrt((xTilt**2) + (zTilt**2)))*(180/math.pi))
    xdegrees = int(math.atan2(xTilt, math.sqrt((yTilt**2) + (zTilt**2)))*(180/math.pi))
    sleep(50)
    return xdegrees, ydegrees

def arrows(xdeg, ydeg):
    print((xdeg,ydeg))  #used to identify xdeg and ydeg on a running basis,
                        #allowing me to come up with the inequalities for the conditionals
    if (-90 < xdeg < -5):
        if (40 > ydeg > 5):
            display.show(Image.ARROW_SW)
        elif (-40 < ydeg < -5):
            display.show(Image.ARROW_NW)
        else:
            display.show(Image.ARROW_W)
    elif (10 < xdeg < 90):
        if (40 >ydeg > 5):
            display.show(Image.ARROW_SE)
        elif (-40 < ydeg < -5):
            display.show(Image.ARROW_NE)
        else:
            display.show(Image.ARROW_E)
    elif (5 < ydeg < 90):
        display.show(Image.ARROW_S)
    elif (-90 < ydeg < -5):
        display.show(Image.ARROW_N)
    else:
        display.show(Image.HEART)

while(True):
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    arrows(tilt(x, y, z)[0], tilt(x, y, z)[1])