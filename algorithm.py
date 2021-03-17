#!/usr/bin/env python
class Algorithm():
    def __init__(self, parameter):
        self.parameter = parameter

    def getSumOfY(self,index):
        return self.parameter.originalLeft_y[index] + self.parameter.originalRight_y[index]
    
    def getSumOfX(self,index):
        return self.parameter.originalLeft_x[index] + self.parameter.originalRight_x[index]

    def twoPointIncline(self):
        direction = (self.getSumOfX(0) + self.getSumOfX(-1)) / (self.getSumOfX(0) + self.getSumOfX(-1))
        return 1500 * direction, self.parameter.speed

    def threePointIncline(self):
        direction = (self.getSumOfX(0) + self.getSumOfX(0) + self.getSumOfX(-1)) / (self.getSumOfY(0) + self.getSumOfY(0) + self.getSumOfY(-1))
        return 1500 * direction , self.parameter.speed

    def sumPoint(self):
        right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
        left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
        left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
        right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
        direction = (left_x + right_x) / (left_y + right_y)
        if (self.parameter.incline[0] * self.parameter.incline[1]) > 0:
            self.parameter.speed *= 0.25
        return 1500 * direction , self.parameter.speed
    
    def caseByCase(self):
        right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
        left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
        left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
        right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
        if self.sumPoint()/1500:
            pass
        return 1500 * direction , self.parameter.speed

def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y):
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

    algorithm = Algorithm(Parameter(5000))
    return algorithm.sumPoint()
