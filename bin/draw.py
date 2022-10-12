import pygame

def drawShips(ship1, ship2, window):
	positions = []
	ships = [ship1, ship2]	
	for ship in ships:

		skin = ship.skin
		position = (ship.position[0], ship.position[1])
		position = window.blit(skin, position)
		ship.rect = position
		positions.append(positions)
	return positions

def drawShells(shells, window):
	shellsInGame = []
	for projectile in shells:
		skin = projectile.skin
		position = (projectile.position[0], projectile.position[1])
		position = window.blit(skin, position)
		projectile.rect = position
		shellsInGame.append(position)
	return shellsInGame