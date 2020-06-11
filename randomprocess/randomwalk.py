import pygame
import random
import sys
import time

pygame.init()
WIDTH=1920
HEIGHT=1080
color= (255,255,255)
speed=3
startingX=1500
startingY=540
position=[startingX,startingY]
radius=1
screen= pygame.display.set_mode((WIDTH,HEIGHT))
redtogreen=1
greentoblue=0
bluetored=0
game_over=False
shadow=[]
shadow_color=[]
shadow_length=10000
shadow_thickness=1
pause=0
clock = pygame.time.Clock()
previousX=position[0]
previousY=position[1]

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

def color_transform():     ##red to green to blue
	global color
	global redtogreen
	global greentoblue
	global bluetored
	if redtogreen==1:
		if color[1]==255:
			redtogreen=0
			greentoblue=1
		else:
			color=(color[0]-1,color[1]+1,0)
	if greentoblue==1:
		if color[2]==255:
			greentoblue=0
			bluetored=1
		else:
			color=(0,color[1]-1,color[2]+1)
	if bluetored==1:
		if color[0]==255:
			bluetored=0
			redtogreen=1
		else:
			color=(color[0]+1,0,color[2]-1)	

AtoB=1

def color_transform2():   ## red to white
	global color
	global AtoB
	if AtoB==1:
		if color[2]==0:
			AtoB =0
		else:
			color=(255,255,color[2]-1)
	if AtoB==0:
		if color[2]==255:
			AtoB =1
		else:
			color=(255,255,color[2]+1)



def boundary(position):
	if position[0]<=0:
		position[0]=0
	if position[1]<=0:
		position[1]=0
	if position[0]>=WIDTH:
		position[0]=WIDTH
	if position[1]>=HEIGHT:
		position[1]=HEIGHT
	return position

def circleboundary(position):
	if (position[0]-startingX)*(position[0]-startingX)+(position[1]-startingY)*(position[1]-startingY)>90000:
		position=[previousX,previousY]
	return position

while not game_over:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				pause=1-pause
			#if event.key==pygame.K_c:                       ##Take picture
			# 	pygame.image.save(screen, "screenshot.tga")
	if pause==0:
		for i in range(1000):
			x=random.randint(0,1)
			if x==0:
				y=random.randint(0,1)
				if y==0:
					position[0]+=speed*(4*random.randint(0,1)-2)
				else:
					position[1]+=speed*(4*random.randint(0,1)-2)
			else:
				position[0]+=speed*(2*random.randint(0,1)-1)
				position[1]+=speed*(2*random.randint(0,1)-1)
			position=circleboundary(position)
			previousX=position[0]
			previousY=position[1]
			color_transform2()
			#shadow_update()
			shadow.append(tuple(position))
			#shadow_color_update()
			shadow_color.append(tuple(color))
		screen.fill((0,0,20))
		for i in range(len(shadow)-1):
			pygame.draw.line(screen, list(shadow_color[i]), list(shadow[i]),list(shadow[i+1]), shadow_thickness)
		pygame.draw.circle(screen, color, position, radius)
		pygame.display.update()
