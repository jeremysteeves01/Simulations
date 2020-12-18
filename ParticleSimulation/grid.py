import pyglet
import pyglet.gl as gl
import math
import random

class grid:

    def __init__(self,spaceinit,spaceend,n):
        self.distance = [(spaceend[0] - spaceinit[0]) / n, (spaceend[1] - spaceinit[1])/n]
        self.pointzero = spaceinit
        self.n=n

        self.index = []

        for i in range(n+1):
            index = []
            for j in range(n+1):
                index += [[i,j,[]]]
            self.index +=[index]

    def whereparticles(self, particlexs, nparticles):
        # index = [1,[3,4]] , 1 is the index of the particles, [3,4] is the position in the grid
        for i in range(self.n +1):
            for j in range(self.n+1):
                self.index[i][j][2]=[]

        for i in range(nparticles):
            thisindex = self.whereparticles(particlexs[i].position)
            self.index[thisindex[1]][thisindex[0]][2] += [particlexs[i].index]

    # Where a single particle is located
    def whereparticle(self,points):
        nx = int((points[0]-self.pointzero[0]) / self.distances[0])
        ny = int((points[1]-self.pointzero[1]) / self.distances[1])
        return [nx, ny]

    # TAKE THE INDEX TO DETERMINE WHAT ARE THE INTERSECTIONS BETWEEN PARTICLES IN
    def intersection(self, particlexs):
        for i in range(self.n+1):
            for j in range(self.n+1):
                listx = []
                for k in listx:
                    where = particlexs[k].scatter(particlexs,listx)
                    if where is not None:
                        listx.remove(where)
                    listx.pop(0)