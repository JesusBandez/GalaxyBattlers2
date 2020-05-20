from commonProjectile import *
from harmonicProjectile import *
import pygame
class Ship(object):
	def __init__(self, direction):
		self.direction = direction
		self.health = 4
		self.attackSpeed = 500
		self.attackTimer = 0
		self.movementSpeed = 2	
		if direction == "Right":			
			self.position = [30, 277]
			self.skin = pygame.image.load("Ships/ShipSkin.png")
		else:
			self.position = [670, 277]
			self.skin = pygame.image.load("Ships/ShipSkin.png")
		self.rect = None


	def move(self, direction):
		if direction == "UP":
			self.position[1] -= self.movementSpeed
		else:
			self.position[1] += self.movementSpeed

	def shoot(self):
		tryToShoot = pygame.time.get_ticks()
		if tryToShoot - self.attackTimer >= self.attackSpeed:
			initialPosition = self.position[:]
			projectile = CommonProjectile(self.direction, initialPosition)
			self.attackTimer = tryToShoot
			return projectile

	def shootHarmonic(self):
		tryToShoot = pygame.time.get_ticks()
		if tryToShoot - self.attackTimer >= self.attackSpeed:
			initialPosition = self.position[:]
			projectile = HarmonicProjectile(self.direction, initialPosition)
			self.attackTimer = tryToShoot
			return projectile


