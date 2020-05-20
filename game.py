import pygame
from pygame.locals import *
from ship import *
from draw import *
from movement import *
from sys import *



pygame.init()

window = pygame.display.set_mode((800,600))

fondo = pygame.image.load("Background/Background.png")
window.blit(fondo, (0,0))

player1 = Ship("Right")
player2 = Ship("Left")
shellsInGame = []

framerateClock = pygame.time.Clock()

while player1.health > 0 and player2.health > 0:

	keys = pygame.key.get_pressed()

	moveShips(player1, player2, keys)
	shellsInGame += shoots(player1, player2, keys)


	for event in pygame.event.get():
		if event.type == QUIT:
			exit()


	window.blit(fondo, (0,0))
	drawShips(player1, player2, window)
	drawShells(shellsInGame, window)
	moveShells(shellsInGame, player1, player2)
	
	pygame.display.flip()

	framerateClock.tick(60)



