import pygame
from pygame.math import Vector2
import math
from globals import SCREEN_X, SCREEN_Y
from pygame import Rect
pygame.init()

#screensize = pygame.display.get_window_size()

class Player:

	def __init__(self,scale):

		self.baseImage = pygame.image.load('resources/guyNice.png')
		self.defaultSizeImage = pygame.transform.smoothscale_by(self.baseImage, 128/self.baseImage.get_rect().height)
		self.image = pygame.transform.smoothscale_by(self.defaultSizeImage,scale)
		self.transformed_image = pygame.transform.rotate(self.image, 0)

		self.size = self.image.get_rect().height+20
		self.power = 1#.36

		#self.pos = Vector2(0,0)
		self.vel = Vector2(0,0)
		self.centerpos = Vector2(0,0)

		
		#self.offset = Vector2(self.image.get_rect().topleft) - Vector2(self.image.get_rect().midtop)

		self.newMousePos = Vector2(0,0)
		self.oldMousePos = Vector2(0,0)

		self.correctionangle = 90

		self.mouseVels: list[Vector2] = []

	def atan2(self, y, x):
		num = math.atan2(y, x) * (180/math.pi)
		if num > 0:
			return num
		else:
			return 180 + (180 - abs(num))
		
	def mouseMove(self,delta):
		self.newMousePos = Vector2(pygame.mouse.get_pos())

		rel = (self.newMousePos - self.oldMousePos) / delta

		if len(self.mouseVels) < 8:
			self.mouseVels.append(rel)
		else:
			self.mouseVels.pop(0)
			self.mouseVels.append(rel)
		
		avgVel = Vector2(0, 0)

		for vel in self.mouseVels:
			avgVel += vel
		avgVel /= len(self.mouseVels)
		
		self.oldMousePos = self.newMousePos
		return avgVel

	def move(self, delta: float):
		self.vel = self.mouseMove(delta)
		
		#self.pos += self.vel * delta 
		#self.pos = self.newMousePos
		self.centerpos.x = self.newMousePos.x
		self.centerpos.y = self.newMousePos.y

	def update(self,delta: float, screen):
		
		self.move(delta)
		self.rotate()
		self.draw(screen)

	def rotate(self):
		var = 6
		angle = math.degrees(math.atan2(-self.vel.y, self.vel.x)) - self.correctionangle
		
		if abs(self.vel.x) > 0 and abs(self.vel.y) > 0:
			#STUPID ANGLE STUFFF!!!!!!!! -90 = 270 so ive gotta do some scuffed code

			#smoothes out cardinal direction movement
			if angle <= 90+var and angle >= 90-var:
				self.transformed_image = pygame.transform.rotate(self.image, 90)
			elif angle <= 270+var and angle >= 270-var:
				self.transformed_image = pygame.transform.rotate(self.image, 270)
			elif angle <= 180+var and angle >= 180-var:
				self.transformed_image = pygame.transform.rotate(self.image, 180)
			#negative angles
			elif angle >= -90-var and angle <= -90+var:
				self.transformed_image = pygame.transform.rotate(self.image, -90)
			elif angle >= -270-var and angle <= -270+var:
				self.transformed_image = pygame.transform.rotate(self.image, -270)
			elif angle >= -180-var and angle <= -180+var:
				self.transformed_image = pygame.transform.rotate(self.image, -180)

			#near zero
			elif abs(angle) > 0 and abs(angle) <= var:
				self.transformed_image = pygame.transform.rotate(self.image, 0)
			elif abs(angle) <= 360+var and abs(angle) >= 360-var:
				self.transformed_image = pygame.transform.rotate(self.image, 0)

			else:
				self.transformed_image = pygame.transform.rotate(self.image, angle)
		else:
			self.transformed_image = pygame.transform.rotate(self.image, 0)
		


	def draw(self,screen):
		screen.blit(self.transformed_image, (self.newMousePos.x - self.image.get_rect().height // 2, self.newMousePos.y - self.image.get_rect().height // 2))
