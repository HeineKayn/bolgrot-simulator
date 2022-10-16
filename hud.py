import pygame
from pygame import locals as const
from constantes import *

class HUD():

    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None,HUD_FONT_SIZE)
        self.update() 

    def update(self): 
        self.pa = {"texture":pygame.image.load(PA_TEXTURE),
                    "pos":(HUD_MARGIN,HUD_MARGIN)}  
        last_x = HUD_MARGIN + self.pa["texture"].get_rect().right

        self.pa_text = {"texture" : self.font.render(str(self.game.player.pa),True, WHITE)}
        self.pa_text["pos"] = self.pa_text["texture"].get_rect()
        self.pa_text["pos"].left = last_x + HUD_MARGIN 
        self.pa_text["pos"].top  = HUD_MARGIN

        last_y = HUD_MARGIN + self.pa["texture"].get_rect().bottom
        self.leap = {"texture":pygame.image.load(LEAP_TEXTURE),
                    "pos":(HUD_MARGIN,HUD_MARGIN+last_y),}

        self.leap_text = {"texture" : self.font.render(str(MAX_LEAP-self.game.player.bigLeap),True, WHITE)}
        self.leap_text["pos"] = self.leap_text["texture"].get_rect()
        self.leap_text["pos"].left = last_x + HUD_MARGIN 
        self.leap_text["pos"].top  = last_y + HUD_MARGIN

    def render(self):
        self.game.ecran.blit(self.pa["texture"], self.pa["pos"])
        self.game.ecran.blit(self.leap["texture"], self.leap["pos"])
        self.game.ecran.blit(self.pa_text["texture"], self.pa_text["pos"])
        self.game.ecran.blit(self.leap_text["texture"], self.leap_text["pos"])