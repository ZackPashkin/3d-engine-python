"""
    3d Engine driver here
    
"""
import pygame as pg
from object_3d import *
from camera import *
from projection import *
 
class Render:
    def __init__(self):
        pg.__init__
        self.resolution = self.width, self.height = 1600, 900
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        self.create_object()
        
    def create_object(self):
        self.camera = Camera(self, [0.5,1,-4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2,0.4,0.2])
        self.object.rotate_y(math.pi / 5)
        
    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.draw()
    
    def run(self):
        while True:
            self.draw()
            [exit() for _ in pg.event.get() if _.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = Render()
    app.run()