import pygame
from constantes import *

from bar import Bar

class HpBar(Bar):
	def __init__(self, ecran, entity):
		self.ecran = ecran
		self.entity = entity

		self.value 		= self.entity.hp
		self.pos 		= self.entity.hitbox.midtop
		self.posAbsolue = False
		
		self.size 		= HP_BAR_SIZE
		self.offset 	= HP_BAR_OFFSET
		self.thick 		= HP_BAR_THICK
		self.colors		= [HP_BAR_INNER_COLOR,HP_BAR_EDGE_COLOR]
		super().__init__()

	def update(self):
		self.value = self.entity.hp
		self.inner = self.innerInit.inflate((self.value-self.maxValue)*self.chunkSize,0)

		if len(self.colors) == 2:
			self.updateColor()
		self.updatePos()