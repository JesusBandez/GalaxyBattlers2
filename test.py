import pygame
from pygame.locals import *
import time
pygame.init()

reloj = pygame.time.Clock()


while True:

	time.sleep(1)
	reloj.tick()

	print(reloj.get_time())