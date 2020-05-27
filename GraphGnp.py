import pygame
import random
import sys
import time

pygame.init()
WIDTH=900
HEIGHT=900
screen= pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
vertex_size=5
vertex_color=(50,0,50)
edge_thickness=2
edge_color=(0,0,0)

clock = pygame.time.Clock()


class Graph: 
    def __init__(self, vertices):
    	self.vertices=vertices 
        self.graph = [[] for j in range(vertices)]
    def add_edge(self, src, dest): 
    	self.graph[src].append(dest)
    	self.graph[dest].append(src)
    def print_graph(self):
    	print(self.graph)

def random_graph(vertices,p):
	g=Graph(vertices)
	for i in range(vertices-1):
		for j in range(i+1,vertices):
			x=random.uniform(0,1)
			if x<=p:
				g.add_edge(i,j)
	return g

def draw_graph(g,topleft,width,height):
	vertices=g.vertices
	location=[[topleft[0]+random.randint(0,width),topleft[1]+random.randint(0,height)] for i in range(vertices)]
	for i in range(vertices):
		pygame.draw.circle(screen, vertex_color, location[i], vertex_size)
	for i in range(vertices):
		for j in g.graph[i]:
			pygame.draw.line(screen,edge_color,location[i], location[j], edge_thickness)

def draw_box(copy,n,p):
	for i in range(copy):
		for j in range(copy): 
			g=random_graph(n,p)
			draw_graph(g,(i*WIDTH//copy,j*WIDTH//copy),WIDTH//copy,HEIGHT//copy)

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill((255,255,255))
	draw_box(7,20,0.2)
	pygame.display.update()
	clock.tick(10)

