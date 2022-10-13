import pygame
from constantes import *

import random

from hp_bar import HpBar

class Nexus:
	def __init__(self, ecran):
		self.ecran = ecran
		self.hp = NEXUS_HP
		self.alive = True

		self.images = [pygame.image.load(x) for x in NEXUS_TEXTURES]
		self.anim_count = 0
		self.image = self.images[random.randint(1,len(self.images)-1)]

		self.hitbox = self.image.get_rect()
		self.hitbox = self.hitbox.inflate(-80,0)
		self.pos = (0,HEIGHT//2 - self.image.get_height()//2)
		self.hitbox.topleft = self.pos

		self.hpBar = HpBar(self.ecran,self)

	def render(self):
		self.ecran.blit(self.image, self.pos)
		self.anim_count += 1
		if self.anim_count >= NEXUS_ANIM_FRAMES :
			self.image = self.images[random.randint(1,len(self.images)-1)]
			self.anim_count = 0

		self.hpBar.update()
		self.hpBar.render()
		pygame.draw.rect(self.ecran,RED,self.hitbox,1)  

	def collide(self, projectile):
		projectile.alive = False

		self.hp -= 1
		if self.hp < 1 :
			self.alive = False
