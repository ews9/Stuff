import pygame
import random
import sys
import time

pygame.init()
WIDTH=1000
HEIGHT=1000
color= (200,0,0)
speed=1
position=[WIDTH/2, HEIGHT/2]
direction=[5,8]
radius=2
screen= pygame.display.set_mode((WIDTH,HEIGHT))
redtogreen=1
greentoblue=0
bluetored=0
game_over=False
shadow=[]
shadow_color=[]
shadow_length=10
shadow_thickness=3

clock = pygame.time.Clock()


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
		direction[0]=random.randint(1,20)
	if position[1]<=radius:
		direction[1]=random.randint(1,20)
	if position[0]>=WIDTH-radius:
		direction[0]=random.randint(-20,-1)
	if position[1]>HEIGHT-radius:
		direction[1]=random.randint(-20,-1)
	return direction

def shadow_color_update():
	if len(shadow_color)>=shadow_length:
		shadow_color.pop(0)
		shadow_color.append(tuple(color))
	else:
		shadow_color.append(tuple(color))

def shadow_update():
	if len(shadow)>=shadow_length:
		shadow.pop(0)
		shadow.append(tuple(position))
	else:
		shadow.append(tuple(position))

def color_transform():
	global color
	global redtogreen
	global greentoblue
	global bluetored
	if redtogreen==1:
		if color[1]==200:
			redtogreen=0
			greentoblue=1
		else:
			color=(color[0]-1,color[1]+1,0)
	if greentoblue==1:
		if color[2]==200:
			greentoblue=0
			bluetored=1
		else:
			color=(0,color[1]-1,color[2]+1)
	if bluetored==1:
		if color[0]==200:
			bluetored=0
			redtogreen=1
		else:
			color=(color[0]+1,0,color[2]-1)	


while not game_over:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	for i in range(10):
		direction=random_update_direction(direction, position)
		position[0]+=speed*direction[0]
		position[1]+=speed*direction[1]
		color_transform()
		shadow_update()
		shadow_color_update()
	screen.fill((0,0,0))
	for i in range(len(shadow)-1):
		pygame.draw.line(screen, list(shadow_color[i]), list(shadow[i]),list(shadow[i+1]), shadow_thickness)
	pygame.draw.circle(screen, color, position, radius)
	pygame.display.update()
