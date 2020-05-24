from commonProjectile import *
from harmonicProjectile import *
from slipperyProjectile import *
import pygame

def timeInRange(timeInSprint, maxTime):
	return timeInSprint <= maxTime

class Ship(object):
	def __init__(self, direction):
		self.direction = direction
		self.health = 4
		self.attackSpeed = 500
		self.timeSinceLastShot = self.attackSpeed - 100
		self.attackTimer = pygame.time.Clock()
		self.movementSpeed = 2	

		if direction == "Right":			
			self.position = [30, 277]
			self.skin = pygame.image.load("Ships/ShipSkin.png")
		else:
			self.position = [670, 277]
			self.skin = pygame.image.load("Ships/ShipSkin.png")

		self.rect = None
		self.sprintingTime = 0
		self.maxTime = 1500
		self.sprinting = False
		self.resting = False
		self.sprintClock = pygame.time.Clock()
		

	def move(self, direction):
		if direction == "UP":
			self.position[1] -= self.movementSpeed
		else:
			self.position[1] += self.movementSpeed

	def sprint(self, key, speedIncrease):
		tick = self.sprintClock.tick()
		
		if (key and timeInRange(self.sprintingTime, self.maxTime)
			and not self.sprinting and not self.resting):
			self.movementSpeed += speedIncrease
			self.updateTime("UP", tick)
			self.sprinting = True

		elif (key and timeInRange(self.sprintingTime, self.maxTime)
			and self.sprinting and not self.resting):
			self.updateTime("UP", tick)

		elif (not timeInRange(self.sprintingTime, self.maxTime)
			and not self.resting):
			self.updateTime("DOWN", tick)
			self.sprinting = False
			self.resting = True
			self.movementSpeed -= speedIncrease

		elif (not key and timeInRange(self.sprintingTime, self.maxTime)
			and self.sprinting and not self.resting):
			
			self.movementSpeed -= speedIncrease
			self.updateTime("DOWN", tick)
			self.sprinting = False		

		elif (timeInRange(self.sprintingTime, self.maxTime) 
			and not self.sprinting and not self.resting):
			
			self.updateTime("DOWN", tick)

		elif self.resting:
			
			self.updateTime("DOWN", tick)
			if self.sprintingTime <= 0:
				self.resting = False
				self.sprintingTime = 0


	def shoot(self):
		tick = self.attackTimer.tick()
		self.timeSinceLastShot += tick
		
		if self.attackSpeed - self.timeSinceLastShot <= 0:
			initialPosition = self.position[:]
			projectile = CommonProjectile(self.direction, initialPosition)
			self.timeSinceLastShot = 0
			return projectile

	def shootHarmonic(self):
		tick = self.attackTimer.tick()
		self.timeSinceLastShot += tick
		if self.attackSpeed - self.timeSinceLastShot <= 0:
			initialPosition = self.position[:]
			projectile = HarmonicProjectile(self.direction, initialPosition)			
			self.timeSinceLastShot = 0
			return projectile

	def shootSlippery(self):
		tick = self.attackTimer.tick()	
		self.timeSinceLastShot += tick
		if self.attackSpeed - self.timeSinceLastShot <= 0:
			initialPosition = self.position[:]
			projectile = SlipperyProjectile(self.direction, initialPosition)			
			self.timeSinceLastShot = 0
			return projectile

	def updateTime(self, increase, timeSinceLastCall):
		if self.sprintingTime < 0 and increase == "DOWN":
			return

		if increase is "UP":
			self.sprintingTime += timeSinceLastCall

		else:
			self.sprintingTime -= timeSinceLastCall




