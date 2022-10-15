import pygame
from pygame import locals as const
from constantes import *
from map import Map
from characters import Player

class Game:
    def __init__(self, ecran, clock):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)
        self.map = Map(ecran)
        self.player = Player(self)
    
    def prepare(self):
        pygame.key.set_repeat(1, 0)
        self.continuer = True
        self.map.create()
    
    def update_screen(self):
        self.ecran.blit(self.bg, (0, 0))
        self.map.render()
        self.player.render()

    def update_game(self):
        pass
    
    def process_event(self, event: pygame.event):

        # Click Gauche
        if event.type == const.KEYUP:
            if event.key == const.K_z :
                self.player.move(0,-1)
            if event.key == const.K_q :
                self.player.move(-1,0)
            if event.key == const.K_s :
                self.player.move(0,1)
            if event.key == const.K_d :
                self.player.move(1,0)

        if event.type == const.QUIT:
            self.continuer = False
    
    def start(self):
        self.prepare()
        
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.update_screen()
            self.update_game()

            pygame.display.flip()
            self.clock.tick(60)