from pygame.locals import *

def moveShells(shells, player1, player2):
	for projectile in shells:
		projectile.move()
		if projectile.direction == "Right":
			if projectile.rect.colliderect(player2.rect):
				projectile.position = [801, 300]
				projectile.inflictDamage(player2)
		
		if projectile.direction == "Left":
			if projectile.rect.colliderect(player1.rect):
				projectile.position = [-10, 300]
				projectile.inflictDamage(player1)



def moveShips(player1, player2, keys):
	if keys[K_a]:
		player1.move("UP")		

	if keys[K_d]:
		player1.move("DOWN")
	
	if keys[K_LEFT]:
		player2.move("DOWN")

	if keys[K_RIGHT]:
		player2.move("UP")
	
	player1.sprint(keys[K_LSHIFT], 5)	
	player2.sprint(keys[K_RSHIFT], 5)

	player1.reduction(keys[K_f])
	player2.reduction(keys[K_l])



def shoots(player1, player2, keys):
	shells = []
	if keys[K_w]:
		projectile = player1.shoot()
		if projectile is not None:
			shells.append(projectile)

	if keys[K_UP]:
		projectile = player2.shoot()
		if projectile is not None:
			shells.append(projectile)

	if keys[K_q]:
		projectile = player1.shootHarmonic()
		if projectile is not None:
			shells.append(projectile)

	if keys[K_DOWN]:
		projectile = player2.shootHarmonic()
		if projectile is not None:
			shells.append(projectile)

	if keys[K_e]:
		projectile = player1.shootSlippery()
		if projectile is not None:
			shells.append(projectile)

	if keys[K_KP0]:
		projectile = player2.shootSlippery()
		if projectile is not None:
			shells.append(projectile)

	return shells


		
