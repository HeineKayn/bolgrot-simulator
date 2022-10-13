import pygame
from constantes import *

from bar import Bar

class ManaBar(Bar):
	def __init__(self, ecran, entity):
		self.ecran = ecran
		self.entity = entity

		self.value 	= self.entity.valueMax
		self.pos 	= (20,20)
		self.posAbsolue = True

		self.size 	= MANA_BAR_SIZE
		self.offset = 0
		self.thick 	= MANA_BAR_THICK
		self.colors	= [BLUE,WHITE]
		super().__init__()

	def update(self):
		self.value = self.entity.value
		self.inner = self.innerInit.inflate((self.value-self.maxValue)*self.chunkSize,0)
		self.updatePos()