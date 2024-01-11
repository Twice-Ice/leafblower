import pygame
import random
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

def updateTicker():
    global ticker
    if ticker < 60:
        ticker += 1
    else:
        ticker = 0

class leafSpawner:
    def __init__(self, leaves):
        self.xpos = screenX/2 #position for the leaf spawner to be. This doesn't really affect anything but I thought it might be nice to have.
        self.ypos = screenY/2
        self.colors = []
        self.leaves = []
        for i in range(leaves): #creates a 2d list containing each leaf.
            YY = random.randint(0, screenY)
            self.leaves.append([random.randint(0, screenX), YY, 0, 0]) #xpos, ypos, xvelo, yvelo
            print("Y = ", YY)

    def draw(self):
        for i in range(len(self.leaves)):
            pygame.draw.circle(screen, (0, 255, 0), (self.leaves[i][1], self.leaves[i][2]), 10)
            print(self.leaves[i][2])

    

leeevs = leafSpawner(100)

#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
    updateTicker()

    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    leeevs.draw()



    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()