import pygame
from constantes import *

import math
import random 

from projectile import Projectile
from nexus import Nexus
from barrieres import Barrieres

class Projectiles:
	def __init__(self, ecran):
		self.ecran = ecran
		self.list = []
		self.time = 0
		self.mu = FIREBALL_GAUSS_MU_INIT 

	def generate(self):
		if (self.time % FIREBALL_SPAWN_DELAY) == 0 :
			self.mu =  self.time * FIREBALL_GAUSS_MU_MAX / FIREBALL_MAX_TIME
			nbProjectile = random.gauss(self.mu,FIREBALL_GAUSS_SIG_INIT)
			nbProjectile = int(abs(nbProjectile*10))
			nbProjectile = min(nbProjectile,FIREBALL_MAX_SPAWN)

			# nbProjectile = 2

			for i in range(nbProjectile):
				self.list += [Projectile(self.ecran,self.time)]

	def render(self):
		for projectile in self.list : 
			projectile.render()

		self.time += 1 

	def move(self,nexus,barrieres):
		for i,projectile in enumerate(self.list) : 

			if not projectile.alive or (not projectile.onScreen() and projectile.enter):
				self.list.pop(i)
				continue

			projectile.move(nexus,barrieres)

	def destroy(self,pos):
		for i,projectile in enumerate(self.list) : 
			if projectile.hitbox.collidepoint(pos) : 
				self.list.pop(i)
				break