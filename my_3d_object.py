"""
    Create 3d object

"""
    
import pygame as pg
from matrix_manipulations import *
from settings import POLYGON_WIDTH, CIRCLE_WIDTH, DRAW_VERTICES, OBJECT_SPIN
from numba import njit


@njit(fastmath=True)
def speed_up_numpy_any(arr, width_, height_):
    # assert width_ == int, "Incorrect input for width. Width should be int"
    # assert height_ == int, "Incorrect input for height. Height should be int"
    return np.any((arr == width_) | (arr == height_))

class Object3D:
    # def __init__(self, render):
    #     self.render = render
    #     self.vertices = np.array([(0,0,0,1),(0,1,0,1), (1,1,0,1), (1,0,0,1),
    #                               (0,0,1,1), (0,1,1,1), (1,1,1,1),(1,0,1,1)])
        
    #     self.faces = np.array([(0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)])
    
    # def draw(self):
    #     self.screen_projection()
    #     self.object_self_rotation()
    
    # for object from file
    def __init__(self, render,vertices,faces):
        self.render = render
        self.vertices = np.array([np.array(v) for v in vertices])
        self.faces = np.array([np.array(face) for face in faces])
        self.movement_flag = DRAW_VERTICES
        self.draw_vertices = OBJECT_SPIN
        
  
    def draw(self):
        self.screen_projection()
        self.object_self_rotation()
        
        
    def object_self_rotation(self):
        "Fuction that make object spin"
        self.rotate_y(pg.time.get_ticks() % 0.1)
    
    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1,1)
        vertices[(vertices > 1) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:,:2]
        
        for face in self.faces:
            polygon = vertices[face]
            #put numba here
            if not speed_up_numpy_any(polygon, self.render.h_width, self.render.h_height):
                pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, POLYGON_WIDTH)
                
        if self.draw_vertices:     
            for vertex in vertices:
                if not speed_up_numpy_any(polygon, self.render.h_width, self.render.h_height):
                    pg.draw.circle(self.render.screen, pg.Color('white'), vertex, CIRCLE_WIDTH)
                        
            
        
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
        
        

        
    
    
    