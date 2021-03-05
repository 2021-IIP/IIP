#!/usr/bin/env python

#incline[0] = incline of the left line on the origin image
#incline[1] = incline of the right line on the origin image
#incline[2] = incline of the left line on the warped image
#incline[3] = incline of the right line on the warped image

#warpLeft = left x coordinates on wapred image
#warpRight = right x coordinates on wapred image

#originalLeft_x = left x coordinates on original image
#originalRight_x = right x coordinates on original image
#originalLeft_y = left y coordinates on original image
#originalRight_y = right y coordinates on original image

def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y):
    class Point():
        def __init__(self,x,y):
            self.x = x
            self.y = y
    
    leftPoints = list(map(lambda x,y : Point(x,y),(originalLeft_x,originalLeft_y)))
    rightPoints = list(map(lambda x,y : Point(x,y),(originalRight_x,originalRight_y)))

    left = True
    right = True

    try:
        if (warpLeft[0] > 180  or incline[0] == 0):
            print('no left')
            left = False
    except:
        print('no left')
        left = False

    try:
        if (warpRight[0] < 180 or incline[1] == 0):
            print('no right')
            right = False
    except:
        print('no right')
        right = False

#start code from here
    steer = 1500 # min : 500 , max : 2500
    speed = 3000 # min : -5000 , max : 5000 , middle : 0

    try:
        mean = (originalLeft_x[0]+originalRight_x[0])/2
    except:
        pass

    if left and right:
        steer = 1500

        if mean > 185:
            steer = 1900
        if mean < 140:
            steer = 1250
            
    elif left and not right:
        steer = 1800
        if((originalLeft_y[0]+originalLeft_y[-1])/2 > 150):
            steer = 1900

        
    elif not left and right:
        if (incline[1] < 0):
            steer = 1900
        steer = 1150
        if (incline[1] < 0.4):
            steer = 1100

    return steer , speed
