import pygame
from constantes import *

class Barriere:
	def __init__(self, ecran, pos, timeCreated):
		self.ecran = ecran
		self.pos = pos
		self.time = timeCreated

		self.hp = 1
		self.hitbox = pygame.Rect(self.pos,(BARRIER_SIZE,BARRIER_SIZE)) 

	def render(self):
		pygame.draw.rect(self.ecran,BARRIER_COLOR,self.hitbox)  

	def collide(self, projectile):
		projectile.alive = False
		# self.hp -= 1