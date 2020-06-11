import pygame
import random
import sys
import time

pygame.init()
WIDTH=1920
HEIGHT=1080
screen= pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()




for i in range(WIDTH):
	for j in range(HEIGHT):
		pygame.draw.circle(screen,(random.randint(0,100),random.randint(0,100),random.randint(0,100)),(i,j),0)
pygame.display.update()

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_c:
				pygame.image.save(screen, "random.tga")
