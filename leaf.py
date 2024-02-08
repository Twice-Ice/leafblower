#type: strict
import pygame
import random
import math
from globals import screen_X, screen_Y
from pygame.math import Vector2
from pygame.color import Color

LEAF_DRAG = 2
LEAF_WEIGHT = 0.02
BLOWER_FALLOFF = 0.5 # 1 is linear

class Blower:
	pos: Vector2
	size: float
	power: float

	def __init__(self, pos: Vector2, size: float, power: float):
		self.pos = pos
		self.size = size
		self.power = power
 
class Leaf:
	pos: Vector2
	vel: Vector2
	color: Color
	size: float

	def __init__(self, pos: Vector2, color: Color, size: float):
		self.pos = pos
		self.vel = Vector2(0, 0)
		self.color = color
		self.size = size

	def draw(self, screen: pygame.Surface):
		pygame.draw.circle(screen, self.color, self.pos, self.size)

	def update(self, delta: float):
		self.pos += self.vel * delta

	def applyForce(self, force: Vector2, delta: float):
		'''Applies `force` to the leaf. The force is measured in pixels/sec^2. This meant is for forces applied on every frame!'''
		self.vel += force / LEAF_WEIGHT * delta

class LeafSpawner:
	STARTING_SPEED = 0.1
	def __init__(self, leaves: int, scale: float):
		self.frameMoney = 0
		self.leafBlowers: list[Blower] = []
		self.leaves: list[Leaf] = [] #this list contains every single leaf in the game.
		self.scale = scale
		for _ in range(leaves): #creates a list containing each leaf.
			self.leaves.append(
				Leaf(
					Vector2(
						random.randint(50, screen_X-50), 
						random.randint(50, screen_Y-50)
					), 
					Color(
						random.randint(155, 255), 
						random.randint(0, 155), 
						0
					),
					8 * self.scale
				)
			)

	def update(self, delta: float, screen: pygame.Surface):
		#delta is calculated using the framerate. Applying delta to (for example) movement, means the leaves will stay the same speed even if fps drops, rather than slowing down
		self.frameMoney = 0  #resets frame money every frame.
		# print(self.leaves[1])
		for leaf in self.leaves: #goes through each leaf in the leaves list.
			if leaf.pos.x < screen_X + 10 and leaf.pos.x > -10 and leaf.pos.y < screen_Y + 10 and leaf.pos.y > -10: # doesn't update the leaf if it's outside of the screen.
				self.applyPhysics(leaf, delta)
				leaf.draw(screen)
			elif leaf.pos.x != -69 and leaf.pos.y != -420: #collects the leaf (assuming it's not already collected), because it's not on screen.
				self.collectLeaf(leaf)

	def applyPhysics(self, leaf: Leaf, delta: float):
		for blower in self.leafBlowers: #cycles through all leafblowers
			#calculates hypotenuse (distance) between the leafblower and the leaf
			leafDistance = (blower.pos - leaf.pos).length()

			if leafDistance <= blower.size: #checks if the leaf is in the range of the current leafblower
				# if leafDistance == 0: #if the leaf is too close, it is offset in order to avoid leaves getting stuck at the center of a leafblower.
				# 	leafDistance = .01
				# #Finds the angle between leaf & leafblower
				# angle = math.atan2(float(leaf.pos.y - blower.pos.y), float(leaf.pos.x - blower.pos.x))

				# #Convert that angle to coordinates, extend to the correct size so that it picks a point along the leafblower's bounds
				# endX = int((math.cos(angle) * blower.size) + blower.pos.x)
				# endY = int((math.sin(angle) * blower.size) + blower.pos.y)

				# #Linear algebra stuff, takes the distance between the current and end position, converts that to a ratio that can be used to make leaves move at a constant speed
				# xDistance = endX - leaf.pos.x
				# yDistance = endY - leaf.pos.y
				# magnitude = math.sqrt((xDistance)**2 + (yDistance)**2)
				# if magnitude == 0:
				# 	#Prevent divide by zero error
				# 	magnitude = 0.01
				# yDir = yDistance/magnitude
				# xDir = xDistance/magnitude

				blowDirection = ((leaf.pos - blower.pos).normalize() if leaf.pos != blower.pos else Vector2(0, 0))
				normalizedDist = leafDistance / blower.size

				blowSpeed = 1 - normalizedDist**BLOWER_FALLOFF
				blowForce = blowDirection * blowSpeed * blower.power


				leaf.applyForce(blowForce, delta) #default power = .2 (?)

				#sets the velocities
				# leaf.vel = (xDir * leaf[SPEED])*self.scale
		
		#applies drag
		self.drag(leaf, delta)

		#moves the leaf
		leaf.pos += leaf.vel * delta

		#screen wrapping stuff because funny inifinite pain with leaves go brrrrr
		#if leaf[X] < 0:
		#	leaf[X] += screen_X
		#elif leaf[X] > screen_X:
		#	leaf[X] -= screen_X

		#if leaf[Y] < 0:
		#	leaf[Y] += screen_Y
		#elif leaf[Y] > screen_Y:
		#	leaf[Y] -= screen_Y

	def drag(self, leaf: Leaf, delta: float):
		leaf.vel *= 1 - (LEAF_DRAG * delta)

	def collectLeaf(self, leaf: Leaf):
		#the leaf goes to an arbitrary position that would otherwise be impossible to reach for the leaf.
		#This is used in self.respawnLeaves() as a way of checking if the leaf was collected previously or not without using another variable in the leaf's list.
		leaf.pos = Vector2(-69, -420)
		self.frameMoney += 1

	def respawnLeaves(self):
		adjustor = random.randint(1, 4)
		for leaf in self.leaves: #checks all the leaves
			if (leaf.pos.x == -69 and leaf.pos.y == -420): #or (i + adjustor) % 4 == 0: #if the leaf is collected or every 4th leaf, it is moved to a random pos and it's velo is reset.
				#it's every 4th leaf in order to avoid clumping, or all the leaves being out of reach of the player. this allows for afk time.
				leaf.pos.x = random.randint(50, screen_X-50)
				leaf.pos.y = random.randint(50, screen_Y-50)
				leaf.vel = Vector2(0, 0)