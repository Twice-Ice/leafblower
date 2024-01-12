import pygame
from pygame.math import Vector2
import math
from pygame import Rect
pygame.init()

screen = pygame.display.set_mode((800,800))
screensize = pygame.display.get_window_size()

class Player:

	def __init__(self):
		self.pos = Rect(0,0,128,128)
		self.rel = Vector2(0,0)
		self.vel = tuple[0,0]

		self.image = pygame.image.load('resources/placeholder.png')
		self.offset = Vector2(self.image.get_rect().topleft) - Vector2(self.image.get_rect().midtop)

		self.newMousePos = Vector2(0,0)
		self.oldMousePos = Vector2(0,0)

		self.correctionangle = 90
	
	def mouseShisse(self):
		self.newMousePos = pygame.mouse.get_pos()
		self.oldMousePos = self.newMousePos

	def atan2(y, x):
		num = math.atan2(y, x) * (180/math.pi)
		if num > 0:
			return num
		else:
			return 180 + (180 - abs(num))

	def update(self):
		

		self.newMousePos = pygame.mouse.get_pos()

		self.rel = self.newMousePos-self.oldMousePos

		print(self.rel)
		
		self.pos=self.oldMousePos

		self.oldMousePos = self.newMousePos
		self.draw()

		
	def draw(self):

		angle = math.degrees(math.atan2(-self.rel.y,self.rel.x)) - self.correctionangle

		transformed_image = pygame.transform.rotate(self.image, angle)

		pygame.math.Vector2.rotate_ip(self.pos,angle)
		
		screen.blit(transformed_image, self.newMousePos)
		#pygame.draw.circle(screen, (255,255,240),self.pos,50)


guy = Player()
clock = pygame.time.Clock()
bye = False
guy.mouseShisse()

while bye == False:
	clock.tick(60)
	screen.fill((0,0,0))
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				bye = True

	guy.update()


	pygame.display.flip()

pygame.quit()