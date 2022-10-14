import pygame
from pygame.locals import *
from pygame import Rect

import numpy as np
from random import randint

debug = False # display map as text

TILE_W = 32
TILE_H = 32

class Map():
    def __init__(self,game):
        self.game = game
        self.ecran = game.ecran
        self.tiles = np.array([[0, 0, 1, 1, 0, 0], 
                             [0, 1, 1, 1, 1, 0],
                             [0, 1, 1, 1, 1, 0], 
                             [0, 1, 1, 1, 1, 0], 
                             [0, 1, 1, 1, 1, 0], 
                             [0, 0, 1, 1, 0, 0], ])
        self.tiles_x, self.tiles_y = np.shape(self.tiles)
        
    def reset(self):
        pass
            
    # garder des infos sur les cases à leur création
    # placé au bon endroit et bonne taille (en fonction nombre elem)
    def draw(self):     
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                
                id = self.tiles[x,y]
                print(id)
                dest = Rect( x * TILE_W, y * TILE_H, TILE_W, TILE_H )
                # src  = Rect( id * TILE_W, 0, TILE_W, TILE_H )     
                if id>0:
                    pygame.draw.rect(self.ecran, (150, 150, 150), dest)              
                    
        
