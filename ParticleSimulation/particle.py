import pyglet
import pyglet.gl as gl
import math
from mywindow import *
import random



class particle:

    # def __int__(self, particlexs, nparticles):
    #     self.particle = particlexs
    #     self.nparticles = nparticles
    #
    #     self.points = []
    #     self.colors = []
    #
    #     for i in range(self.nparticles):
    #         self.points += self.particle[i].position
    #         self.colors += self.particle[i].color
    #
    #     self.pointsdraw = pyglet.graphics.vertex_list(nparticles, 'v2f/stream', self.points), ('c3B', self.colors)

    def __init__(self, position, mass, velocity, index):
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)

        # self.momentum = self.mass * self.speed
        self.index = index
        self.isscatter = False
        colour = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        self.pointsdraw = pyglet.graphics.vertex_list(1, ('v2f/stream', self.position), ('c3B', colour))

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.pointsdraw.vertices = self.position

    def intersection(self, particles, nparticles):
        for i in range(nparticles):
            if i != self.index:
                x = self.position[0] - particles[i].position[0]
                y = self.position[1] - particles[i].position[1]
                if math.sqrt(x ** 2 + y ** 2) < 5:
                    print("collsion!!!")
                    return [True, i]
        return [False]

    def scatter(self, particles, nparticles):
        where = self.intersection(particles, nparticles)
        if where[0] and particles[where[1]].isscatter:
            # avoid multiple scattering at the same time
            particles[where[1]].isscatter = False
            self.isscatter = False

            # TOTAL AND DIFFERENCE MASS TO SIMPLIFY CALC
            totalmass = self.mass + particles[where[1]].mass
            massdiff = self.mass - particles[where[1]].mass

            # STORE THE VELOCITY VARIABLE AVOIDING THE ERROR CAUSED BY SEQUENTIAL CALCS
            tempvelocity = [self.velocity[0], self.velocity[1]]

            self.velocity[0] = (massdiff * self.velocity[0] + 2 * particles[where[1]].mass *
                                particles[where[1]].velocity[0]) / totalmass
            self.velocity[1] = (massdiff * self.velocity[1] + 2 * particles[where[1]].mass *
                                particles[where[1]].velocity[1]) / totalmass
            particles[where[1]].velocity[0] = (-massdiff * tempvelocity[0] + 2 * self.mass + tempvelocity[
                0]) / totalmass
            particles[where[1]].velocity[1] = (-massdiff * tempvelocity[1] + 2 * self.mass + tempvelocity[
                1]) / totalmass


# Resize the window
def resize(width, height, zoom, x, y):
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    gl.glOrtho(-width, width, -height, height, -1, 1)
    gl.glViewport(0, 0, width, height)
    gl.glOrtho(-zoom, zoom, -zoom, zoom, -1, 1)
    gl.glTranslated(-x, -y, 0)

# class mywindow(pyglet.window.Window):
#
#     def __init__(self, width, height, name):
#         super().__init__(width, height, name, resizable=True)
#
#         gl.glClearColor(1, 1, 1, 1)
#         gl.glPointSize(5)
#
#         # Window Stuff
#         self.width = width
#         self.height = height
#         self.name = name
#         self.zoom = 1
#         self.x = 0
#         self.y = 0
#         self.time = 0
#         self.key = None
#         self.mainparticle = particle([0, 0], 10, [1, 0])
#
#     # @window.event
#     def on_draw(self, dt=0.002):
#         self.clear()
#         self.mainparticle.pointsdraw.draw(pyglet.gl.GL_POINTS)
#         self.mainparticle.move()
#
#     def on_resize(self, width, height):
#         gl.glMatrixMode(gl.GL_MODELVIEW)
#         gl.glLoadIdentity()
#         gl.glOrtho(-width, width, -height, height, -1, 1)
