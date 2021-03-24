#!/usr/bin/env python
class Algorithm():
    def __init__(self, parameter):
        self.parameter = parameter
        self.middle = 1500

    def getSumOfY(self,index):
        return self.parameter.originalLeft_y[index] + self.parameter.originalRight_y[index]
    
    def getSliceSumOfY(self,start,end = -1):
        out = 0
        for i in self.parameter.originalLeft_y[start : end] : out += i
        for i in self.parameter.originalRight_y[start : end] : out += i
        return out
    
    def getSumOfX(self,index):
        return self.parameter.originalLeft_x[index] + self.parameter.originalRight_x[index]
    
    def getSliceSumOfX(self,start,end = -1):
        out = 0
        for i in self.parameter.originalLeft_x[start : end] : out += i
        for i in self.parameter.originalRight_x[start : end] : out += i
        return out

    def twoPointIncline(self):
        direction = (self.getSumOfX(0) + self.getSumOfX(-1)) / (self.getSumOfY(0) + self.getSumOfY(-1))
        return self.middle * direction, self.parameter.speed

    def threePointIncline(self):
        try:
            meanIncline = (incline[0] + incline[1])/2
            if -0.2 < meanIncline < 0.2 :
                print("straight")
                direction = self.getSumOfX(0)/ self.getSumOfY(0)
                return self.middle * direction , self.parameter.speed
            elif -3 < meanIncline < 3 :
                print("turn")
                if self.getSumOfX(0)/2 < 180:
                    direction = 0.75
                else:
                    direction = 1.25
                return self.middle * direction , self.parameter.speed
            else:
                print("???")
                return 0 , self.parameter.speed
        except:
            print("?????????????")
            return self.middle , self.parameter.speed

    def sumPoint(self):
        try:
            right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            direction = (left_x + right_x) / (left_y + right_y) * self.middle
            return direction , self.parameter.speed
        except ZeroDivisionError:
            return self.middle , self.parameter.speed
    
    def caseByCase(self):
        left = True
        right = True

        try:
            if (self.parameter.warpLeft[0] > 180  or self.parameter.incline[0] == 0):left = False
        except:
            left = False

        try:
            if (self.parameter.warpRight[0] < 180 or self.parameter.incline[1] == 0):right = False
        except:
            right = False
        
        steer = 1500
        try:
            if (left and right):
                gap = [0,0]
                for l in range(len(self.parameter.originalLeft_y)-1):gap[0] += self.parameter.originalLeft_y[l] - self.parameter.originalLeft_y[l+1]
                for r in range(len(self.parameter.originalRight_y)-1):gap[1] += self.parameter.originalRight_y[r] - self.parameter.originalRight_y[r+1]
                gap[0] /= len(self.parameter.originalLeft_y)-1
                gap[1] /= len(self.parameter.originalRight_y)-1
                steer -= 100*(gap[0]-gap[1])
                print((gap[0]-gap[1])*100)
            elif (not left and right):
                gap = 0
                for r in range(len(self.parameter.originalRight_y)-1):gap[1] += self.parameter.originalRight_y[r] - self.parameter.originalRight_y[r+1]
                gap /= len(self.parameter.originalLeft_y)-1
                print(-gap*100)
                steer -= 100*gap
            elif (left and not right):
                gap = 0
                for l in range(len(self.parameter.originalLeft_y)-1) : gap += self.parameter.originalLeft_y[l] - self.parameter.originalLeft_y[l+1]
                gap /= len(self.parameter.originalLeft_y)-1
                print(gap*100)
                steer += 100*gap
        except:
            pass
        return steer, self.parameter.speed

    
def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y, obstacle_distance):
    steer = 1500 # min : 500 , max : 2500
    # min : -5000 , max : 5000 , middle : 0

    class Parameter():
        def __init__(self,speed):
            self.incline = incline
            self.warpLeft = warpLeft
            self.warpRight = warpRight
            self.originalLeft_x = originalLeft_x
            self.originalRight_x = originalRight_x
            self.originalLeft_y = originalLeft_y
            self.originalRight_y = originalRight_y
            self.speed = speed

    algorithm = Algorithm(Parameter(1000))
    mid = algorithm.caseByCase()
    out = [mid[0],mid[1]]
    if out[0] < 1100 : out[0] = 1100
    if 1900 < out[0] : out[0] = 1900
    if obstacle_distance < 200:
        out[1] = 0

    return out

'''def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y, obstacle_distance):
    class Point():
        def __init__(self,x,y):
            self.x = x
            self.y = y
    
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
    speed = 1500 # min : -5000 , max : 5000 , middle : 0

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
        if (originalLeft_y[0]+originalLeft_y[-1])/2 > 150:
            steer = 1900
        
    elif not left and right:
        if (incline[1] < 0):
            steer = 1900
        steer = 1150
        if (incline[1] < 0.4):
            steer = 1100

    print(incline)
    return steer , speed'''
