import pygame
from pygame import Vector2
from buttons import Button

class Menu:
    """
    each menu needs to be set to a button that activates it.
    (set the activator button's click funciton to the menu's activate function)
    when the button is clicked, the menu will be activated and will display.
    make sure to pass a list of buttons that you want to draw and have do stuff in the buttons list.
    """

    def __init__(self, rect, color, buttonsList):
        self.rect = rect
        self.color = color
        self.buttonsList = buttonsList
        self.active = False

    def activate(self): #activates/deactivates the menu
        if self.active:
            self.active = False
        else:
            self.active = True

    def update(self, screen, mousePos):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.active = False #this makes it so that if the escape key is pressed, the menu closes

        if self.active: #if it's active, it runs draws and updates the menu
            pygame.draw.rect(screen, self.color, self.rect)
            for button in range(len(self.buttonsList)): #goes through the list of buttons for this menu and updates + draws them
                self.buttonsList[button].update(screen, mousePos)