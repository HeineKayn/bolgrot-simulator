from pygame.locals import *
from constantes import *
from random import randint,choice
import numpy as np

class Character():

    def __init__(self,game,pos):
        self.game = game
        self.pos = pos
        self.anim_count = 0
        self.alive = True

    def move(self,right,up):
        shapex,shapey = np.shape(self.game.map.tiles)
        posx = min(max(self.pos[0] + right,0),shapex-1)
        posy = min(max(self.pos[1] + up,0),shapey-1)
        moved = posx != self.pos[0] or posy != self.pos[1]
        if moved :
            self.game.map.getTile(self.pos).entity = None
            self.pos = [posx,posy]
            self.game.map.getTile(self.pos).entity = self
        return moved

    def render(self):
        if self.alive:
            self.rec_sprite   = self.sprite.get_rect()
            self.current_tile = self.game.map.tiles[self.pos[0],self.pos[1]]
            self.current_pos  = self.current_tile.pos
            self.pos_sprite   = [self.current_pos[0] + TILEWIDTH_HALF - self.rec_sprite.width//2, self.current_pos[1] - self.rec_sprite.height//4]
            self.rec_sprite.topleft = self.pos_sprite
            self.game.ecran.blit(self.sprite, self.pos_sprite)

class Enemies():
    def __init__(self,game):
        self.game = game
        self.list = []

    def render(self):
        for ennemy in self.list:
            ennemy.render()

    def invoke(self,x=1):
        for _ in range(x):
            pos = self.game.map.getFreePos()
            enemy = Enemy(self.game,pos)
            self.list += [enemy]
            self.game.map.getTile(pos).entity = enemy

class Enemy(Character):
    def __init__(self,game,pos):
        self.sprite = pygame.image.load(ENNEMY_TEXTURE)
        self.sprite = pygame.transform.scale(self.sprite,[50,50]) 
        super().__init__(game,pos)

class Player(Character):

    def __init__(self,game):
        self.sprite = pygame.image.load(PLAYER_TEXTURE)
        self.sprite = pygame.transform.scale(self.sprite,[25,50]) 
        pos = game.map.getFreePos()
        game.map.getTile(pos).entity = self
        super().__init__(game,pos)