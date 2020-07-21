import pygame
import random
import sys
import time
import math

pygame.init()

WIDTH=1000
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 50)
BACKGROUNDCOLOR=[200,200,200]
gap=160 #gap between cups
cupsize=100 #side length
cupnumber=3
steps=200
firstxposition=WIDTH/2-cupnumber*gap/2+20
cupyposition=HEIGHT/2-cupsize


def randomswaps():
	global steps
	mylist=[]
	for i in range(steps):
		x=random.randint(0,cupnumber-1)
		y=random.randint(1,cupnumber-1)
		mylist.append([x,(x+y)%cupnumber])
	return mylist

def displaychosen(chosencup):
	position=[firstxposition+i*gap for i in range(cupnumber)]
	for j in range(cupnumber):
			if j!= chosencup:
					pygame.draw.rect(screen, [0,0,0], (position[j], cupyposition, cupsize, cupsize))
	pygame.draw.rect(screen, [255,0,0], (position[chosencup], cupyposition, cupsize, cupsize))
	pygame.display.update()
	time.sleep(1)

 
initialsmoothness=12

moving=0
def animation(first,second):  #move then "shadow reset"
	position=[firstxposition+i*gap for i in range(cupnumber)]
	radius=abs(position[first]-position[second])/2
	center=(position[first]+position[second])/2
	pi=math.pi

	for i in range(smoothness+1):
		screen.fill(BACKGROUNDCOLOR)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		clock.tick(60)

		if first>second:
			newfirst=[center+int(math.cos(i*pi/smoothness)*radius),cupyposition-int(math.sin(i*pi/smoothness)*radius)]
			newsecond=[center-int(math.cos(i*pi/smoothness)*radius),cupyposition+int(math.sin(i*pi/smoothness)*radius)]
		else:
			newfirst=[center+int(math.cos(i*pi/smoothness)*radius),cupyposition+int(math.sin(i*pi/smoothness)*radius)]
			newsecond=[center-int(math.cos(i*pi/smoothness)*radius),cupyposition-int(math.sin(i*pi/smoothness)*radius)]
		for j in range(cupnumber):
			if j!=first and j!= second:
					pygame.draw.rect(screen, [0,0,0], (position[j], cupyposition, cupsize, cupsize))
		pygame.draw.rect(screen, [0,0,0], (newfirst[0], newfirst[1], cupsize, cupsize))
		pygame.draw.rect(screen, [0,0,0], (newsecond[0], newsecond[1], cupsize, cupsize))
		pygame.display.update()


stop=0
while not game_over:
	screen.fill(BACKGROUNDCOLOR)
	randomswap=randomswaps()
	chosencup=random.randint(0,cupnumber-1)
	permutation=[i for i in range(cupnumber)]
	smoothness=initialsmoothness
	displaychosen(chosencup)
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	for x in randomswap:
		animation(x[0],x[1])
		permutation[x[0]],permutation[x[1]]=permutation[x[1]],permutation[x[0]]
		#smoothness=smoothness-1            #enable for gradual increase in speed
	choosing=1
	newposition=permutation.index(chosencup)
	while choosing==1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type==pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if pos[0]>firstxposition+newposition*gap and pos[0]<firstxposition+newposition*gap+cupsize and pos[1]<cupyposition+cupsize and pos[1]>cupyposition:
					screen.blit(myFont.render("Win",1 , (0,0,0)), (WIDTH/2-50,0))
				else:
					screen.blit(myFont.render("Lose",1 , (0,0,0)), (WIDTH/2-50,0))
				pygame.draw.rect(screen, [255,0,0], (firstxposition+newposition*gap, cupyposition, cupsize, cupsize))
				pygame.display.update()
				stop=1
				choosing=0
		while stop==1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type==pygame.KEYDOWN:
					stop=0	
	pygame.display.update()

