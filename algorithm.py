#!/usr/bin/env python
import math

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

    def getGap(self):
        gap = [0, 0]
        self.parameter.originalRight_x = map(lambda x: (x-160)**2, self.parameter.originalRight_x)
        self.parameter.originalLeft_x = map(lambda x: x**2, self.parameter.originalLeft_x)
        self.parameter.originalLeft_y = map(lambda y: y**2, self.parameter.originalLeft_y)
        self.parameter.originalRight_y = map(lambda y: y**2, self.parameter.originalRight_y)
        gap[1] = map(lambda x,y: math.sqrt(x + y), self.parameter.originalRight_x,self.parameter.originalRight_y)
        gap[0] = map(lambda x,y: math.sqrt(x + y), self.parameter.originalLeft_x,self.parameter.originalLeft_y)
        SUM = [sum(gap[0]), sum(gap[1])]
        gap[0] = map(lambda x: math.sqrt(((x - SUM[0] / len(gap[0])) ** 2) /len(gap[0])), gap[0])
        gap[1] = map(lambda x: math.sqrt(((x - SUM[1] / len(gap[1])) ** 2) /len(gap[1])), gap[1])
        gap[0] = math.sqrt(sum(gap[0])/len(gap[0]))
        gap[1] = math.sqrt((sum(gap[1])-math.sqrt(self.parameter.originalRight_x))/len(gap[1]))
        return gap

    def threePointIncline(self):
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
        
        try:
            if left and right:
                direction = (self.getSliceSumOfX(0,3)+self.getSumOfX(-1)) / (self.getSliceSumOfY(0,3)+self.getSumOfY(-1))
                steer = self.middle * direction
                direction = (direction - 1) * 0.8
                steer += self.middle * direction
                
                #center = ((180-self.parameter.originalLeft_x[0]) + (180+self.parameter.originalRight_x[0]))/4

                #print(center)

                if self.getSumOfX(0)/2 < 150:
                    print("right")
                    steer -= 100

                elif self.getSumOfX(0)/2 > 170:
                    print("left")
                    steer += 100

                if 1100 > steer : steer = 1100
                if 1900 < steer : steer = 1900

            elif left and not right:
                steer = 1700
                if abs((self.parameter.originalLeft_x[0]+self.parameter.originalLeft_x[-1])/(self.parameter.originalLeft_y[0]+self.parameter.originalLeft_y[-1])) < 0.1:
                    steer = 1900
            elif not left and right:
                steer = 1300
                if abs((self.parameter.originalRight_x[0]+self.parameter.originalRight_x[-1]-360)/(self.parameter.originalRight_y[0]+self.parameter.originalRight_y[-1])) < 0.1:
                    steer = 1100
            else:
                steer = 1500
            return steer , self.parameter.speed
        except:
            return 1500 , self.parameter.speed

    def sumPoint(self):
        try:
            right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            steer = 1500
            direction = (left_x + right_x) / (left_y + right_y)
            steer *= direction

            if self.getSumOfX(0) / 2 < 140:
                steer -= 300
            elif self.getSumOfX(0) / 2 > 180:
                steer += 300

            return direction * self.middle, self.parameter.speed
        except ZeroDivisionError:
            return self.middle , self.parameter.speed
    
    def getSumPoint(self):
        try:
            right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            direction = (left_x + right_x) / (left_y + right_y)
            return self.parameter.speed * direction
        except:
            return self.middle , self.parameter.speed
    
    def comedyShow(self):
        try:
            right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            direction = (left_x + right_x) / (left_y + right_y)
            steer = self.middle * direction
            direction = (direction-1) * 0.8
            steer += self.middle * direction
            center = (self.parameter.originalLeft_x[0] - self.parameter.originalRight_x[0])/2

            steer += center*10


            '''if self.getSumOfX(0) / 2 < 140:
                steer -= 300
            elif self.getSumOfX(0) / 2 > 180:
                steer += 300'''
            if 1100 > steer : steer = 1100
            if 1900 < steer : steer = 1900
    
            return steer , self.parameter.speed
        except ZeroDivisionError:
            return self.middle , self.parameter.speed
    
    def fiveStar(self):
        try:
            X = self.getSliceSumOfX(0,4)+self.getSumOfX(-1)
            Y = self.getSliceSumOfY(0,4)+self.getSumOfY(-1)
            direction =  X / Y
            steer = self.middle * direction
            direction = (direction-1) * 0.8
            steer += self.middle * direction
            center = (self.parameter.originalLeft_x[0] - self.parameter.originalRight_x[0])/2

            steer += center*10

            '''if self.getSumOfX(0) / 2 < 140:
                steer -= 300
            elif self.getSumOfX(0) / 2 > 180:
                steer += 300'''
            if 1100 > steer : steer = 1100
            if 1900 < steer : steer = 1900
    
            return steer , self.parameter.speed
        except ZeroDivisionError:
            return self.middle , self.parameter.speed
    
    def inclineControl(self):
        return 1500 - 300 * (self.parameter.incline[0] + self.parameter.incline[1]) , self.parameter.speed

    def withMean_first(self):
        left = True
        right = True

        try:
            if (self.parameter.warpLeft[0] > 180  or self.parameter.incline[0] == 0):
                print('no left')
                left = False
        except:
            print('no left')
            left = False

        try:
            if (self.parameter.warpRight[0] < 180 or self.parameter.incline[1] == 0):
                print('no right')
                right = False
        except:
            print('no right')
            right = False

        #start code from here
        steer = 1500 # min : 500 , max : 2500

        try:
            mean = (self.getSumOfX(0))/2
        except:
            pass

        if left and right:
            steer = 1500
            if mean > 185:
                steer = 1800
            if mean < 140:
                steer = 1200
        elif left and not right:
            steer = 1800
            if (self.parameter.originalLeft_y[0]+self.parameter.originalLeft_y[-1])/2 > 150:
                steer = 1900

        elif not left and right:
            if (self.parameter.incline[1] < 0):
                steer = 1900
            steer = 1150
            if (self.parameter.incline[1] < 0.4):
                steer = 1100

        return steer , self.parameter.speed
    
    def withMean_second(self):
        left = True
        right = True

        try:
            if (self.parameter.warpLeft[0] > 180  or self.parameter.incline[0] == 0):
                print('no left')
                left = False
        except:
            print('no left')
            left = False

        try:
            if (self.parameter.warpRight[0] < 180 or self.parameter.incline[1] == 0):
                print('no right')
                right = False
        except:
            print('no right')
            right = False

        #start code from here
        steer = 1500 # min : 500 , max : 2500

        try:
            mean = (self.getSumOfX(0)+self.getSumOfX(-1))/4
        except:
            pass

        if left and right:
            steer = 1500
            if mean > 185:
                steer = 1800
            if mean < 140:
                steer = 1200
        elif left and not right:
            steer = 1800
            if (self.parameter.originalLeft_y[0]+self.parameter.originalLeft_y[-1])/2 > 150:
                steer = 1900

        elif not left and right:
            if (self.parameter.incline[1] < 0):
                steer = 1900
            steer = 1150
            if (self.parameter.incline[1] < 0.4):
                steer = 1100

        return steer , self.parameter.speed

    def algorithmFromHell(self):
        try:
            right_x = sum(self.parameter.originalRight_x)/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            direction = (left_x + right_x) / (left_y + right_y)
            steer = self.middle * direction
            direction = (direction-1) * 0.8
            steer += self.middle * direction
            center = ((180-self.parameter.originalLeft_x[0]) + (180+self.parameter.originalRight_x[0]))/2

            steer += (320-center)*10
            if 1100 > steer : steer = 1100
            if 1900 < steer : steer = 1900
            print(steer)
    
            return steer , self.parameter.speed
        except ZeroDivisionError:
            return self.middle , self.parameter.speed
    
    def halfLineTracer(self):
        try:
            right_x = (sum(self.parameter.originalRight_x)-160*len(self.parameter.originalRight_x))/len(self.parameter.originalRight_x)
            left_x = sum(self.parameter.originalLeft_x)/len(self.parameter.originalLeft_x)
            left_y = sum(self.parameter.originalLeft_y)/len(self.parameter.originalLeft_y)
            right_y = sum(self.parameter.originalRight_y)/len(self.parameter.originalRight_y)
            leftDirection = left_x / left_y
            rightDirection = right_x / right_y
            steer = 1500
            if abs(leftDirection - rightDirection) < 1:
                steer = 1500
            else:
                steer -= 1000*(leftDirection - rightDirection) + 100
            
            if (originalLeft_y[0]+originalLeft_y[-1])/2 > 150:
                print(steer)

            if 1100 > steer : steer = 1100
            if 1900 < steer : steer = 1900

            return steer , self.parameter.speed
        except ZeroDivisionError:
            return self.middle , self.parameter.speed

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
    #return Algorithm(Parameter(3000)).sumPoint()
    #return Algorithm(Parameter(3000)).comedyShow()
    #return Algorithm(Parameter(3000)).fiveStar()
    return Algorithm(Parameter(2000)).withMean_first()
    #return Algorithm(Parameter(3000)).withMean_second()
    #return Algorithm(Parameter(3000)).halfLineTracer()
    #return Algorithm(Parameter(3000)).algorithmFromHell()
    #return Algorithm(Parameter(1500)).threePointIncline()

'''
def algorithm_custom(incline, draw_left, draw_right, warpLeft, warpRight, originalLeft_x, originalRight_x, originalLeft_y, originalRight_y):
    
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
            steer = 1200
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

    return steer , speed
'''