import pyglet
import pyglet.gl as gl
import math
import random

class fixsurface:
    def __init__(self,positionstart,positionend,color=(0,0,0)):
        self.position = positionstart + positionend

        #WHERE THE SURFACE START AND END
        self.positionstart = positionstart
        self.positionend = positionend
        self.length = math.sqrt((positionend[1]-positionstart[1])**2+(positionend[0]-positionstart[0])**2)

        # UNDERSTAND IF WE ARE LOOKING FOR Y=mx (XTYPE == TRUE) or x=my (xtype == false)
        self.xtype = True
        self.m = 0 #angular coefficient of segment
        self.q = 0
        self.alpha = 0 #angle between the segment and x-axis
        self.calculatemq()
        self.pointsdraw = pyglet.graphics.vertex_list(2, ('v2f/stream',self.position),('c3B',color*2))

    def calculatemq(self):

        # CALCULATE THE COEFFICIENT FOR DESCRIBING THE SEGMENT AS A STRAIGHT LINE (ANGULAR COEFFICIENT)
        deltay = self.positionend[1] - self.positionstart[1]
        deltax = self.positionend[0] - self.positionstart[0]

        if abs(deltax) > 0 :
            self.m = deltay/deltax
            self.q = self.positionstart[1] - self.m*self.positionstart[0]
            self.alpha = math.atan(self.m)
        else:
            self.xtype = False
            self.alpha = math.pi/2

    def intersection(self,particles, nparticles):
        #determine where particles hit a wall segment
        for i in range(nparticles):
            if self.xtype:
                y = self.m*particles[i].position[0]+self.q
                if abs(y-particles[i].position[1]) < 40:
                    return [True,i]
            else:
                x = self.positionstart[0]
                if abs(x - particles[i].position[0]) < 40:
                    return [True,i]
        return [False]

    def scatter(self,particles, nparticles):
        where = self.intersection(particles, nparticles)
        if where[0]:
            tempvx = particles[where[1]].velocity[0]
            tempvy = particles[where[1]].velocity[1]
            particles[where[1]].velocity[0] = math.cos(2*self.alpha) * tempvx + math.sin(2*self.alpha) * tempvy
            particles[where[1]].velocity[1] = math.sin(2*self.alpha) * tempvx - math.cos(2*self.alpha) * tempvy


