#!/usr/bin/env python
class Algorithm():
    def __init__(self, parameter):
        self.parameter = parameter

    def getSumOfY(self,index):
        return self.parameter.originalLeft_y[index] + self.parameter.originalRight_y[index]
    
    def getSumOfX(self,index):
        return self.parameter.originalLeft_x[index] + self.parameter.originalRight_x[index]

    def twoPointIncline(self):
        direction = (self.getSumOfY(0) + self.getSumOfY(-1)) / (self.getSumOfX(0) + self.getSumOfX(-1))
        return direction

    def threePointIncline(self):
        direction = (self.getSumOfY(0) + self.getSumOfY(-5) + self.getSumOfY(-1)) / (self.getSumOfX(0) + self.getSumOfY(-5) + self.getSumOfX(-1))
        return direction

    def sumPoint(self):
        direction = (sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y) + sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)) / (sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x) + (sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)))
        return direction
    
    def inclineControl(self):
        left = self.parameter.incline[0]
        right = self.parameter.incline[1]
        if (left * right) < 0:
            return -(left + right)
        else:
            return -(left * right)
    
    def meanTwoPointIncline(self):
        direction = (self.getSumOfY(0) + self.getSumOfY(1)) / (Self.getSumOfX(0) + self.getSumOfX(1))
        return direction

def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y):
    steer = 1500 # min : 500 , max : 2500
    speed = 1500 # min : -5000 , max : 5000 , middle : 0

    class Parameter():
        def __init__(self):
            self.incline = incline
            self.warpLeft = warpLeft
            self.warpRight = warpRight
            self.originalLeft_x = originalLeft_x
            self.originalRight_x = originalRight_x
            self.originalLeft_y = originalLeft_y
            self.originalRight_y = originalRight_y

    parameter = Parameter()
    direction = Algorithm(parameter)

    direction = direction.sumPoint()
    steer = 1500 * direction

    return steer , speed