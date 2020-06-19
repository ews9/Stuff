import pygame
import random
import sys
import time

pygame.init()
WIDTH=1600
HEIGHT=700
numberofballs=random.randint(15,25)
color= [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(numberofballs)]
color= [(random.randint(160,255),0,0) for i in range(numberofballs)]
speed=1
position=[[WIDTH/2, HEIGHT/2] for i in range(numberofballs)]
direction=[[random.randint(-10,10),random.randint(-10,10)] for i in range(numberofballs)]
#direction=[[5,8] for i in range(numberofballs)]
radius=10
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 50)



def update_direction(direction, position):
	if position[0]<=radius:
		direction[0]=-direction[0]
	if position[1]<=radius:
		direction[1]=-direction[1]
	if position[0]>=WIDTH-radius:
		direction[0]=-direction[0]
	if position[1]>HEIGHT-radius:
		direction[1]=-direction[1]
	return direction

def random_update_direction(direction,position):
	if position[0]<=radius:
		direction[0]=random.randint(1,15)
	if position[1]<=radius:
		direction[1]=random.randint(1,15)
	if position[0]>=WIDTH-radius:
		direction[0]=random.randint(-15,-1)
	if position[1]>HEIGHT-radius:
		direction[1]=random.randint(-15,-1)
	return direction

guess=0
over=0

while not game_over:
	clock.tick(60)
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				guess=guess-1
			if event.key==pygame.K_RIGHT:
				guess=guess+1
			if event.key==pygame.K_SPACE:
				over=1

	if guess<0:
		guess=0
	screen.blit(myFont.render(str(guess),1 , (255,255,255)), (WIDTH-100,HEIGHT-50))
	for i in range(numberofballs):
		direction[i]=random_update_direction(direction[i], position[i])
		position[i][0]+=speed*direction[i][0]
		position[i][1]+=speed*direction[i][1]
		pygame.draw.circle(screen, color[i], position[i], radius)
	if over==1:
		if guess==numberofballs:
			screen.blit(myFont.render("You Win!",1 , (255,255,255)), (WIDTH/2-100,HEIGHT/2-100))
		else:
			screen.blit(myFont.render("You Lose!",1 , (255,255,255)), (WIDTH/2-100,HEIGHT/2-100))
			screen.blit(myFont.render("Number of balls:"+str(numberofballs),1 , (255,255,255)), (0,HEIGHT-50))
	pygame.display.update()
