import pyglet
import particle
import mywindow


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1 / 120)
particle.mywindow(800, 800, 'particle collision simulator')
pyglet.app.run()

