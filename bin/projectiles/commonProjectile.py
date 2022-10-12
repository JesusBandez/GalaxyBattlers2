import pygame

class CommonProjectile(object):
	def __init__(self, direction:str, initialPosition:list):
		self.direction = direction		
		self.movementSpeed = 5
		if direction == "Right":			
			self.skin = pygame.image.load("sprites/Shells/CommonProjectilSkin.png")
			self.position = initialPosition
			self.position[0] += 98
			self.position[1] += 18
		else:			
			self.skin = pygame.image.load("sprites/Shells/CommonProjectilSkin.png")
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
		else:
			self.position[0] -= self.movementSpeed

	def inflictDamage(self, player):
		player.health -= self.attackDamage
		