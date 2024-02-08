import pygame
import math
import random
from globals import screen_X, screen_Y

class Drone:
    def __init__(self, xpos, ypos, scale):
        self.pos = pygame.Vector2(xpos, ypos)
        self.speed = 3
        self.angle = random.randint(0, 360)
        self.size = 100
        self.power = 500
        self.tempCircleSize = 20
        self.velo = pygame.Vector2(self.speed, self.speed)
        self.scale = scale

    def update(self, screen):
        self.move()
        pygame.draw.circle(screen, (255, 255, 255), (self.pos.x, self.pos.y), self.tempCircleSize*self.scale)

    def move(self):
        if self.pos.x < 0 + self.tempCircleSize or self.pos.x > screen_X - self.tempCircleSize:
            self.velo.x *= -1
        if self.pos.y < 0 + self.tempCircleSize or self.pos.y > screen_Y - self.tempCircleSize:
            self.velo.y *= -1
        self.pos.x += math.cos(self.angle) * self.velo.x
        self.pos.y += math.sin(self.angle) * self.velo.y