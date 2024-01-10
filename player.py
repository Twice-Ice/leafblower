import pygame
from pygame.math import Vector2
import math
pygame.init()

screen = pygame.display.set_mode((800,800))
screensize = pygame.display.get_window_size()

class Player:

	def __init__(self):
		self.pos = Vector2(pygame.mouse.get_pos())
		self.rel = Vector2(0,0)
		self.vel = Vector2(0,0)

		self.image = pygame.image.load('resources/placeholder.png')
		self.offset = Vector2(self.image.get_rect().topleft) - Vector2(self.image.get_rect().midtop)
	
	def update(self):
		
		self.vel = pygame.mouse.get_rel()
		self.rel = pygame.mouse.get_pos() - self.pos

		self.pos += self.vel
		
	def rotate(self):
		#angle = (180 / math.pi) * -math.atan2(self.rel.y,self.rel.x)
		radius, angle = self.rel.as_polar()
		self.image = pygame.transform.rotate(self.image, -angle)
		#self.pos+=self.offset

		
	
	def draw(self):
		screen.blit(self.image, self.pos)

guy = Player()
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	screen.fill((0,0,0))

	guy.update()
	guy.rotate()
	guy.draw()


	pygame.display.flip()