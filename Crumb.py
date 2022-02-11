import random
import pygame

from main import WIDTH

class Crumb:

    #class vars with constant starting vals
    width = 10
    height = 10
    speed = 5

    #constructor funtion
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    #render function
    def render(self, _surface):
        crumbRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (219, 167, 77), crumbRect)

    #movement function
    def crumbMove(self):
        self.y += 5

    #interaction with player (add points)
    def addPoints(self, target):
        if target.rect.collideRect(self.rect):
            target.points += 1
            self.y = 0
            self.x = random(0, WIDTH)
            print("point added")