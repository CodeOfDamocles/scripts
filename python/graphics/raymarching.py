from math import sqrt, cos, sin, radians
import pygame
import pygame.gfxdraw
import time
import random

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

class Circle:
    def __init__(self):
        self.x = int(random.random() * 500)
        self.y = int(random.random() * 500)
        self.radius = int(random.random()*50)

    def pos(self):
        return [self.x, self.y]

    def draw(self,pygame, window):
        pygame.gfxdraw.circle(w, self.pos()[0], self.pos()[1], self.radius, (25,222,2))

# return the distance from a point to a circle minus the circle radius
def getDistanceToCircle(point, center, radius):
    
    vc = []
    vc.append(center.pos()[0] - point[0])
    vc.append(center.pos()[1] - point[1])
    
    return length(vc) - radius

def smallestDistanceToCircle(p, circles):
    
    distanceToObject = 500
    mindistance = 0.1 # the minimum distance to check
    
    for circle in circles:
        
        # calculate distance to circle
        distanceToCircle = getDistanceToCircle(p, circle, circle.radius)
        
        # get smaller distance
        distanceToObject = min(distanceToCircle, distanceToObject)
        
        # if minimum distance found return it
        if distanceToObject <= mindistance:
            return distanceToObject

    return distanceToObject


def moveVectorAlongRay(origin,direction,speed):
    # march the point forward by the size returned by
    # the smallest distance
    v1=origin[0] + direction[0] * speed
    v2=origin[1] + direction[1] * speed
    return [v1,v2]

w = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('Ray marching')

p1 = [10,10]
direction = [p1[0] / length(p1), p1[1] / length(p1)]

def drawRay(p1,po,smallest):
    # draw line from origin to current position
    # draw circle showing the distance to the closest circle using the radius
    # draw a circle with radius of one showing the current position of the vector
    pygame.draw.line(w,(25,55,255), p1, po)  
    pygame.gfxdraw.circle(w,  int(p1[0]), int(p1[1]), int(smallest)+1, (255,255,255))
    pygame.gfxdraw.circle(w,  int(p1[0]), int(p1[1]), 1, (255,255,255))
def drawRedCircle(p1):
    pygame.gfxdraw.circle(w,  int(p1[0]), int(p1[1]), 2, (255,2,2))
def drawCircles(circles, pygame, w):
    for mcircle in circles:    
        mcircle.draw(pygame,w)
        pass 

def drawRayMarch(p1,direction):
    # save origin of our vector in po
    po = p1
    # print(direction)
    
    while 1:
        
        # check which circle is closests to the point
        smallest = smallestDistanceToCircle(p1, mcircles)
        
        # if limits are met draw red line to indicate a hit
        if smallest <= 1 or smallest >= 500:
            drawRedCircle(p1)
            break
        
        else:
            # draw a line and circle showing the position of the vector
            # and the length to the nearest 
            drawRay(p1,po,smallest)

        # move the vector along the direction by the smallest distance to a circle
        p1 = moveVectorAlongRay(p1, direction, smallest)
        
        # draw the circles 
        drawCircles(mcircles, pygame, w)
        
        pygame.display.update()
        time.sleep(0.2)
        #w.fill((0,0,0))

def generateCircles(n):
    circles = []
    for _ in range(n):
        circles.append(Circle())
    return circles

# draw scene with increating amount of circles 
for i in range(100):
    mcircles = generateCircles(i) # generate circles for scene 
    drawRayMarch([0,0], [0.5,0.5]) # march from position, along a direction
    
    w.fill((0,0,0))
    time.sleep(0.1)
    
