from globals import FPS, screen_X, screen_Y
import pygame
#this file contains all small classes with less significant line size.

#ticker class, it's a looping timer of sorts.
class Ticker:
	#time is represented in seconds
	def __init__(self, time):
		self.maxTicks = time * FPS
		self.ticks = 0
	
	#update self.ticks, and returns true when self.ticks is reset.
	def update(self):
		if self.ticks < self.maxTicks:
			self.ticks += 1
			return False
		else:
			self.ticks = 0
			return True
		
class MoneyCounter:
	def __init__(self):
		self.val = 0 #value

	def add(self, addValue):
		self.val += addValue

class TextDisplay:
	def __init__(self, text, x, y):
		if text == None: text = ""
		self.text = text
		self.x = x
		self.y = y

	def update(self, screen, text):
		font = pygame.font.Font(None, 74)
		text = font.render(str(text), 1, (255, 255, 255))
		screen.blit(text, (self.x, self.y))
			
#temporary player class containing positions because player class doesn't work right now.
class Temp:
	def __init__(self, xpos, ypos, size):
		self.xpos = xpos
		self.ypos = ypos
		self.size = size