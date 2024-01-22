import pygame
import random
import math
#ehh I'll import player later. I think I'm just gonna play this easy.
pygame.init()

screenX = 800
screenY = 800

#creates game screen and caption
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("leaves")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed
ticker = 0

#Constants because Tess is gonna give me an aneurysm
X = 0
Y = 1
deltaX = 2
deltaY = 3

leafBlowers = []

def updateTicker():
	global ticker
	if ticker < 60:
		ticker += 1
	else:
		ticker = 0

#a better function for telling the angle between two points. 
#input (y1 - y2, x1 - x2) in order to get two points working.
def atan2(y, x):
	def adjustAngle(angle):
		if angle + 90 > 360:
			return angle - 270 # + 90 - 360
		else:
			return angle + 90
	num = math.atan2(y, x) * (180/math.pi)
	if num > 0:
		print("atan2 = ", adjustAngle(num), end= ", ")
		return adjustAngle(num)
	else:
		print("atan2 = ", adjustAngle(180 + (180 - abs(num))), end= ", ")
		return adjustAngle(180 + (180 - abs(num)))

def tpd(num):
	return math.floor(num*100)/100

#temporary player class containing positions because player class doesn't work right now.
class temp:
	def __init__(self, xpos, ypos):
		self.xpos = xpos
		self.ypos = ypos

#adds the temp class to the leafBlowers (entities) list.
leafBlowers.append(temp(screenX/2, screenY/2))

class leafSpawner:
	def __init__(self, leaves):
		self.leaves = [] #this list contains information regarding every single leaf in the game.
		for a in range(leaves): #creates a 2d list containing each leaf.
			tempX = 0
			tempY = 10
			self.leaves.append([random.randint(0,screenX), random.randint(0,screenY), 0, 0]) #random.randint(0, screenX), random.randint(0, screenY), 0, 0]) #xpos, ypos, xvelo, yvelo
		self.leafspawns = self.leaves.copy()

	def draw(self, i):
		pygame.draw.circle(screen, (0, 255, 0), (self.leaves[i][X], self.leaves[i][Y]), 5)

	def update(self):
		for i in range(len(self.leaves)): #goes through each leaf in the leaves list.
			self.applyPhysics(i)
			self.draw(i)
			for j in range(len(self.leaves[0])):
				print(math.floor(self.leaves[0][j] * 100)/100, end = ", ")
			print()

	def applyPhysics(self, i):
		size = 800
		for k in range(len(leafBlowers)):
			leafDistance = abs(math.sqrt((leafBlowers[k].xpos - self.leaves[i][X]) ** 2 + abs(leafBlowers[k].ypos - self.leaves[i][Y]) ** 2))
			if leafDistance == 0:
				leafDistance = .01
			if  leafDistance <= size: #checks if the leaf is in the range of the current leafblower
				angle = atan2(leafBlowers[k].xpos - self.leaves[i][X], leafBlowers[k].ypos - self.leaves[i][Y]) #gets the angle between the the leaf and the leafblower
				#angle = 270
				print(tpd(angle), end = ", ")

				endX = math.cos(angle*(math.pi/180)) * size
				endY = math.sin(angle*(math.pi/180)) * size



				#sets the velocities
				#self.leaves[i][deltaX] += math.cos(angle)#.5 #* (size/leafDistance) #x
				#self.leaves[i][deltaY] += math.sin(angle)#.5 #* (size/leafDistance) #y
		#moves the leaf
		self.leaves[i][X] += self.leaves[i][deltaX] 
		self.leaves[i][Y] += self.leaves[i][deltaY]
		#applies drag
		self.drag(i)

	def drag(self, i):
		dragVal = .4

		if abs(self.leaves[i][deltaX]) <= dragVal:
			self.leaves[i][deltaX] = 0
		elif self.leaves[i][deltaX] > 0:
			self.leaves[i][deltaX] -= dragVal
		elif self.leaves[i][deltaX] < 0:
			self.leaves[i][deltaX] += dragVal
			
		
		if abs(self.leaves[i][deltaY]) <= dragVal:
			self.leaves[i][deltaY] = 0
		elif self.leaves[i][deltaY] > 0:
			self.leaves[i][deltaY] -= dragVal
		elif self.leaves[i][deltaY] < 0:
			self.leaves[i][deltaY] += dragVal


	

leeevs = leafSpawner(1000)

#BEGIN GAME LOOP######################################################
while not doExit:
	
	clock.tick(60) #FPS (frames per second)
	updateTicker()
	screen.fill((0,0,0))

	pygame.draw.circle(screen, (255, 255, 255), (screenX/2, screenY/2), 1)

	#pygame's way of listening for events (key presses, mouse clicks, etc)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit program

	leeevs.update()



	pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()




#jaime hp:
#25
#tess hp:
#25