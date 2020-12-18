import pyglet
import pyglet.gl as gl
import math
import random

from pyglet import window
import particles as pp
import particle as p
import fixsurface as fs

game_window = pyglet.window.Window()


class mywindow(pyglet.window.Window):

    def __init__(self, width, height, name):
        super().__init__(width, height, name, resizable=True)

        gl.glClearColor(1, 1, 1, 1)
        gl.glPointSize(10)

        # Window Stuff
        self.width = width
        self.height = height
        self.name = name
        self.zoom = 1
        self.x = 0
        self.y = 0
        self.time = 0
        self.key = None

        #CREATE THE PARTICLES
        self.Nparticles = 20
        self.rangeparticles = range(self.Nparticles)
        self.mainparticles = []
        # self.mainparticles += [p.particle([-self.width / 2, 0], 50, [1, 0], 0)]
        # self.mainparticles += [p.particle([self.width / 2, 0], 10, [-1, 0], 1)]

        # self.mainparticle = p.particle([0, 0], 10, [1, 0])
        for i in self.rangeparticles:
            self.mainparticles += [p.particle([random.uniform(-100,100),random.uniform(-100,100)],5,
                                              [random.uniform(-2,2),random.uniform(-2,2)],i)]

        # CREATE THE SURFACES
        self.Nsurfaces = 4
        self.rangesurfaces = range(self.Nsurfaces)
        self.surfaces = []
        self.surfaces += [fs.fixsurface([0,-500],[-500,0])]
        self.surfaces += [fs.fixsurface([0,+500],[+500,0])]
        self.surfaces += [fs.fixsurface([0,+500],[-500,0])]
        self.surfaces += [fs.fixsurface([0,-500],[+500,0])]

    def on_draw(self, dt=0.002):
        self.clear()

        # Draw the particle,
        for i in self.rangeparticles:
            self.mainparticles[i].pointsdraw.draw(pyglet.gl.GL_POINTS)

        # DRAW THE SURFACES
        for i in self.rangesurfaces:
            self.surfaces[i].pointsdraw.draw(pyglet.gl.GL_LINES)
            self.surfaces[i].scatter(self.mainparticles, self.Nparticles)

        # check if the particle collides
        for i in self.rangeparticles:
            self.mainparticles[i].scatter(self.mainparticles, self.Nparticles)

        # move the particle and reset the scatter flat
        for i in self.rangeparticles:
            self.mainparticles[i].isscatter = True
            self.mainparticles[i].move()


    def on_resize(self, width, height):
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glOrtho(-width, width, -height, height, -1, 1)
