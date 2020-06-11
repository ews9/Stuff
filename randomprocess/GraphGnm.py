import pygame
import random
import sys
import time

pygame.init()
WIDTH=900
HEIGHT=900
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
vertex_size=8
vertex_color=(0,0,255)
edge_thickness=5
edge_color=(0,0,0)

clock = pygame.time.Clock()
vertices=20



def good_random():
	while True:
		x=[random.randint(0,WIDTH),random.randint(0,HEIGHT)]
		if (WIDTH/2-x[0])*(WIDTH/2-x[0])+(HEIGHT/2-x[1])*(HEIGHT/2-x[1])>= 450*450:
			return x


location=[good_random() for i in range(vertices)]



class Graph: 
    def __init__(self, vertices):
    	self.vertices=vertices 
        self.graph = [[] for j in range(vertices)]
    def add_edge(self, src, dest): 
    	self.graph[src].append(dest)
    	self.graph[dest].append(src)
    def print_graph(self):
    	print(self.graph)

def add_random_edge(g):
	vertices=g.vertices
	notfull=1
	for i in range(vertices):
		if len(g.graph[i])<vertices-1:
			notfull=0
	if notfull==1:
		return Graph(vertices)
	while True:
		i=random.randint(0,vertices-1)
		j=random.randint(0,vertices-1)
		if j not in g.graph[i]:
			g.add_edge(i,j)
			return g

def draw_graph(g,location):
	for i in range(vertices):
		for j in g.graph[i]:
			pygame.draw.line(screen,edge_color,location[i], location[j], edge_thickness)
	for i in range(vertices):
		pygame.draw.circle(screen, vertex_color, location[i], vertex_size)

g=Graph(vertices)

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill((255,255,255))
	draw_graph(g,location)
	g=add_random_edge(g)
	pygame.display.update()
	clock.tick(10)

