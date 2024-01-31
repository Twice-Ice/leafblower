import pygame
from pygame.math import Vector2
from pygame import Rect
pygame.init

class Button:
    def __init__(self, xpos, ypos, width, height, callFunction):
        self.callFunction = callFunction
        self.rect = Rect(xpos, ypos, width, height)

    def update(self, screen, mouse):
        self.draw(screen)
        self.collisions(mouse)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def collisions(self, mouse):
        if self.rect.collidepoint(mouse):
            self.callFunction()