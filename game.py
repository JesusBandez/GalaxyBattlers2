import pygame
from pygame.locals import *
from sys import *

import bin.ship as ship
import bin.draw as draw
import bin.movement as movement


pygame.init()

window = pygame.display.set_mode((800,600))

fondo = pygame.image.load("sprites/Background/Background.png")
window.blit(fondo, (0,0))

player1 = ship.Ship("Right")
player2 = ship.Ship("Left")
shellsInGame = []

framerateClock = pygame.time.Clock()

while player1.health > 0 and player2.health > 0:

	keys = pygame.key.get_pressed()

	movement.moveShips(player1, player2, keys)
	shellsInGame += movement.shoots(player1, player2, keys)


	for event in pygame.event.get():
		if event.type == QUIT:
			exit()


	window.blit(fondo, (0,0))
	draw.drawShips(player1, player2, window)
	draw.drawShells(shellsInGame, window)
	movement.moveShells(shellsInGame, player1, player2)
	
	pygame.display.flip()

	framerateClock.tick(60)



