import pygame
import random
import sys
import time

#shuffling: random trasposition, top to random, random to top

pygame.init()
WIDTH=1000
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
White=(255,255,255)
Black=(0,0,0)


thickness=3
cardwidth=200
cards=255    #factor of 255
colormultiplier=255/cards
deck=[i for i in range(cards)]
topleft=(WIDTH/2-cardwidth/2,100)

def randomtransposition():
	global deck
	x=random.randint(0,cards-1)
	y=random.randint(0,cards-1)
	cardx=deck[x]
	deck[x]=deck[y]
	deck[y]=cardx

def randomtotop():
	global deck
	x=random.randint(0,cards-1)
	cardx=deck[x]
	deck.pop(x)
	deck.insert(0,cardx)

def toptorandom():
	global deck
	x=random.randint(0,cards-1)
	cardx=deck[0]
	deck.pop(0)
	deck.insert(x,cardx)

pause=0

while not game_over:
	clock.tick(10)
	screen.fill(White)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				pause=1-pause
	if pause==0:
		randomtotop()
		for i in range(cards):
			pygame.draw.rect(screen, (0,deck[i]*colormultiplier,255-deck[i]*colormultiplier), (topleft[0],topleft[1]+i*thickness,cardwidth,thickness))
		pygame.display.update()
