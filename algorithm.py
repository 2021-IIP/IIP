#!/usr/bin/env python
import math

class Algorithm():
    def __init__(self, parameter):
        self.parameter = parameter

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
    
    def getDistance(self,p1x,p1y,p2x,p2y):
        return math.sqrt((p1x-p2x)**2 + (p1y-p2y)**2)

    def getStandardDeviation(self,x,y):
        gap = [self.getDistance(x[i],y[i],x[i+1],y[i+1]) for i in range(len(y)-1)]
        return math.sqrt(sum([(gap[i]-sum(gap)/len(gap))**2 for i in range(len(gap))]))

    ####################################################################################

    def subSetMiddle(self,left_x,right_x):
        mid = (left_x, right_x)/2 -160
        return 1500 + mid * 5/2

    def sumPoint(self):
        try:
            right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            direction = (left_x + right_x) / (left_y + right_y) * 1500
            direction = max(1100,direction)
            direction = min(1900,direction)

            return direction
        except ZeroDivisionError:
            return 1500
    
    def oneLineSumPoint(self,x,y):
        try:
            direction = sum(x) / sum(y) * 1500
            direction = max(1100,direction)
            direction = min(1900,direction)

            return direction
        except ZeroDivisionError:
            return 1500
    
    def main(self):
        try:
            direction = self.sumPoint()
            if (direction < 1150 and self.parameter.incline[1] != 0) or (direction > 1850 and self.parameter.incline[0] != 0):
                direction = self.subSetMiddle()
            lengthOfLeft = len(self.parameter.originalLeft_x)
            lengthOfRight = len(self.parameter.originalRight_x)
            COUNT = 3
            if lengthOfLeft >= COUNT and lengthOfRight >= COUNT :
                #SD = standard deviation
                leftSD = self.getStandardDeviation(self.parameter.originalLeft_x[:COUNT],self.parameter.originalLeft_y[:COUNT])
                rightSD = self.getStandardDeviation(self.parameter.originalRight_x[:COUNT],self.parameter.originalRight_y[:COUNT])
                gap = leftSD - rightSD
                if self.parameter.incline[0] != 0 and self.parameter.incline[1] != 0:
                    if gap > 50:
                        direction = self.oneLineSumPoint(self.parameter.originRight_x,self.parameter.originRight_y)
                    elif gap < -50:
                        direction = self.oneLineSumPoint(self.parameter.originLeft_x,self.parameter.originLeft_y)
            return direction, self.parameter.speed
        except:
            return 1500, self.parameter.speed

def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y):
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
    
    return Algorithm(Parameter(3000)).sumPoint()
