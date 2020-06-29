import pygame
import random
import sys
import time

pygame.init()
WIDTH=750
HEIGHT=1000
numberofballs=50
#color= [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(numberofballs)]
x=[random.randint(160,255) for i in range(numberofballs)]
color= [(x[i],x[i],x[i]) for i in range(numberofballs)]
#color=[(255,255,255) for i in range(numberofballs)]
speed=1
maxdirection=5
goodlist=[-5,-4,-3,-2,-1,1,2,3,4,5]
position=[[WIDTH/2+random.randint(-WIDTH/3,WIDTH/3), HEIGHT/2+random.choice([-1,1])*(HEIGHT/2-20)+random.randint(-10,10)] for i in range(numberofballs)]
direction=[[random.choice(goodlist),random.choice(goodlist)] for i in range(numberofballs)]
#direction=[[5,8] for i in range(numberofballs)]
radius=10
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 50)

yourspeed=5
yourposition=[WIDTH/2,HEIGHT/2]
yourcolor=(255,0,0)
yourradius=5

borderwidth=100
borderheight=100

CONTROL=0  #0 for keyboard, 1 for joystick



def random_update_direction(direction,position):
	if position[0]<=radius:
		direction[0]=random.randint(1,maxdirection)
	if position[1]<=radius:
		direction[1]=random.randint(1,maxdirection)
	if position[0]>=WIDTH-radius:
		direction[0]=random.randint(-maxdirection,-1)
	if position[1]>HEIGHT-radius:
		direction[1]=random.randint(-maxdirection,-1)
	return direction


def reset_position():
	global position
	#position=[[WIDTH/2+random.randint(-WIDTH/3,WIDTH/3), 13+random.randint(-10,30)] for i in range(numberofballs)]
	#position=[[WIDTH/2, 13+random.randint(-10,30)] for i in range(numberofballs)]
	#position=[[WIDTH/2+random.randint(-WIDTH/2,WIDTH/2), 13+random.randint(-10,30)] for i in range(numberofballs)]
	#position=[[WIDTH/2+random.randint(-40,40), 13+random.randint(-10,30)] for i in range(numberofballs)]
	position=[[WIDTH/2+random.randint(-WIDTH/3,WIDTH/3), HEIGHT/2+random.choice([-1,1])*(HEIGHT/2-20)+random.randint(-10,10)] for i in range(numberofballs)]



def collision_detection():
	global yourposition
	global position
	global yourradius
	global radius
	distance=radius+yourradius
	for i in position:
		if (yourposition[0]-i[0])*(yourposition[0]-i[0])+(yourposition[1]-i[1])*(yourposition[1]-i[1])<distance*distance:
			return True
	return False

def fix_position():
	global yourposition
	if yourposition[0]>WIDTH/2+borderwidth-yourradius:
		yourposition[0]=WIDTH/2+borderwidth-yourradius
	if yourposition[0]<WIDTH/2-borderwidth+yourradius:
		yourposition[0]=WIDTH/2-borderwidth+yourradius
	if yourposition[1]<HEIGHT/2-borderheight+yourradius:
		yourposition[1]=HEIGHT/2-borderheight+yourradius
	if yourposition[1]>HEIGHT/2+borderheight-yourradius:
		yourposition[1]=HEIGHT/2+borderheight-yourradius

over=0
start_time=pygame.time.get_ticks()
pause=False
pygame.joystick.init()

if CONTROL==1:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()

while not game_over:
	clock.tick(60)
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	if CONTROL==0:
		keys=pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			yourposition[0]=yourposition[0]+yourspeed
		if keys[pygame.K_LEFT]:
			yourposition[0]=yourposition[0]-yourspeed
		if keys[pygame.K_UP]:
			yourposition[1]=yourposition[1]-yourspeed
		if keys[pygame.K_DOWN]:
			yourposition[1]=yourposition[1]+yourspeed	

	if CONTROL==1:
		hat=joystick.get_hat(0)
		yourposition[0]=yourposition[0]+yourspeed*hat[0]
		yourposition[1]=yourposition[1]-yourspeed*hat[1]	
		# x_axis=joystick.get_axis(0)
		# y_axis=joystick.get_axis(1)
		# x=int(round(x_axis*yourspeed))
		# y=int(round(y_axis*yourspeed))
		# yourposition[0]=yourposition[0]+x
		# yourposition[1]=yourposition[1]+y
	fix_position()
	message=str((pygame.time.get_ticks()-start_time)/1000.0)+' s'
	screen.blit(myFont.render(message,1 , (255,255,255)), (WIDTH-250,HEIGHT-150))
	for i in range(numberofballs):
		direction[i]=random_update_direction(direction[i], position[i])
		position[i][0]+=speed*direction[i][0]
		position[i][1]+=speed*direction[i][1]
		pygame.draw.circle(screen, color[i], position[i], radius)
	pygame.draw.circle(screen,yourcolor,yourposition,yourradius)
	pygame.draw.line(screen,(0,255,0),(WIDTH/2-borderwidth,HEIGHT/2-borderheight),(WIDTH/2+borderwidth,HEIGHT/2-borderheight),1)
	pygame.draw.line(screen,(0,255,0),(WIDTH/2-borderwidth,HEIGHT/2-borderheight),(WIDTH/2-borderwidth,HEIGHT/2+borderheight),1)
	pygame.draw.line(screen,(0,255,0),(WIDTH/2+borderwidth,HEIGHT/2+borderheight),(WIDTH/2+borderwidth,HEIGHT/2-borderheight),1)
	pygame.draw.line(screen,(0,255,0),(WIDTH/2+borderwidth,HEIGHT/2+borderheight),(WIDTH/2-borderwidth,HEIGHT/2+borderheight),1)
	if collision_detection():
		over=1
	if over==1:
		score=pygame.time.get_ticks()-start_time
		screen.blit(myFont.render("Score:"+str(score),1 , (255,255,255)), (WIDTH/2-125,0))
		over=0
		pause=True
		pygame.display.update()
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key!=pygame.K_UP and event.key!=pygame.K_LEFT and event.key!=pygame.K_RIGHT and event.key!=pygame.K_DOWN:			
					pause=False
					reset_position()
					yourposition=[WIDTH/2,HEIGHT/2]
					start_time=pygame.time.get_ticks()

		if CONTROL==1:	
			x=joystick.get_button(7)
			if x==1:
				pause=False
				reset_position()
				yourposition=[WIDTH/2,HEIGHT/2]
				start_time=pygame.time.get_ticks()


	pygame.display.update()
