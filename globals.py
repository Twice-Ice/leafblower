#sets window to fullscreen and monitor resolution
import pygame
pygame.init()
from pygame.math import Vector2
SCREEN_X = pygame.display.get_desktop_sizes()[0][0]
SCREEN_Y = pygame.display.get_desktop_sizes()[0][1]
SCREEN_X = 1280
SCREEN_Y = 720
FPS = 60