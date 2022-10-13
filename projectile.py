import pygame
from constantes import *

import math
from random import randint

from nexus import Nexus
from barrieres import Barrieres

class Projectile:
	def __init__(self, ecran, time):
		self.ecran = ecran
		self.time = time

		# Init
		self.create()	
		self.alive = True
		self.enter = False

		# Image
		self.images = [pygame.image.load(x) for x in FIREBALL_TEXTURES]
		self.anim_count = 0
		self.image = self.images[round(self.anim_count)]
		
		# Hitbox
		self.hitbox = self.image.get_rect()
		self.hitbox = self.hitbox.inflate(-40,-40)
		self.hitbox.topleft = self.pos

	def create(self):
		xSpawn = randint(FIREBALL_SPAWNAREA["xMin"],FIREBALL_SPAWNAREA["xMax"])
		ySpawn = randint(FIREBALL_SPAWNAREA["yMin"],FIREBALL_SPAWNAREA["yMax"])
		self.pos = [xSpawn,ySpawn]

		xDest = 0
		yDest = randint(0,HEIGHT)

		# LA COURBE SPEEDAMP PAS OUF
		self.vect_dir = (xDest - xSpawn, yDest - ySpawn)
		self.speedAmp = -0.019/(0.0001*self.time+1) + FIREBALL_MAX_AMP

		# Pour les test je le monte
		# self.speedAmp = 9999

		self.speedAmp = min(self.speedAmp,FIREBALL_MAX_AMP)

	def onScreen(self):
		return self.ecran.get_rect().contains(self.hitbox)

	def render(self):
		pygame.draw.rect(self.ecran,BLUE,self.hitbox,1)

		if self.alive and self.onScreen(): 
			self.image = self.images[round(self.anim_count)]
			self.image = pygame.transform.scale(self.image, FIREBALL_SIZE) 
			self.ecran.blit(self.image, self.pos)
			self.anim_count += FIREBALL_ANIM_FRAMES / 100
			if self.anim_count >= len(self.images)-1 :
				self.anim_count = 0

	def move(self, nexus, barrieres):
		self.pos[0] += self.vect_dir[0] * self.speedAmp 
		self.pos[1] += self.vect_dir[1] * self.speedAmp

		self.hitbox.topleft = self.pos

		if self.onScreen() and not self.enter :
			self.enter = True

		if nexus.hitbox.colliderect(self.hitbox) :
			nexus.collide(self)

		for barriere in barrieres.list :
			if barriere.hitbox.colliderect(self.hitbox) :
				barriere.collide(self)