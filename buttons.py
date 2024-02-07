import pygame
from pygame.math import Vector2
from pygame import Rect
pygame.init

class Button:
	def __init__(self, xpos, ypos, width, height, img, clickFunc):
		self.clickFunc = clickFunc
		self.img = img
		self.rect = Rect(xpos, ypos, width, height)

	def update(self, screen, mouse):
		self.draw(screen)
		self.collisions(mouse)

	def draw(self, screen):
		scale = self.rect.height/self.img.get_rect().height
		newImage = pygame.transform.smoothscale_by(self.img,scale)
		screen.blit(newImage, (self.rect[0], self.rect[1]))

	def collisions(self, mouse):
		if self.rect.collidepoint(mouse): #if your mouse is colliding with the button only.
			for event in pygame.event.get(): #loops through the frame's events.
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #if the left mouse button was pressed (event.button 1 is lmb).
					self.clickFunc() #calls the function for when the button is clicked.