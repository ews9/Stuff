import pygame
import random
import sys
import time


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
WIDTH = 700
HEIGHT = 1050
BACKGROUND_COLOR=(255,255,255)
BLOCK_COLOR=(0,0,0)
myFont = pygame.font.SysFont("dejavuserif", 50)
easy=1	

tap_sound=pygame.mixer.Sound("typewriter.wav")


screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
ROW=10
write_score=0

def newgame():
	if easy==1:
		x=random.randint(0,3)
		game=[]
		for i in range(25):
			x=(x+random.randint(1,3))%4
			game.append(x)
		return game
	else:
		game=[random.randint(0,3) for i in range(25)]
		return game

game=newgame()
start=0
win=0
playing=1
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	start=0
	win=0
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if start==0:
					start_time=pygame.time.get_ticks()
					start=1
				if event.key==pygame.K_d:
					if game[0]==0:
						game=game[1:]
						pygame.mixer.Sound.play(tap_sound)
					else:
						game_over=True
				if event.key==pygame.K_f:
					if game[0]==1:
						game=game[1:]
						pygame.mixer.Sound.play(tap_sound)
					else:
						game_over=True
				if event.key==pygame.K_j:
					if game[0]==2:
						game=game[1:]
						pygame.mixer.Sound.play(tap_sound)
					else:
						game_over=True
				if event.key==pygame.K_k:
					if game[0]==3:
						game=game[1:]
						pygame.mixer.Sound.play(tap_sound)
					else:
						game_over=True
				
		screen.fill(BACKGROUND_COLOR)
		pygame.draw.line(screen,(0,0,0),(WIDTH/4,0),(WIDTH/4,HEIGHT),1)
		pygame.draw.line(screen,(0,0,0),(2*WIDTH/4,0),(2*WIDTH/4,HEIGHT),1)
		pygame.draw.line(screen,(0,0,0),(3*WIDTH/4,0),(3*WIDTH/4,HEIGHT),1)
		for i in range(ROW):
			pygame.draw.line(screen,(0,0,0),(0,i*HEIGHT/ROW),(WIDTH,i*HEIGHT/ROW),1)
		m=min(ROW,len(game))
		for i in range(m):
			pygame.draw.rect(screen,BLOCK_COLOR,(game[i]*WIDTH/4,(ROW-1)*HEIGHT/ROW-i*HEIGHT/ROW,WIDTH/4,HEIGHT/ROW))
		
		if start==1:
			message=str((pygame.time.get_ticks()-start_time)/1000.0)+' s'
			screen.blit(myFont.render(message, True, (255,0,0)), (0.35*WIDTH,0))
		pygame.display.update()
		if len(game)==0:
			win=1
			final_time=(pygame.time.get_ticks()-start_time)/1000.0
			final_time_text=str(final_time)+' s'
			write_score=1
			game_over=True

	while game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_SPACE:
						game_over=False
						game=newgame()
		if win==1:
			if write_score==1:
				f=open('highscore.txt', 'rU')
				i=0
				for line in f:
					if final_time<=float(line):
						break
					i=i+1
				f.close()
				f=open('highscore.txt', 'rU')
				line_number=1
				for line in f:
					line_number+=1
				f.close()
				f=open('highscore.txt', 'rU')
				contents=f.readlines()
				contents.insert(i, str(final_time)+'\n')
				f.close()
				f=open('highscore.txt','w')
				contents="".join(contents)
				f.write(contents)
				f.close()
				write_score=0
			screen.fill((0,255,0))
			final_time_render=myFont.render(final_time_text, True, (0,0,0))
			final_time_rect=final_time_render.get_rect(center=(WIDTH/2, 0.4*HEIGHT))
			screen.blit(final_time_render, final_time_rect)
			if i==0:
				newbest_render=myFont.render("New Best!", True, (0,0,0))
				newbest_rect=newbest_render.get_rect(center=(WIDTH/2,0.35*HEIGHT))
				screen.blit(newbest_render, newbest_rect)
			placement_text=str(i+1)+'/'+str(line_number)
			placement_render=myFont.render(placement_text, True, (0,0,0))
			placement_rect=placement_render.get_rect(center=(WIDTH/2,0.45*HEIGHT))
			screen.blit(placement_render, placement_rect)
			percentile=100-round((float(i+1)/line_number)*100,2)
			percentile_render=myFont.render(str(percentile)+'%', True, (0,0,0))
			percentile_rect=percentile_render.get_rect(center=(WIDTH/2,0.5*HEIGHT))
			screen.blit(percentile_render, percentile_rect)
			screen.blit(myFont.render('Space to restart', True, (0,0,0)), (0.20*WIDTH,0.95*HEIGHT))
			pygame.display.update()
		else:
			screen.fill((255,0,0))
			screen.blit(myFont.render('Space to restart', True, (0,0,0)), (0.20*WIDTH,0.95*HEIGHT))
			pygame.display.update()
	clock.tick(60)

