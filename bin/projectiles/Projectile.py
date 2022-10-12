import pygame, math, random

class Projectile(object):
	def __init__(self, name:str, movementSpeed:int, 
		damage:int, skin:str, move:callable):

		self.movementSpeed = movementSpeed
		self.damage = damage
		self.rect = None
		self.skin = pygame.image.load(skin)
		self.move = move


	def setDirection(self, direction:str, initialPosition:list[int]):
		self.direction = direction
		if direction == "Right":			
			self.position = initialPosition
			self.position[0] += 98
			self.position[1] += 18

		else:			
			self.position = initialPosition
			self.position[0] -= 10
			self.position[1] += 18
	
	def move(self):
		raise Exception("Move function unassigned")

	def inflictDamage(self, player):
		player.health -= self.damage

def commonProjectileMove(projectile):
	if projectile.position[0] < -12 or projectile.position[0] > 802:
		return 

	if projectile.direction == "Right":
		projectile.position[0] += projectile.movementSpeed
	else:
		projectile.position[0] -= projectile.movementSpeed


def harmonicProjectileMove(projectile):
	if projectile.position[0] < -12 or projectile.position[0] > 802:
		return 

	if projectile.direction == "Right":
		projectile.position[0] += projectile.movementSpeed
		projectile.position[1] += 10*math.sin(projectile.position[0]*math.pi/30)
	else:
		projectile.position[0] -= projectile.movementSpeed
		projectile.position[1] += 10*math.sin(projectile.position[0]*math.pi/30)

### Slippery Projectile ####


class SlipperyProjectile(Projectile):
	def __init__(self, name: str, movementSpeed: int, damage: int, skin: str, move: callable):		
		self.stoppedTime = 0
		self.stopTime = 0
		super().__init__(name, movementSpeed, damage, skin, move)
	
	def setDirection(self, direction: str, initialPosition: list[int]):
		super().setDirection(direction, initialPosition)
		self.initialPosition = initialPosition[:]
		self.gradient = getGradient(self.position, self.direction)

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

def slipperyProjectileMove(projectile):

	if projectile.position[0] < -12 or projectile.position[0] > 802:
		return 

	if projectile.direction == "Right":
		if stopProjectile(projectile, projectile.position, projectile.stopTime, 
			projectile.stoppedTime, projectile.direction):
			return

		projectile.position[0] += projectile.movementSpeed

		if projectile.position[0] > 350:

			projectile.position[1] = (projectile.gradient*(projectile.position[0] - 350) 
				+ projectile.initialPosition[1])

		
	else:
		if stopProjectile(projectile, projectile.position, projectile.stopTime, 
			projectile.stoppedTime, projectile.direction):
			return

		projectile.position[0] -= projectile.movementSpeed

		if projectile.position[0] < 450:

			projectile.position[1] = (projectile.gradient*(projectile.position[0] - 450) 
				+ projectile.initialPosition[1])
