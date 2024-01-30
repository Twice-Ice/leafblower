import pygame
import random
import math
from globals import SCREEN_X, SCREEN_Y
from miscClasses import MoneyCounter
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
COLOR = 5

# guy = Player()
class LeafSpawner:
	STARTING_SPEED = 0.1
	def __init__(self, leaves):
		self.frameMoney = 0
		self.leafBlowers = []
		self.leaves = [] #this list contains information regarding every single leaf in the game.
		for i in range(leaves): #creates a 2d list containing each leaf.
			tempX = 0
			tempY = 10
			self.leaves.append([ random.randint(0,SCREEN_X) + tempX, random.randint(0,SCREEN_Y)+ tempY, 0, 0, self.STARTING_SPEED, (random.randint(155, 255), random.randint(0, 155), 0)]) #xpos, ypos, xvelo, yvelo, speed, color

	def draw(self, leafPos, screen):
		if leafPos == 1: #since the leaves are autumn colors now, this will just be white.
			pygame.draw.circle(screen, (255, 255, 255), (self.leaves[leafPos][X], self.leaves[leafPos][Y]), 6)
		else:
			pygame.draw.circle(screen, self.leaves[leafPos][COLOR], (self.leaves[leafPos][X], self.leaves[leafPos][Y]), 6)

	def update(self, screen):
		self.frameMoney = 0  #resets frame money every frame.
		# print(self.leaves[1])
		for leafPos in range(len(self.leaves)): #goes through each leaf in the leaves list.
			if self.leaves[leafPos][X] < SCREEN_X + 10 and self.leaves[leafPos][X] > -10 and self.leaves[leafPos][Y] < SCREEN_Y + 10 and self.leaves[leafPos][Y] > -10: # doesn't update the leaf if it's outside of the screen.
				self.applyPhysics(leafPos)
				self.draw(leafPos, screen) #only draws the leaf if it's on screen.
			elif self.leaves[leafPos][X] != -69 and self.leaves[leafPos][Y] != -420: #collects the leaf (assuming it's not already collected), because it's not on screen.
				self.collectLeaf(leafPos)

	def applyPhysics(self, leafPos):
		for j in range(len(self.leafBlowers)): #cycles through all leafblowers
			#calculates hypotenuse (distance) between the leafblower and the leaf
			leafDistance = math.sqrt((self.leafBlowers[j][0].x - self.leaves[leafPos][X]) ** 2 + abs(self.leafBlowers[j][0].y - self.leaves[leafPos][Y]) ** 2)

			if leafDistance <= self.leafBlowers[j][1]: #checks if the leaf is in the range of the current leafblower
				if leafDistance == 0: #if the leaf is too close, it is offset in order to avoid leaves getting stuck at the center of a leafblower.
					leafDistance = .01
					self.leaves[leafPos][X] += 0.01
				#Finds the angle between leaf & leafblower
				angle = math.atan2(float(self.leaves[leafPos][Y] - self.leafBlowers[j][0].y), float(self.leaves[leafPos][X] - self.leafBlowers[j][0].x))

				#Convert that angle to coordinates, extend to the correct size so that it picks a point along the leafblower's bounds
				endX = int((math.cos(angle) * self.leafBlowers[j][1]) + self.leafBlowers[j][0].x)
				endY = int((math.sin(angle) * self.leafBlowers[j][1]) + self.leafBlowers[j][0].y)

				#Linear algebra stuff, takes the distance between the current and end position, converts that to a ratio that can be used to make leaves move at a constant speed
				xDistance = endX - self.leaves[leafPos][X]
				yDistance = endY - self.leaves[leafPos][Y]
				magnitude = math.sqrt((xDistance)**2 + (yDistance)**2)
				if magnitude == 0:
					#Prevent divide by zero error
					magnitude = 0.01
				yDir = yDistance/magnitude
				xDir = xDistance/magnitude

				self.leaves[leafPos][SPEED] += self.leafBlowers[j][2] #default power = .2 (?)

				#sets the velocities
				self.leaves[leafPos][DELTA_X] = xDir * self.leaves[leafPos][SPEED]
				self.leaves[leafPos][DELTA_Y] = yDir * self.leaves[leafPos][SPEED]
		
		#applies drag
		self.drag(leafPos)

		#moves the leaf
		self.leaves[leafPos][X] += self.leaves[leafPos][DELTA_X]
		self.leaves[leafPos][Y] += self.leaves[leafPos][DELTA_Y]

		#screen wrapping stuff because funny inifinite pain with leaves go brrrrr
		#if self.leaves[leafPos][X] < 0:
		#	self.leaves[leafPos][X] += SCREEN_X
		#elif self.leaves[leafPos][X] > SCREEN_X:
		#	self.leaves[leafPos][X] -= SCREEN_X

		#if self.leaves[leafPos][Y] < 0:
		#	self.leaves[leafPos][Y] += SCREEN_Y
		#elif self.leaves[leafPos][Y] > SCREEN_Y:
		#	self.leaves[leafPos][Y] -= SCREEN_Y

	def drag(self, leafPos):
		#keep dragVal below minSpeed or else small shaking visual bug.
		dragVal = 0.25
		minSpeed = 0.4

		#if the leaf isn't still, and it's not below the minimum speed,
		#then it will be reduced by some fancy math that just determines whether or not DELTA_X/Y is pos/neg and applies the inverse.

		if self.leaves[leafPos][DELTA_X] != 0:
			if abs(self.leaves[leafPos][DELTA_X]) <= minSpeed:
				self.leaves[leafPos][DELTA_X] = 0
			else:
				self.leaves[leafPos][DELTA_X] += dragVal * ((self.leaves[leafPos][DELTA_X]/abs(self.leaves[leafPos][DELTA_X])) * -1)

		if self.leaves[leafPos][DELTA_Y] != 0:
			if abs(self.leaves[leafPos][DELTA_Y]) <= minSpeed:
				self.leaves[leafPos][DELTA_Y] = 0
			else:
				self.leaves[leafPos][DELTA_Y] += dragVal * ((self.leaves[leafPos][DELTA_Y]/abs(self.leaves[leafPos][DELTA_Y])) * -1)

	def collectLeaf(self, leafPos):
		#the leaf goes to an arbitrary position that would otherwise be impossible to reach for the leaf.
		#This is used in self.respawnLeaves() as a way of checking if the leaf was collected previously or not without using another variable in the leaf's list.
		self.leaves[leafPos][X] = -69
		self.leaves[leafPos][Y] = -420
		self.frameMoney += 1

	def respawnLeaves(self):
		for i in range(len(self.leaves)): #checks all the leaves
			if (self.leaves[i][X] == -69 and self.leaves[i][Y] == -420) or i % 4 == 0: #if the leaf is collected or every 4th leaf, it is moved to a random pos and it's velo is reset.
				#it's every 4th leaf in order to avoid clumping, or all the leaves being out of reach of the player. this allows for afk time.
				self.leaves[i][X] = random.randint(0, SCREEN_X)
				self.leaves[i][Y] = random.randint(0, SCREEN_Y)
				self.leaves[i][DELTA_X] = 0
				self.leaves[i][DELTA_Y] = 0
				self.leaves[i][SPEED] = 0