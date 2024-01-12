import pygame
import random
import math
#ehh I'll import player later. I think I'm just gonna play this easy.
pygame.init

screenX = 800
screenY = 800

#creates game screen and caption
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("leaves")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed
ticker = 0

leafBlowers = []

def updateTicker():
    global ticker
    if ticker < 60:
        ticker += 1
    else:
        ticker = 0

def atan2(y, x):
    num = math.atan2(y, x) * (180/math.pi)
    if num > 0:
        return num
    else:
        return 180 + (180 - abs(num))
    
class temp:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

leafBlowers.append(temp(screenX/2, screenY/2))

class leafSpawner:
    def __init__(self, leaves):
        self.xpos = screenX/2 #position for the leaf spawner to be. This doesn't really affect anything but I thought it might be nice to have.
        self.ypos = screenY/2
        self.leaves = []
        for i in range(leaves): #creates a 2d list containing each leaf.
            YY = random.randint(0, screenY)
            self.leaves.append([random.randint(0, screenX), YY, 0, 0]) #xpos, ypos, xvelo, yvelo

    def draw(self, i):
            pygame.draw.circle(screen, (0, 255, 0), (self.leaves[i][0], self.leaves[i][1]), 5)

    def update(self):
        for i in range(len(self.leaves)):
            self.applyPhysics(i)
            self.draw(i)

    def applyPhysics(self, i):
        for j in range(len(leafBlowers)):
            angle = atan2(leafBlowers[j].xpos - self.leaves[i][0], leafBlowers[j].ypos - self.leaves[i][1])
            self.leaves[i][2] += math.cos(angle) * 1.5 #xVelo
            self.leaves[i][3] += math.sin(angle) * 1.5 #yVelo

    def drag(self, i):
        self.leaves[i][2] -= 2
        self.leaves[i][3] -= 2

    

leeevs = leafSpawner(100)

#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
    updateTicker()

    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    leeevs.update()



    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()