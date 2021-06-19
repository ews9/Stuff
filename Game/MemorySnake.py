import pygame
import random
import sys
import time

pygame.init()
WIDTH=1010
HEIGHT=1010
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 50)


def arraygenerator(space,length): #space is odd so we can get center. NOTE: can get stuck so repeat if necessary. Length 1 means 2 boxes, ALSO need to return answer key
	boxarray=[[0 for i in range(space)] for j in range(space)]
	boxarray[(space-1)/2][(space-1)/2]=1
	current=[(space-1)/2,(space-1)/2]
	moves=[]
	for j in range(length): #check which candidates are valid, then pick randomly
		valid=['U','L','R','D']
		#check if U is valid
		if boxarray[current[0]][current[1]+1]==1 or boxarray[current[0]-1][current[1]+1]==1 or boxarray[current[0]+1][current[1]+1]==1 or boxarray[current[0]][current[1]+2]==1:
			valid.remove('U')
		if boxarray[current[0]-1][current[1]]==1 or boxarray[current[0]-1][current[1]+1]==1 or boxarray[current[0]-1][current[1]-1]==1 or boxarray[current[0]-2][current[1]]==1:
			valid.remove('L')
		if boxarray[current[0]+1][current[1]]==1 or boxarray[current[0]+1][current[1]+1]==1 or boxarray[current[0]+1][current[1]-1]==1 or boxarray[current[0]+2][current[1]]==1:
			valid.remove('R')
		if boxarray[current[0]][current[1]-1]==1 or boxarray[current[0]-1][current[1]-1]==1 or boxarray[current[0]+1][current[1]-1]==1 or boxarray[current[0]][current[1]-2]==1:
			valid.remove('D')
		if not valid:
			arraygenerator(space,length)
		else:
			move=random.choice(valid)
			moves.append(move)
			if move=='U':
				current[1]=current[1]+1		
			if move=='L':
				current[0]=current[0]-1
			if move=='R':
				current[0]=current[0]+1
			if move=='D':
				current[1]=current[1]-1
			boxarray[current[0]][current[1]]=1
	return boxarray, moves



def mazegenerator(thearray,radius):
	l=len(thearray)
	mid=(l-1)/2

	for i in range(l):
		for j in range(l):
			if thearray[i][j]==1:
				drawsquare([WIDTH/2+(i-mid)*2*radius,HEIGHT/2+(mid-j)*2*radius],radius)

def drawsquare(center,radius):
	pygame.draw.rect(screen,(100,100,100),[center[0]-radius,center[1]-radius,2*radius,2*radius], 0)
	pygame.draw.line(screen,(255,255,255),(center[0]-radius,center[1]-radius),(center[0]-radius,center[1]+radius),1)
	pygame.draw.line(screen,(255,255,255),(center[0]-radius,center[1]-radius),(center[0]+radius,center[1]-radius),1)
	pygame.draw.line(screen,(255,255,255),(center[0]+radius,center[1]+radius),(center[0]-radius,center[1]+radius),1)
	pygame.draw.line(screen,(255,255,255),(center[0]+radius,center[1]+radius),(center[0]+radius,center[1]-radius),1)


