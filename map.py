from pygame.locals import *

import numpy as np
from constantes import *
from random import choice

class Map():
    def __init__(self,ecran):
        self.ecran = ecran
        # self.tiles_map = np.array([[0, 0, 1, 1, 0, 0, 1, 1], 
        #                             [0, 1, 1, 1, 1, 0, 1, 1],
        #                             [0, 1, 1, 1, 1, 0, 1, 1], 
        #                             [0, 1, 1, 1, 1, 0, 1, 1],
        #                             [0, 1, 1, 1, 1, 1, 1, 1], 
        #                             [0, 1, 1, 1, 1, 1, 1, 1], 
        #                             [0, 1, 1, 1, 1, 1, 1, 1],  
        #                             [0, 1, 1, 1, 1, 0, 1, 1], 
        #                             [0, 0, 1, 1, 0, 0, 1, 1]])
        self.tiles_map = np.ones((MAP_SIZE,MAP_SIZE))
        self.tiles = np.empty(np.shape(self.tiles_map), dtype=Tile)
        self.create()
        
    def reset(self):
        pass
            
    def create(self):     
        for row_nb, line in enumerate(self.tiles_map):    
            for col_nb, tile in enumerate(line):
                centered_x = self.ecran.get_rect().centerx - ((len(self.tiles_map)/2 - row_nb) * TILEWIDTH)
                centered_y = self.ecran.get_rect().centery - ((len(line)/2 - col_nb) * TILEHEIGHT_UPPER)

                id  = [row_nb, col_nb]
                pos = (centered_x, centered_y)
                if tile == 1:
                    self.tiles[row_nb, col_nb] = Tile(self.ecran,id,pos,type=tile)
                else:
                    pass
    
    def getTile(self,pos):
        return self.tiles[pos[0], pos[1]]

    def getFreePos(self):
        free_tiles = [tile for tile in self.tiles.flatten() if tile.entity == None]
        tile = choice(free_tiles)
        return tile.id

    def render(self):
        for line in self.tiles:
            for tile in line:
                if tile : 
                    tile.render()
                    
class Tile():
    def __init__(self,ecran,id,pos,type):
        self.ecran = ecran
        self.id = id
        self.pos = pos
        self.type = type
        self.entity = None
        self.texture = pygame.image.load(TILE_TEXTURE).convert_alpha()
        self.texture = pygame.transform.scale(self.texture,[TILEWIDTH,TILEHEIGHT]) 

    def render(self):
        self.ecran.blit(self.texture, self.pos) #display the actual tile  