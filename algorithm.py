#!/usr/bin/env python

#incline[0] = incline of the left line on the origin image
#incline[1] = incline of the right line on the origin image
#incline[2] = incline of the left line on the warped image
#incline[3] = incline of the right line on the warped image

#left_x = left x coordinates on wapred image
#right_x = right x coordinates on wapred image
#left_y = left y coordinates on wapred image
#right_y = right y coordinates on wapred image

#left_or_x = left x coordinates on original image
#right_or_x = right x coordinates on original image
#left_or_y = left y coordinates on original image
#right_or_y = right y coordinates on original image

def algorithm_custom(incline,draw_left,draw_right,left_x,right_x,left_or_x,right_or_x,left_or_y,right_or_y):

#Detection left or right line existance
    left = True
    right = True

    try:
        if (left_x[0] > 180  or incline[0] == 0):
            print('no left')
            left = False
    except:
        print('no left')
        left = False

    try:
        if (right_x[0] < 180 or incline[1] == 0):
            print('no right')
            right = False
    except:
        print('no right')
        right = False
############################################

#start code from here
    steer = 1500 # min : 500 , max : 2500
    speed = 1000 # min : -5000 , max : 5000 , middle : 0

    try:
        mean = (left_or_x[0]+right_or_x[0])/2
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
        if((left_or_y[0]+left_or_y[-1])/2 > 150):
            steer = 1900

        
    elif not left and right:
        if (incline[1] < 0):
            steer = 1900
        steer = 1150
        if (incline[1] < 0.4):
            steer = 1100

    return steer , speed
