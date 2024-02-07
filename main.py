import pygame
import random
import math
from buttons import Button
from drone import Drone
from pygame.math import Vector2
from globals import screen_X, screen_Y, FPS, FULLSCREEN_X, FULLSCREEN_Y
from leaf import LeafSpawner, Blower
from player import Player
from miscClasses import Temp, Ticker, MoneyCounter, TextDisplay
pygame.init()

#creates game screen and caption
X = 1
Y = 1
screen = pygame.display.set_mode((screen_X, screen_Y),  pygame.FULLSCREEN, pygame.SCALED, vsync=1)
pygame.display.set_caption("leaves")

#calculate scale
scale = (screen_Y/720)

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed

guy = Player(scale)
drone1 = Drone(screen_X/2, screen_Y/2,scale)
leeevs = LeafSpawner(700,scale)

leafTicker = Ticker(float(5)) #x seconds between ticks
money = MoneyCounter()
moneyDisplay = TextDisplay(money.val, 10, 10)
def tempFunc():
	print("AHHHH PLEASE NO GOD NO!!!")
testButton = Button(10, 10, 10, 10, pygame.image.load('resources/guyNice.png'), tempFunc)

#adds the player to the leafBlowers (entities) list.
leeevs.leafBlowers.append(Blower(guy.centerpos, guy.size, guy.power)) #Vector2(xpos, ypos), size

#for drone in range(10):
leeevs.leafBlowers.append(Blower(drone1.pos, drone1.size, drone1.power))
# for i in range(20):
# 	leeevs.leafBlowers.append([Vector2(random.randint(0, screen_X), random.randint(0, screen_Y)), 100])

center = pygame.display.get_window_size()
pygame.mouse.set_pos(center[0]//2,center[1]//2)
#pygame.mouse.set_visible(False)

#game loop
while not doExit:
	delta = clock.tick(FPS) / 1000 #FPS (frames per second)
	screen.fill((0,0,0))
	#for i in range(700):
	#	print(delta)
	if leafTicker.update(): #updates the leaf ticker, the update function returns T/F if the ticker has activated or not.
		leeevs.respawnLeaves() #if True, all leaves "respawn". See more in the function def.

	#pygame's way of listening for events (key presses, mouse clicks, etc)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit program

	#update functions
	guy.update(delta,screen)
	drone1.update(screen)
	leeevs.update(delta, screen)
	money.val += leeevs.frameMoney
	moneyDisplay.update(screen, money.val)
	testButton.update(screen, Vector2(pygame.mouse.get_pos()))

	pygame.display.flip() #update graphics each game loop

	#screen = pygame.display.set_mode((X, Y))
	#X+=0.5
	#Y+=0.5

pygame.quit()