import pygame
import random
import math
from const import SCREEN_X, SCREEN_Y
from leaf import LeafSpawner
from player import Player
#ehh I'll import player later. I think I'm just gonna play this easy.
pygame.init

#creates game screen and caption
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("leaves")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed
ticker = 0

def updateTicker():
	global ticker
	if ticker < 60:
		ticker += 1
	else:
		ticker = 0
		
guy = Player()
leeevs = LeafSpawner(7000)

#temporary player class containing positions because player class doesn't work right now.
class temp:
	def __init__(self, xpos, ypos, size):
		self.xpos = xpos
		self.ypos = ypos
		self.size = size

#adds the temp class to the leafBlowers (entities) list.
leeevs.leafBlowers.append(temp(SCREEN_X/2, SCREEN_Y/2, 200)) #xpos, ypos, size

		
#BEGIN GAME LOOP######################################################
while not doExit:
	
	delta = clock.tick(60) / 1000 #FPS (frames per second)
	updateTicker()
	screen.fill((0,0,0))

	pygame.draw.circle(screen, (255, 255, 255), (SCREEN_X/2, SCREEN_Y/2), 1)

	#pygame's way of listening for events (key presses, mouse clicks, etc)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit program

	leeevs.update()
	guy.update(delta)

	screen.blit(guy.transformed_image, (guy.newMousePos.x-72,guy.newMousePos.y-72))


	pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()