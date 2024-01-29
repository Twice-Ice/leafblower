import pygame
import random
import math
from const import SCREEN_X, SCREEN_Y
from pygame import mixer
from player import Player
from pygame.math import Vector2
pygame.init

#constants because why not.
X = 0
Y = 1
DELTA_X = 2
DELTA_Y = 3
SPEED = 4

def tpd(num):
	return math.floor(num*100)/100

#temporary player class containing positions because player class doesn't work right now.
class temp:
	def __init__(self, xpos, ypos):
		self.xpos = xpos
		self.ypos = ypos

# guy = Player()
class LeafSpawner:
	STARTING_SPEED = 0.1
	def __init__(self, leaves):
		self.leafBlowers = []
		self.leaves = [] #this list contains information regarding every single leaf in the game.
		for i in range(leaves): #creates a 2d list containing each leaf.
			tempX = 0
			tempY = 10
			self.leaves.append([ random.randint(0,SCREEN_X) + tempX, random.randint(0,SCREEN_Y)+ tempY, 0, 0, self.STARTING_SPEED]) #random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y), 0, 0]) #xpos, ypos, xvelo, yvelo

	def draw(self, i, screen):
		if i == 1:
			pygame.draw.circle(screen, (255, 0, 0), (self.leaves[i][X], self.leaves[i][Y]), 6)
		else:
			pygame.draw.circle(screen, (0, 255, 0), (self.leaves[i][X], self.leaves[i][Y]), 6)

	def update(self, screen):
		print(self.leaves[1])
		for i in range(len(self.leaves)): #goes through each leaf in the leaves list.
			if self.leaves[i][X] < SCREEN_X + 10 and self.leaves[i][X] > -10 and self.leaves[i][Y] < SCREEN_Y + 10 and self.leaves[i][Y] > -10: # doesn't update the leaf if it's outside of the screen.
				self.applyPhysics(i)
				self.draw(i, screen)

	def applyPhysics(self, i):
		for j in range(len(self.leafBlowers)):
			leafDistance = math.sqrt((self.leafBlowers[j][0].x - self.leaves[i][X]) ** 2 + abs(self.leafBlowers[j][0].y - self.leaves[i][Y]) ** 2)
			# leafDistance = math.sqrt((guy.centerpos.x - self.leaves[i][X]) ** 2 + abs(guy.centerpos.y - self.leaves[i][Y]) ** 2)
			
			if leafDistance == 0:
				leafDistance = .01
				self.leaves[i][X] += 0.01
			if leafDistance <= self.leafBlowers[j][1]: #checks if the leaf is in the range of the current leafblower

				#Finds the angle between leaf & leafblower
				angle = math.atan2(float(self.leaves[i][Y] - self.leafBlowers[j][0].y), float(self.leaves[i][X] - self.leafBlowers[j][0].x))
				# angle = math.atan2(float(self.leaves[i][Y] - guy.centerpos.y), float(self.leaves[i][X] - guy.centerpos.x))


				#Convert that angle to coordinates, extend to the correct size so that it picks a point along the leafblower's bounds
				endX = int((math.cos(angle) * self.leafBlowers[j][1]) + self.leafBlowers[j][0].x)
				endY = int((math.sin(angle) * self.leafBlowers[j][1]) + self.leafBlowers[j][0].y)
				# endX = int((math.cos(angle) * size) + guy.centerpos.x)
				# endY = int((math.sin(angle) * size) + guy.centerpos.y)

				#Linear algebra stuff, takes the distance between the current and end position, converts that to a ratio that can be used to make leaves move at a constant speed
				xDistance = endX - self.leaves[i][X]
				yDistance = endY - self.leaves[i][Y]
				magnitude = math.sqrt((xDistance)**2 + (yDistance)**2)
				if magnitude == 0:
					#Prevent divide by zero error
					magnitude = 0.01
				yDir = yDistance/magnitude
				xDir = xDistance/magnitude

				self.leaves[i][SPEED] += 0.5

				#sets the velocities
				self.leaves[i][DELTA_X] = xDir * self.leaves[i][SPEED]
				self.leaves[i][DELTA_Y] = yDir * self.leaves[i][SPEED]
			   # pygame.draw.line(screen, (255, 0, 0), (self.leafBlowers[j].xpos, self.leafBlowers[j].ypos), (self.))
			#else:
				#resets speed
				#self.leaves[i][SPEED] = self.STARTING_SPEED
				
				#applies drag
		self.drag(i)

		#moves the leaf
		self.leaves[i][X] += self.leaves[i][DELTA_X]
		self.leaves[i][Y] += self.leaves[i][DELTA_Y]

		#if self.leaves[i][X] < 0:
		#	self.leaves[i][X] += SCREEN_X
		#elif self.leaves[i][X] > SCREEN_X:
		#	self.leaves[i][X] -= SCREEN_X

		#if self.leaves[i][Y] < 0:
		#	self.leaves[i][Y] += SCREEN_Y
		#elif self.leaves[i][Y] > SCREEN_Y:
		#	self.leaves[i][Y] -= SCREEN_Y

	def drag(self, i):
		dragVal = 0.3
		minSpeed = 0.1

		if abs(self.leaves[i][DELTA_X]) <= minSpeed:
			self.leaves[i][DELTA_X] = 0
		else:
			self.leaves[i][DELTA_X] += dragVal * ((self.leaves[i][DELTA_X]/abs(self.leaves[i][DELTA_X])) * -1)

		if abs(self.leaves[i][DELTA_Y]) <= minSpeed:
			self.leaves[i][DELTA_Y] = 0
		else:
			self.leaves[i][DELTA_Y] += dragVal * ((self.leaves[i][DELTA_Y]/abs(self.leaves[i][DELTA_Y])) * -1)