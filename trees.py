import pygame
import random
screen = pygame.display.set_mode((800,800))
gameover = False
class Tree:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, screen):
        pygame.draw.circle(screen,(250,0,0),(50,500),5)
        
class Forest:
    def __init__(self, numOfTrees):
        self.trees = []
        for top in (numOfTrees/4):
            self.trees.append(Tree(0, 0))#top left to top right for X, and then 0 for Y

    def draw(self, screen):
        pass
        #loop through all tress in self.trees, and then do self.tress[i].draw(screen)