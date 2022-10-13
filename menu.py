import pygame
from pygame import locals as const
from constantes import *

class Menu():

    def __init__(self, ecran, clock):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)

        self.texts = []
        self.rects = []
        self.nb_text = len(TEXT_MENU)
        self.margins = []
        
        # Partie bonus clignotement du sous titre
        self.compteur = 0

        for text in TEXT_MENU : 
            self.addText(text["content"],text["color"],text["style"])
        self.centerRects()

    def addText(self,text,color,style):
        font = pygame.font.SysFont(FONT_LIST[style][0],FONT_LIST[style][1]) 
        text = font.render(text, True, color)
        self.texts += [text]
        self.margins += [FONT_LIST[style][2]]

        rect = text.get_rect()
        rect.centerx = WIDTH // 2 
        if self.rects :
            rect.midtop = self.rects[-1].midbottom
        self.rects += [rect]

    def centerRects(self):
        self.menuRect = self.rects[0].unionall(self.rects[1:])
        self.menuRect = self.menuRect.inflate(0,sum(self.margins[:-1]))
        self.menuRect.center = (WIDTH//2, HEIGHT//2)

        self.rects[0].top = self.menuRect.top
        for i in range(self.nb_text):
            if i > 0 :
                self.rects[i].top = self.rects[i-1].bottom + self.margins[i-1]

    def render(self):
        for i,text in enumerate(self.texts) : 

            # Clignotement du sous titre
            if TEXT_MENU[i]["style"] == "h2" and self.compteur > CLIGNE_PERIODE : 
                continue
            self.ecran.blit(text, self.rects[i])

        if self.compteur >= CLIGNE_PERIODE*2 :
             self.compteur = 0
        else :
            self.compteur += 1    

    def process_event(self):
        for event in pygame.event.get():
            if event.type == const.QUIT :
                exit()
            if event.type == const.KEYDOWN:
                self.continuer = 0

    def start(self):
        while self.continuer:
            self.process_event()
            self.ecran.blit(self.bg, (0, 0))
            self.render()
            pygame.display.flip()    
            self.clock.tick(60)