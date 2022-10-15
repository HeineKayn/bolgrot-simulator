from pygame.locals import *
from constantes import *
from random import randint

class Character():

    def __init__(self,game,pos):
        self.game = game
        self.pos = pos
        self.anim_count = 0

    def move(self,right,up):
        posx = self.pos[0] + right
        posy = self.pos[1] + up
        self.pos = [posx,posy]

    def render(self):
        self.rec_sprite   = self.sprite.get_rect()
        self.current_tile = self.game.map.tiles[self.pos[0],self.pos[1]]
        self.current_pos  = self.current_tile.pos
        self.pos_sprite   = [self.current_pos[0] + TILEWIDTH_HALF - self.rec_sprite.width//2, self.current_pos[1] - self.rec_sprite.height//4]
        self.rec_sprite.topleft = self.pos_sprite
        self.game.ecran.blit(self.sprite, self.pos_sprite)

class Player(Character):

    def __init__(self,game,pos=[randint(0,MAP_SIZE-1),randint(0,MAP_SIZE-1)]):
        self.sprite = pygame.image.load(PLAYER_TEXTURE)
        self.sprite = pygame.transform.scale(self.sprite,[25,50]) 
        super().__init__(game,pos)