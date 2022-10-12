import pygame, math, random

def getGradient(initialPosition, direction):
	if direction == "Right":
		minGradient  = int(round(initialPosition[1]/-450, 3) * 1000)
		maxGradient= int(round((initialPosition[1] - 600)/-450, 3) * 1000)
		gradients = []

		for i in range(minGradient, maxGradient, 50):
			gradients.append(i)

	else:
		maxGradient= int(round(initialPosition[1]/450, 3) * 1000)
		minGradient = int(round((initialPosition[1] - 600)/450, 3) * 1000)
		gradients = []

		for i in range(minGradient, maxGradient, 50):
			gradients.append(i)

	return random.choice(gradients)/1000

def stopProjectile(projectile, position, stopTime, stoppedTime, direction):
	if direction == "Right":

		if position[0] > 350 and stopTime == 0:
			projectile.stopTime = pygame.time.get_ticks()

		projectile.stoppedTime = pygame.time.get_ticks() - projectile.stopTime
		if projectile.stoppedTime < 500:
			return True
		return False

	else:

		if position[0] < 450 and stopTime == 0:
			projectile.stopTime = pygame.time.get_ticks()

		projectile.stoppedTime = pygame.time.get_ticks() - projectile.stopTime

		if projectile.stoppedTime < 500:
			return True
		return False





class SlipperyProjectile(object):
	def __init__(self, direction:str, initialPosition:list):
		self.direction = direction		
		self.movementSpeed = 10
		self.initialPosition = initialPosition[:]
		if direction == "Right":			
			self.skin = pygame.image.load("sprites/Shells/SlipperyProjectileSkin.png")
			self.position = initialPosition
			self.position[0] += 98
			self.position[1] += 18
		else:			
			self.skin = pygame.image.load("sprites/Shells/SlipperyProjectileSkin.png")
			self.position = initialPosition
			self.position[0] -= 10
			self.position[1] += 18
		self.initialPosition = [self.position[0], self.position[1]]
		self.attackDamage = 1
		self.rect = None
		
		self.gradient = getGradient(self.position, self.direction)
		self.stoppedTime = 0
		self.stopTime = 0
	

		

	def move(self):
		if self.position[0] < -12 or self.position[0] > 802:
			return 

		if self.direction == "Right":
			if stopProjectile(self, self.position, self.stopTime, 
				self.stoppedTime, self.direction):
				return

			self.position[0] += self.movementSpeed

			if self.position[0] > 350:

				self.position[1] = (self.gradient*(self.position[0] - 350) 
					+ self.initialPosition[1])

			
		else:
			if stopProjectile(self, self.position, self.stopTime, 
				self.stoppedTime, self.direction):
				return

			self.position[0] -= self.movementSpeed

			if self.position[0] < 450:

				self.position[1] = (self.gradient*(self.position[0] - 450) 
					+ self.initialPosition[1])
			
	def inflictDamage(self, player):
		player.health -= self.attackDamage
	
		