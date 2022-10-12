from pygame.locals import *
import bin.projectiles.Projectile as projectiles
from bin.projectiles.slipperyProjectile import SlipperyProjectile

def moveShells(shells, player1, player2):
	for projectile in shells:
		projectile.move(projectile)

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
	if keys[K_w] and player1.canShoot():		
		projectile = projectiles.Projectile("Common", 5, 1, 
			"sprites/Shells/CommonProjectilSkin.png", 
			projectiles.commonProjectileMove)
		player1.shoot(projectile)
		shells.append(projectile)
		
	if keys[K_UP] and player2.canShoot():
		
		projectile = projectiles.Projectile("Common", 5, 1, 
			"sprites/Shells/CommonProjectilSkin.png", 
			projectiles.commonProjectileMove)
		player2.shoot(projectile)
		shells.append(projectile)
		

	if keys[K_q] and player1.canShoot():

		projectile = projectiles.Projectile("Harmonic", 3, 1, 
			"sprites/Shells/HarmonicProjectileSkin.png", 
			projectiles.harmonicProjectileMove)
		player1.shoot(projectile)
		shells.append(projectile)

	if keys[K_DOWN] and player2.canShoot():

		projectile = projectiles.Projectile("Harmonic", 3, 1, 
			"sprites/Shells/HarmonicProjectileSkin.png", 
			projectiles.harmonicProjectileMove)
		player2.shoot(projectile)
		shells.append(projectile)

	if keys[K_e] and player1.canShoot():
		projectile = projectiles.SlipperyProjectile("Slippery", 10, 1, 
		"sprites/Shells/SlipperyProjectileSkin.png", projectiles.slipperyProjectileMove)
		player1.shoot(projectile)
		
		shells.append(projectile)

	if keys[K_KP0] and player2.canShoot():
		projectile = projectiles.SlipperyProjectile("Slippery", 10, 1, 
			"sprites/Shells/SlipperyProjectileSkin.png", projectiles.slipperyProjectileMove)
		player2.shoot(projectile)
		shells.append(projectile)

	return shells


		
