import pygame
from pygame import locals as const
from constantes import *

from nexus import Nexus
from projectiles import Projectiles
from barrieres import Barrieres
from map import Map

class Game:
    def __init__(self, ecran, clock):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)
        self.map = Map(self)
    
    def prepare(self):
        pygame.key.set_repeat(1, 0)
        self.continuer = True
    
    def update_screen(self):
        
        self.ecran.blit(self.bg, (0, 0))
        self.map.draw()

    def update_game(self):
        pass
    
    def process_event(self, event: pygame.event):

        # Click Gauche
        if event.type == const.MOUSEBUTTONUP and event.button == 1:
            pass

        # Click Droit
        if event.type == const.KEYDOWN and event.key == const.K_a:
            pass

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