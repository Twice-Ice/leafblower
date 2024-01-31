import pygame
import random
import math
from buttons import Button
from pygame.math import Vector2
from globals import SCREEN_X, SCREEN_Y, FPS
from leaf import LeafSpawner
from player import Player
from miscClasses import Temp, Ticker, MoneyCounter, TextDisplay
pygame.init

#creates game screen and caption
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.FULLSCREEN)
pygame.display.set_caption("leaves")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed

guy = Player()
leeevs = LeafSpawner(3000)
leafTicker = Ticker(float(5)) #x seconds between ticks
money = MoneyCounter()
moneyDisplay = TextDisplay(money.val, 10, 10)
def tempFunc():
	print("AHHHH PLEASE NO GOD NO!!!")
testButton = Button(10, 10, 10, 10, tempFunc)

#adds the player to the leafBlowers (entities) list.
leeevs.leafBlowers.append([guy.centerpos, guy.size, guy.power]) #Vector2(xpos, ypos), size
# for i in range(20):
# 	leeevs.leafBlowers.append([Vector2(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y)), 100])

center = pygame.display.get_window_size()
pygame.mouse.set_pos(center[0]//2,center[1]//2)		

#game loop
while not doExit:
	delta = clock.tick(FPS) / 1000 #FPS (frames per second)
	screen.fill((0,0,0))

	if leafTicker.update(): #updates the leaf ticker, the update function returns T/F if the ticker has activated or not.
		leeevs.respawnLeaves() #if True, all leaves "respawn". See more in the function def.

	#pygame's way of listening for events (key presses, mouse clicks, etc)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit program

	#update functions
	guy.update(delta,screen)
	leeevs.update(screen)
	money.val += leeevs.frameMoney
	moneyDisplay.update(screen, money.val)
	testButton.update(screen, Vector2(pygame.mouse.get_pos()))

	pygame.display.flip() #update graphics each game loop
pygame.quit()