import pygame
import random
import sys
import time

order=3
rock=0
paper=1
scissor=2 
rockimage=pygame.image.load('rock.png')
paperimage=pygame.image.load('paper.png')
paperimage=pygame.transform.scale(paperimage,(520,520))
scissorimage=pygame.image.load('scissor.png')

def numbertobase3(num):
	global order
	if num<3:
		return [num]
	else:
		x=numbertobase3(num/3)
		x.append(num%3)
		return x

def base3toindex(base3):
	global order
	while len(base3)<order:
		base3.insert(0,0)
	return base3

def numbertoindex(num):
	return base3toindex(numbertobase3(num))

def rps(num):
	if num==0:
		return 'Rock'
	if num==1:
		return 'Paper'
	if num==2:
		return 'Scissor'



def initializeTP():   #[memory,rockweight,paperweight,scissorweight]
	global order
	index=3**order
	TP=[ [numbertoindex(i) ,1,1,1] for i in range(index)]
	return TP

def updateTP():
	global TP
	global memory
	global attack
	for i in TP:
		if memory==i[0]:
			i[attack+1]+=1


from numpy.random import choice

def updatedefense():
	global TP
	global memory
	for i in TP:
		if memory==i[0]:
			total=float(i[1]+i[2]+i[3])
			x=choice([0,1,2],1,p=[i[1]/total,i[2]/total,i[3]/total])
			return (x[0]+1)%3

TP=initializeTP()

memory=[0 for i in range(order)]

pygame.init()
WIDTH=1000
HEIGHT=800
myFont = pygame.font.SysFont("monospace", 50)
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
White=(255,255,255)
Black=(0,0,0)

attack=3
nextdefense=random.randint(0,2)
YourScore=0
CPUScore=0

screen.fill(White)
YourScoreLabel=myFont.render(str(YourScore), 1, Black)
CPUScoreLabel=myFont.render(str(CPUScore), 1, Black)
screen.blit(YourScoreLabel, (100,100))
screen.blit(CPUScoreLabel,(WIDTH-300,100))
pygame.display.update()

while not game_over:
	clock.tick(60)
	screen.fill(White)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_r:
				attack=0
			if event.key==pygame.K_p:
				attack=1
			if event.key==pygame.K_s:
				attack=2
	while attack<3:
		updateTP()
		memory.pop(0)
		memory.append(attack)
		screen.fill(White)
		if (attack-nextdefense)%3==1:
			YourScore+=1
		if (attack-nextdefense)%3==2:
			CPUScore+=1
		attackLabel=myFont.render(rps(attack), 1, Black)
		defenceLabel=myFont.render(rps(nextdefense),1,Black)	
		YourScoreLabel=myFont.render(str(YourScore), 1, Black)
		CPUScoreLabel=myFont.render(str(CPUScore), 1, Black)
		if attack==0:
			screen.blit(rockimage, (20,250))
		if attack==1:
			screen.blit(paperimage, (20,250))
		if attack==2:
			screen.blit(scissorimage, (20,250))
		if nextdefense==0:
			screen.blit(rockimage, (WIDTH-500,250))
		if nextdefense==1:
			screen.blit(paperimage, (WIDTH-500,250))
		if nextdefense==2:
			screen.blit(scissorimage, (WIDTH-500,250))
		screen.blit(attackLabel, (100,200))
		screen.blit(YourScoreLabel, (100,100))
		screen.blit(defenceLabel,(WIDTH-300,200))
		screen.blit(CPUScoreLabel,(WIDTH-300,100))
		attack=3
		nextdefense=updatedefense()
		pygame.display.update()

