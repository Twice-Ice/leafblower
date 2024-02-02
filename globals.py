#sets window to fullscreen and monitor resolution
import pygame
pygame.init()
from pygame.math import Vector2
FULLSCREEN_X = pygame.display.get_desktop_sizes()[0][0]
FULLSCREEN_Y = pygame.display.get_desktop_sizes()[0][1]
DEFAULTSCREEN_X = 1280
DEFAULTSCREEN_Y = 720
screen_X = DEFAULTSCREEN_X
screen_Y = DEFAULTSCREEN_Y
# screen_X = FULLSCREEN_X
# screen_Y = FULLSCREEN_Y
FPS = 60