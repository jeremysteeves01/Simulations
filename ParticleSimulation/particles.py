import pyglet
import pyglet.gl as gl
import math
from mywindow import *
import random

def calculatecolor(speed):
    if speed < 8.0:
        color = [int(speed)+30.0,0,255-int(speed)*30]
    else:
        color = [255,0,0]
    return color

class particles:

    def __int__(self, particlexs, nparticles):
        self.particle = particlexs
        self.nparticles = nparticles

        self.points = []
        self.colors = []

        for i in range(self.nparticles):
            self.points += self.particle[i].position
            self.colors += self.particle[i].color

        self.pointsdraw = pyglet.graphics.vertex_list(nparticles, 'v2f/stream', self.points), ('c3B', self.colors)

    def move(self, particlexs):
        for i in range(self.nparticles):
            self.points[2*i:2*i+2] = particlexs[i].position

        self.pointsdraw.vertices = self.points

    def colorpoint(self):
        for i in range(self.nparticles):
            self.particle[i].speed()