from math import sqrt, cos, sin
import pygame
import pygame.gfxdraw
import time
import random

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

# return the distance from a point to a circle
def dstToCircle(point, center, radius):
    vc = []
    vc.append(center.pos()[0] - point[0])
    vc.append(center.pos()[1] - point[1])

    return length(vc) - radius

class Circle:
    def __init__(self):
        self.x = int(random.random() * 500)
        self.y = int(random.random() * 500)
        self.radius = int(random.random()*50)

    def pos(self):
        return [self.x, self.y]

    def draw(self,pygame, window):
        pygame.gfxdraw.circle(w,  self.pos()[0], self.pos()[1], self.radius, (25,222,2))

def dstToScene(p, circles):
    vdstToScene = 500
    
    mindistance = 0.1

    for circle in circles:
        vdstToCircle = dstToCircle(p, circle, circle.radius)
        vdstToScene = min(vdstToCircle, vdstToScene)
    
    return vdstToScene


def moveVector(origin,direction,speed):
    v1=origin[0] + direction[0] * speed
    v2=origin[0] + direction[0] * speed
    return [v1,v2]

w = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('Ray marching')


p1 = [10,10]
direction = [p1[0] / length(p1), p1[1] / length(p1)]

# generate circles for scene 
mcircles = []
for i in range(10):
    mcircles.append(Circle())

# main loop
for i in range(100):

    smallest = dstToScene(p1, mcircles)
    
    print(smallest)

    # detect hit 
    if smallest <= 1 or smallest == 500:
       pygame.gfxdraw.circle(w,  int(p1[0]), int(p1[1]), 5, (255,2,2))
       break
    
    else:
        pygame.draw.line(w,(25,55,255), p1, direction)
        pygame.gfxdraw.pixel(w,1,1,(244,2,2))
        pygame.gfxdraw.circle(w,  int(p1[0]), int(p1[1]), int(smallest)+1, (255,255,255))
        pygame.gfxdraw.circle(w,  int(p1[0]), int(p1[1]), 1, (255,255,255))
    
    p1 = moveVector(p1,direction,smallest)
    
    for mcircle in mcircles:    
        mcircle.draw(pygame,w)

    pygame.display.update()
    time.sleep(0.5)
    #w.fill((0,0,0))

pygame.display.update()
time.sleep(2)
    
