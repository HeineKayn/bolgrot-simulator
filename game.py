import pygame
from pygame import locals as const
from constantes import *
from map import Map
from characters import Player,Enemies
from hud import HUD

class Game:
    def __init__(self, ecran, clock):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)
    
    def prepare(self):
        pygame.key.set_repeat(1, 0)
        self.continuer = True
        self.map = Map(self.ecran)
        self.player = Player(self)
        self.enemies = Enemies(self)
        self.hud = HUD(self)
        self.enemies.invoke(2)
    
    def update_screen(self):
        self.ecran.blit(self.bg, (0, 0))
        self.map.render()
        self.enemies.render()
        self.player.render()
        self.hud.render()

    def update_game(self):
        for enemy in self.enemies.list:
            if self.player.pos == enemy.pos :
                enemy.alive = False
                self.enemies.list.remove(enemy)
                del enemy
                
        if self.player.pa < 1 :
            self.player.newRound()
            self.hud.update()
            self.enemies.invoke(4)

    def process_event(self, event: pygame.event):

        # Click Gauche
        if event.type == const.KEYUP:
            factor = 1
            moved  = False

            if self.player.pa > 0 :
                if event.mod & pygame.KMOD_SHIFT and self.player.bigLeap<MAX_LEAP:
                    factor = 2
                if event.key == const.K_z :
                    moved = self.player.move(0,-factor)
                if event.key == const.K_q :
                    moved = self.player.move(-factor,0)
                if event.key == const.K_s :
                    moved = self.player.move(0,factor)
                if event.key == const.K_d :
                    moved = self.player.move(factor,0)
                if moved : 
                    self.player.pa -= 1
                    if moved and event.mod & pygame.KMOD_SHIFT and self.player.bigLeap < MAX_LEAP:
                        self.player.bigLeap += 1
                    self.hud.update()

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