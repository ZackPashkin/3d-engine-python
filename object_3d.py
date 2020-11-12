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
        
    def translate(self, position):
        self.vertices = self.vertices @ self.vertices(position)
        
    def scale(self, scale_up_to):
        self.vertices = self.vertices @ scale(scale_up_to)
        
    def rotate_x_coordinate(self, angle):
        self.vertices = self.vertices @ rotate_x_coordinate(angle)
        
    def rotate_y_coordinate(self, angle):
        self.vertices = self.vertices @ rotate_y_coordinate(angle)
    
    def rotate_z_coordinate(self, angle):
        self.vertices = self.vertices @ rotate_z_coordinate(angle)
        
        

        
    
    
    