def drawsnake(start,moves,radius):
	current=start
	for m in moves:
		oldcurrent=current
		if m=='U':
			newcurrent=[oldcurrent[0],oldcurrent[1]-2*radius]
		if m=='D':
			newcurrent=[oldcurrent[0],oldcurrent[1]+2*radius]
		if m=='L':
			newcurrent=[oldcurrent[0]-2*radius,oldcurrent[1]]
		if m=='R':
			newcurrent=[oldcurrent[0]+2*radius,oldcurrent[1]]
		pygame.draw.line(screen,(255,0,0),oldcurrent, newcurrent, max(radius//10,1))
		current=newcurrent
	pygame.draw.circle(screen,(255,0,0), current, max(radius//4,2)) #snakehead

def lose():
	global level
	global answerkey
	answerkey=[]
	level=0
	screen.fill((255,0,0))

def extreme(maze):
	maxima=0
	l=len(maze)
	mid=(l-1)/2
	for i in range(l):
		for j in range(l):
			if maze[i][j]==1:
				maxima=max(maxima,i-mid,mid-i,j-mid,mid-j)
	return maxima


# def drawtiles(maze,radius):
# 	for center in maze:
# 		drawsquare(center,radius)

#examplemaze=[[WIDTH/2,HEIGHT/2],[WIDTH/2+20,HEIGHT/2],[WIDTH/2+40,HEIGHT/2],[WIDTH/2+40,HEIGHT/2-20],[WIDTH/2+60,HEIGHT/2-20], [WIDTH/2+80,HEIGHT/2-20],[WIDTH/2+80,HEIGHT/2]]

# example=arraygenerator(arraydimension,20)
# examplemaze=example[0]
# examplemoves=example[1]

over=0
start_time=pygame.time.get_ticks()
pause=False

level=5

while not game_over:
	clock.tick(60)
	screen.fill((0,0,0))
	arraydimension=2*level+2	
	thislevel=arraygenerator(arraydimension,level)		
	maze=thislevel[0]
	ex=extreme(maze)
	answerkey=thislevel[1]
	globalradius=(WIDTH-100)//(4*ex+2)
	memostageover=0
	start_ticks=pygame.time.get_ticks()
	while not memostageover:
		screen.blit(myFont.render('Length '+str(level), True, (255,255,255)), (0.01*WIDTH,0.01*HEIGHT))
		mazegenerator(maze,globalradius)
		drawsnake([WIDTH/2,HEIGHT/2],[],globalradius)		
		pygame.display.update()		
		seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
		if seconds>2: 
			memostageover=1  			  
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	playingover=0
	screen.fill((0,0,0))
	screen.blit(myFont.render('Length '+str(level), True, (255,255,255)), (0.01*WIDTH,0.01*HEIGHT))
	partialmaze=[[0 for i in range(arraydimension)] for j in range(arraydimension)]
	partialmaze[(arraydimension-1)/2][(arraydimension-1)/2]=1
	currentposition=[(arraydimension-1)/2,(arraydimension-1)/2]
	currentmoves=[]
	while not playingover:				
		lose=0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					currentmoves.append('U')
					if answerkey[0]=='U':						
						currentposition[1]=currentposition[1]+1
						answerkey.pop(0)						
						partialmaze[currentposition[0]][currentposition[1]]=1
					else:
						lose=1
				if event.key==pygame.K_DOWN:
					currentmoves.append('D')
					if answerkey[0]=='D':
						currentposition[1]=currentposition[1]-1
						answerkey.pop(0)						
						partialmaze[currentposition[0]][currentposition[1]]=1
					else:
						lose=1
				if event.key==pygame.K_LEFT:
					currentmoves.append('L')
					if answerkey[0]=='L':
						currentposition[0]=currentposition[0]-1
						answerkey.pop(0)						
						partialmaze[currentposition[0]][currentposition[1]]=1
					else:
						lose=1
				if event.key==pygame.K_RIGHT:
					currentmoves.append('R')
					if answerkey[0]=='R':
						currentposition[0]=currentposition[0]+1
						answerkey.pop(0)					
						partialmaze[currentposition[0]][currentposition[1]]=1
					else:
						lose=1	
		mazegenerator(partialmaze,globalradius)
		drawsnake([WIDTH/2,HEIGHT/2],currentmoves,globalradius)
		pygame.display.update()		
		if lose:
			answerkey=[]
			level=4			
			mazegenerator(maze,globalradius)
			drawsnake([WIDTH/2,HEIGHT/2],currentmoves,globalradius)
			restart=0
			screen.blit(myFont.render('Press any key to restart', True, (255,255,255)), (0.15*WIDTH,0.95*HEIGHT))
			pygame.display.update()	
			while not restart:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						restart=1
		if not answerkey:
			if not lose:
				nextlevel=0
				screen.blit(myFont.render('Press any key to continue', True, (255,255,255)), (0.15*WIDTH,0.95*HEIGHT))
				pygame.display.update()	
				while not nextlevel:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()
						if event.type == pygame.KEYDOWN:
							nextlevel=1
			playingover=1
			level=level+1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.update()
