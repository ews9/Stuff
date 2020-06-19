import pygame
import random
import sys
import time

pygame.init()


WIDTH = 1080 
HEIGHT = 1080
RED = (255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
BACKGROUND_COLOR=(0,0,0)
SPEED=30
jump_speed=40
fall_speed=40
myFont = pygame.font.SysFont("monospace", 50)
winner=0
player1_size=50
player1_pos=[WIDTH/5,HEIGHT-2*player1_size]
player1_energy=0
score1=0
score2=0
enemy_size=player1_size
enemy_pos=[4*WIDTH/5,HEIGHT-2*enemy_size]
enemy_energy=0
enemy_radar=0
jump_height=400
goal=5

screen= pygame.display.set_mode((WIDTH,HEIGHT))

game_over=False

clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
	p_x=player_pos[0]
	p_y=player_pos[1]
	e_x=enemy_pos[0]
	e_y=enemy_pos[1]
	if (e_x>= p_x and e_x<(p_x+player1_size)) or (p_x>= e_x and p_x< (e_x+enemy_size)):
		if (e_y>= p_y and e_y<(p_y+player1_size)) or (p_y>= e_y and p_y< (e_y+enemy_size)):
			return True
	return False

def boundary(player_pos):
	if player_pos[0]<0:
		player_pos[0]=0
	if player_pos[0]>WIDTH-player1_size:
		player_pos[0]=WIDTH-player1_size
	if player_pos[1]<0:
		player_pos[1]=0



def enemy_jump():
	global enemy_energy
	if enemy_pos[1]==HEIGHT-2*enemy_size:
		enemy_energy+=jump_height


while not game_over:
	SPEED=30
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player1_pos[1]==HEIGHT-2*player1_size:
				player1_energy+=jump_height
	keys=pygame.key.get_pressed()
	
	if player1_energy>0:
		player1_pos[1]-=jump_speed
		player1_energy-=jump_speed
	if player1_energy==0:
		if player1_pos[1]<HEIGHT-2*player1_size:
			player1_pos[1]+=fall_speed
	if keys[pygame.K_RIGHT]:
		player1_pos[0]+=SPEED		
		if keys[pygame.K_SPACE]:
			player1_pos[0]+=2*SPEED	
	if keys[pygame.K_LEFT]:
		player1_pos[0]-=SPEED
		if keys[pygame.K_SPACE]:
			player1_pos[0]-=2*SPEED	
	if keys[pygame.K_DOWN] and player1_pos[1]<HEIGHT-2*player1_size:
		player1_energy=0
		player1_pos[1]+=fall_speed


	enemy_jump()
	if enemy_energy>0:
		enemy_pos[1]-=jump_speed
		enemy_energy-=jump_speed
	if enemy_energy==0:
		if enemy_pos[1]<HEIGHT-2*enemy_size:
			enemy_pos[1]+=fall_speed
	if enemy_pos[0]<player1_pos[0]-player1_size/2:
		enemy_pos[0]+=SPEED
	elif enemy_pos[0]>player1_pos[0]+player1_size/2:
		enemy_pos[0]-=SPEED
		


	BACKGROUND_COLOR=(0,0,0)
	
	boundary(player1_pos)
	boundary(enemy_pos)
	clock.tick(30)
	screen.fill(BACKGROUND_COLOR)
	label1=myFont.render(str(score1), 1, RED)
	screen.blit(label1, (100,200))
	label2=myFont.render(str(score2), 1, BLUE)
	screen.blit(label2, (WIDTH-100,200))
	if score1==goal:
		winner=1
	if score2==goal:
		winner=2
	if winner==1:
		labelwin=myFont.render("YOU WIN", 1, (255,255,255))
		screen.blit(labelwin, (WIDTH/2-100,HEIGHT/2))
	if winner==2:
		labellose=myFont.render("YOU LOSE", 1, (255,255,255))
		screen.blit(labellose, (WIDTH/2-100,HEIGHT/2))
	pygame.draw.rect(screen, GREEN, (0, HEIGHT-player1_size, WIDTH, HEIGHT-2*player1_size))
	pygame.draw.rect(screen, RED, (player1_pos[0],player1_pos[1], player1_size, player1_size))
	pygame.draw.rect(screen, BLUE, (enemy_pos[0],enemy_pos[1], enemy_size, enemy_size))	
	pygame.display.update()
	if winner>0:
		time.sleep(2)
		score1=0
		score2=0
		player1_pos=[WIDTH/5,HEIGHT-2*player1_size]
		enemy_pos=[4*WIDTH/5,HEIGHT-2*player1_size]
		winner=0
	if detect_collision(player1_pos,enemy_pos):
		if player1_pos[1]<enemy_pos[1] and player1_energy==0:
			score1+=1
			player1_pos=[WIDTH/5,HEIGHT-2*player1_size]
			enemy_pos=[4*WIDTH/5,HEIGHT-2*player1_size]

		if enemy_pos[1]<player1_pos[1] and enemy_energy==0:
			score2+=1
			player1_pos=[WIDTH/5,HEIGHT-2*player1_size]
			enemy_pos=[4*WIDTH/5,HEIGHT-2*player1_size]
	
