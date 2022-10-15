from asyncio.windows_events import NULL
import pygame
from pygame.locals import *
from constantes import *

class Tile():
    def __init__(self,ecran,id,pos,type):
        self.ecran = ecran
        self.id = id
        self.pos = pos
        self.type = type
        self.entity = NULL
        self.texture = pygame.image.load(TILE_TEXTURE).convert_alpha()
        self.texture = pygame.transform.scale(self.texture,[TILEWIDTH,TILEHEIGHT]) 

    def render(self):
        self.ecran.blit(self.texture, self.pos) #display the actual tile  