import pygame
import random
import math
from pygame import Rect
from buttons import Button
from drone import Drone
from pygame.math import Vector2
from globals import screen_X, screen_Y, FPS, FULLSCREEN_X, FULLSCREEN_Y
from leaf import LeafSpawner, Blower
from player import Player
from menu import Menu
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
leeevs = LeafSpawner(700,scale)

leafTicker = Ticker(float(5)) #x seconds between ticks
money = MoneyCounter()
moneyDisplay = TextDisplay(money.val, 10, 10)

def tempFunc():
	print("AHHHH PLEASE NO GOD NO!!!")
testButton = Button(10, 10, 10, 10, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), tempFunc)

#adds the player to the leafBlowers (entities) list.
leeevs.leafBlowers.append(Blower(guy.centerpos, guy.size, guy.power)) #Vector2(xpos, ypos), size
#creates the drone list and drones in the list and then appends those all to the blower list.
droneList = []
for drone in range(10):
	droneList.append(Drone(random.randint(0, screen_X), random.randint(0, screen_Y), scale))
	leeevs.leafBlowers.append(Blower(droneList[drone].pos, droneList[drone].size, droneList[drone].power))

#a list that can hold all menus in the game.
menuList = []
menuButtonsList = []
menuRect = Rect(10, 10, screen_X-20, screen_Y-20)
testMenu = Menu(menuRect, (155, 155, 155), [
	Button(50, 50, 50, 50, (255, 255, 255), tempFunc)
])
testMenuButton = Button(screen_Y-50, 15, 50, 50, (255, 255, 255), testMenu.activate)
menuList.append(testMenu)
menuButtonsList.append(testMenuButton)

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
	for drone in range(len(droneList)):
		droneList[drone].update(screen)
	leeevs.update(delta, screen)
	money.val += leeevs.frameMoney
	moneyDisplay.update(screen, money.val)
	testButton.update(screen, Vector2(pygame.mouse.get_pos()))
	for menu in range(len(menuList)): #should always be drawing menus last so that they are on top of everything.
		menuButtonsList[menu].update(screen, Vector2(pygame.mouse.get_pos()))
		menuList[menu].update(screen, Vector2(pygame.mouse.get_pos()))

	pygame.display.flip() #update graphics each game loop

	#screen = pygame.display.set_mode((X, Y))
	#X+=0.5
	#Y+=0.5

pygame.quit()