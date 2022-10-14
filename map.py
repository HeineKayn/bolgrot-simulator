import pygame
from pygame.locals import *
from pygame import Rect

import numpy as np
from random import randint

debug = False # display map as text
TILEWIDTH = 64  #holds the tile width and height
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT /2
TILEWIDTH_HALF = TILEWIDTH /2

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
        self.wall = pygame.image.load('./ressources/textures/wall.png').convert_alpha()  #load images
        self.grass = pygame.image.load('./ressources/textures/grass.png').convert_alpha()
        
    def reset(self):
        pass
            
    # garder des infos sur les cases à leur création
    # placé au bon endroit et bonne taille (en fonction nombre elem)
    def draw(self):     

        self.wall = pygame.transform.scale(self.wall, (TILEHEIGHT* self.game.coef,TILEWIDTH* self.game.coef)) 

        for row_nb, row in enumerate(self.tiles):    #for every row of the map...
            for col_nb, tile in enumerate(row):
                cart_x = row_nb * TILEWIDTH_HALF * self.game.coef
                cart_y = col_nb * TILEHEIGHT_HALF * self.game.coef
                iso_x = (cart_x - cart_y) 
                iso_y = (cart_x + cart_y)/2
                centered_x = self.game.ecran.get_rect().centerx + iso_x
                centered_y = self.game.ecran.get_rect().centery/2 + iso_y

                if tile == 1:
                    tileImage = self.wall
                    self.game.ecran.blit(tileImage, (centered_x, centered_y)) #display the actual tile    
                else:
                    pass
                    # tileImage = self.grass
                      
                    
        

