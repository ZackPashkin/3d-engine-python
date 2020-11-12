"""
    Create 3d object

"""
    
import pygame as pg
from matrix_manipulations import *

class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertices = np.array([(0,0,0,1),(0,1,0,1), (1,1,0,1), (1,0,0,1),
                                  (0,0,1,1), (0,1,1,1), (1,1,1,1),(1,0,1,1)])
        
        self.faces = np.array([(0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)])
    
    def draw(self):
        self.screen_projection()
    
    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1,1)
        vertices[(vertices > 1) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:,:2]
        
        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.render.h_width) | (polygon == self.render.h_height)):
                pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, 3)
                
        for vertex in vertices:
            if not np.any((vertex == self.render.h_width) | (vertex == self.render.h_height)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)
                    
            
        
    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)
        
    def scale(self, scale_up_to):
        self.vertices = self.vertices @ scale(scale_up_to)
        
    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)
        
    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)
    
    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)
        
        

        
    
    
    