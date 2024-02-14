import pygame
from pygame import Vector2
from buttons import Button
from miscClasses import TextDisplay

BUTTONS = 0
TEXT = 1
class Menu:
    """
    each menu needs to be set to a button that activates it.
    (set the activator button's click funciton to the menu's activate function)
    when the button is clicked, the menu will be activated and will display.
    make sure to pass a list of buttons that you want to draw and have do stuff in the buttons list.
    """

    def __init__(self, rect, color, buttonsList, textList):
        self.rect = rect
        self.color = color
        self.buttonsList = buttonsList
        self.textList = []
        for i in range(len(textList)):
            self.textList.append(TextDisplay(textList[i][0], textList[i][1], textList[i][2]))
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

        if self.active: #if active, the menu is drawn
            pygame.draw.rect(screen, self.color, self.rect) #background of the menu
            for button in range(len(self.buttonsList)):#buttons list
                self.buttonsList[button].update(screen, mousePos)
            for text in range(len(self.textList)):#text list
                self.textList[text].update(screen)