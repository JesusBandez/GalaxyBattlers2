import pygame, math


class HarmonicProjectile(object):
	def __init__(self, direction:str, initialPosition:list):
		self.direction = direction		
		self.movementSpeed = 3
		if direction == "Right":			
			self.skin = pygame.image.load("Shells/HarmonicProjectileSkin.png")
			self.position = initialPosition
			self.position[0] += 98
			self.position[1] += 18
		else:			
			self.skin = pygame.image.load("Shells/HarmonicProjectileSkin.png")
			self.position = initialPosition
			self.position[0] -= 10
			self.position[1] += 18
		self.attackDamage = 1
		self.rect = None

	def move(self):
		if self.position[0] < -12 or self.position[0] > 802:
			return 

		if self.direction == "Right":
			self.position[0] += self.movementSpeed
			self.position[1] += 10*math.sin(self.position[0]*math.pi/30)
		else:
			self.position[0] -= self.movementSpeed
			self.position[1] += 10*math.sin(self.position[0]*math.pi/30)

	def inflictDamage(self, player):
		player.health -= self.attackDamage
		