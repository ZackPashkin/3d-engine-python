"""
    3d Engine driver here
    
"""
import pygame as pg
from my_3d_object import *
from camera import *
from projection import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
 
class Render:
    def __init__(self):
        pg.__init__
        self.resolution = self.width, self.height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = FPS
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        self.create_object()
       
        
    def create_object(self):
        self.camera = Camera(self, [-1,2,-20])
        self.projection = Projection(self)
        # default object cube
        # self.object = Object3D(self)
        # self.object = self.load_object_from_file('assets/eyeball.obj')
        self.object = self.load_object_from_file('assets/12953_ChocolateRabbit_v1.obj')
        # self.object = self.load_object_from_file('assets/girl_s.obj')
        self.object.translate([0.2,0.4,0.2])
        self.object.rotate_y(math.pi / 5)
    
    
    def load_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0])-1 for face_ in faces_])
        return Object3D(self, vertex, faces)
    
        
    
        
    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.draw()
    
    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for _ in pg.event.get() if _.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = Render()
    app.run()