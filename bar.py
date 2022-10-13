import pygame

class Bar:
	def __init__(self):
		[self.innerColor,self.edgeColor] = self.colors 

		self.innerInit = self.inner =  pygame.Rect((0,0),self.size) 
		self.edge = self.inner.inflate(self.thick*2,self.thick*2)

		self.maxValue = self.value
		self.midValue = self.maxValue / 2
		self.chunkSize = int(self.inner.width / self.maxValue)

	def updatePos(self):

		if self.posAbsolue :
			self.edge.topleft = self.inner.topleft = self.pos

		else :
			self.edge.midbottom = self.pos
			self.edge.y -= self.offset
			
		self.inner.y = self.edge.y + self.thick
		self.inner.x = self.edge.x + self.thick

	def updateColor(self):
		# Le vert tends vers le jaune
		if(self.value > self.midValue):
			colorVar = 255 - int(255 / self.midValue) * (self.value - self.maxValue//2)
			self.innerColor = [colorVar,255,0]

		elif (self.value == self.midValue):
			self.innerColor = [255,255,0]

		# Le jaune tends vers le rouge
		else:
			colorVar = int(255 / self.midValue) * self.value
			self.innerColor = [255,colorVar,0]

	def render(self):
		if self.value > 0:
			pygame.draw.rect(self.ecran,self.edgeColor,self.edge)
			pygame.draw.rect(self.ecran,self.innerColor,self.inner)