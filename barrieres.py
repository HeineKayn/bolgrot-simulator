import pygame
from constantes import *

from barriere import Barriere
from mana_bar import ManaBar

class Barrieres:
	def __init__(self, ecran):
		self.ecran = ecran
		self.valueMax = BARRIER_LIMIT
		self.list = []
		self.value = 0

		self.lastTime = pygame.time.get_ticks()
		self.lastPos 	= pygame.mouse.get_pos()

		self.manaBar = ManaBar(self.ecran,self)

	def create(self):

		pos = list(pygame.mouse.get_pos())
		newPos = list(pygame.mouse.get_pos())
		time = pygame.time.get_ticks()
		delay = self.lastTime - time

		# Si y'en a déjà un au même endroit on skip
		if self.lastPos == pos :
			return

		# Si ça fait longtemps que pas barriere, en fait juste une
		if delay > BARRIER_CREATE_DELAY:
			self.add(pos)

		# Si clic appuyé on smooth pour pas que y'ai de trou
		else :
			diffPosX = pos[0] - self.lastPos[0]
			diffPosY = pos[1] - self.lastPos[1]

			coeffX 	 = abs(diffPosX) // diffPosX if diffPosX != 0 else 0
			coeffY 	 = abs(diffPosY) // diffPosY if diffPosY != 0 else 0
			coeff 	 = [coeffX,coeffY]
			absPos 	 = [abs(diffPosX),abs(diffPosY)]

			# On fait d'abord la ligne droite
			if absPos[0] != absPos[1]:
				nbItePreablable = abs(absPos[0] - absPos[1])
				indexMax 		= [i for i, x in enumerate(absPos) if x == max(absPos)][0]

				for i in range(nbItePreablable):
					newPos[indexMax] += coeff[indexMax]
					self.add(newPos)

			# Puis la diagonale
			nbIte = min(absPos)
			for i in range(nbIte):
				newPos[0] += coeffX
				newPos[1] += coeffY
				self.add(newPos)

		self.lastTime = time
		self.lastPos  = pos 

	def add(self,pos):
		if len(self.list) < self.valueMax :
			time = pygame.time.get_ticks()
			barriere = Barriere(self.ecran,pos,time)
			self.list += [barriere]

	def update(self):
		for i,barriere in enumerate(self.list) :
			timeExisted = pygame.time.get_ticks() - barriere.time

			if timeExisted > BARRIER_TIME or barriere.hp < 1:
				self.list.pop(i)

		self.value = len(self.list)
		self.manaBar.update()

	def render(self):
		for barriere in self.list :
			barriere.render()
		self.manaBar.render()
