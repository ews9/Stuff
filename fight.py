import pygame
import random
import sys

pygame.init()


WIDTH = 1080 
HEIGHT = 1080
RED = (255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
BACKGROUND_COLOR=(0,0,0)
SPEED=5
jump_speed=10
fall_speed=10
myFont = pygame.font.SysFont("monospace", 50)

player1_size=50
player1_pos=[4*WIDTH/5,HEIGHT-2*player1_size]
player1_energy=0
score1=0
score2=0
player2_size=player1_size
player2_pos=[WIDTH/5,HEIGHT-2*player1_size]
player2_energy=0
jump_height=400
goal=5
previous_player1_position=player1_pos[0]
previous_player2_position=player2_pos[0]

screen= pygame.display.set_mode((WIDTH,HEIGHT))

game_over=False

clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
	p_x=player_pos[0]
	p_y=player_pos[1]
	e_x=enemy_pos[0]
	e_y=enemy_pos[1]
	if (e_x>= p_x and e_x<(p_x+player1_size)) or (p_x>= e_x and p_x< (e_x+player2_size)):
		if (e_y>= p_y and e_y<(p_y+player1_size)) or (p_y>= e_y and p_y< (e_y+player2_size)):
			return True
	return False

def boundary(player_pos):
	if player_pos[0]<0:
		player_pos[0]=0
	if player_pos[0]>WIDTH-player1_size:
		player_pos[0]=WIDTH-player1_size
	if player_pos[1]<0:
		player_pos[1]=0


while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player1_pos[1]==HEIGHT-2*player1_size:
				player1_energy+=jump_height
			if event.key == pygame.K_w and player2_pos[1]==HEIGHT-2*player2_size:
				player2_energy+=jump_height
	keys=pygame.key.get_pressed()
	if player1_energy>0:
		player1_pos[1]-=jump_speed
		player1_energy-=jump_speed
	if player2_energy>0:
		player2_pos[1]-=jump_speed
		player2_energy-=jump_speed
	if player1_energy==0:
		if player1_pos[1]<HEIGHT-2*player1_size:
			player1_pos[1]+=fall_speed
	if player2_energy==0:
		if player2_pos[1]<HEIGHT-2*player2_size:
			player2_pos[1]+=fall_speed
	if keys[pygame.K_RIGHT]:
		player1_pos[0]+=SPEED		
	if keys[pygame.K_d]:
		player2_pos[0]+=SPEED
	if keys[pygame.K_LEFT]:
		player1_pos[0]-=SPEED
	if keys[pygame.K_a]:
		player2_pos[0]-=SPEED
	if keys[pygame.K_DOWN] and player1_pos[1]<HEIGHT-2*player1_size:
		player1_energy=0
		player1_pos[1]+=fall_speed
	if keys[pygame.K_s] and player2_pos[1]<HEIGHT-2*player2_size:
		player2_energy=0
		player2_pos[1]+=fall_speed
	BACKGROUND_COLOR=(0,0,0)
	
	boundary(player1_pos)
	boundary(player2_pos)
	clock.tick(120)
	screen.fill(BACKGROUND_COLOR)
	label1=myFont.render(str(score1), 1, RED)
	screen.blit(label1, (WIDTH-100,200))
	label2=myFont.render(str(score2), 1, BLUE)
	screen.blit(label2, (100,200))
	pygame.draw.rect(screen, GREEN, (0, HEIGHT-player1_size, WIDTH, HEIGHT-2*player1_size))
	pygame.draw.rect(screen, RED, (player1_pos[0],player1_pos[1], player1_size, player1_size))
	pygame.draw.rect(screen, BLUE, (player2_pos[0],player2_pos[1], player2_size, player2_size))	
	pygame.display.update()
	if detect_collision(player1_pos,player2_pos):
		if player1_pos[1]<player2_pos[1] and player1_energy==0 and player1_pos[0]<player2_pos[0]+player2_size-2*SPEED and player1_pos[0]>player2_pos[0]-player2_size+2*SPEED:
			score1+=1
			player1_pos=[4*WIDTH/5,HEIGHT-2*player1_size]
			player2_pos=[WIDTH/5,HEIGHT-2*player1_size]
		elif player2_pos[1]<player1_pos[1] and player2_energy==0 and player2_pos[0]<player1_pos[0]+player1_size-2*SPEED and player2_pos[0]>player1_pos[0]-player1_size+2*SPEED:
			score2+=1
			player1_pos=[4*WIDTH/5,HEIGHT-2*player1_size]
			player2_pos=[WIDTH/5,HEIGHT-2*player1_size]
		else:
			player1_pos[0]=previous_player1_position
			player2_pos[0]=previous_player2_position		
	if score1==5 or score2==5:
		game_over=True
	previous_player1_position=player1_pos[0]
	previous_player2_position=player2_pos[0]