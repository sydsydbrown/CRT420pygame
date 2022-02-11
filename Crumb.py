import random
import pygame


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
        self.crumbRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (219, 167, 77), self.crumbRect)

    #movement function
    def crumbMove(self, aWidth, aHeight):
        self.y += self.speed
        if self.y >= aHeight:
            self.y = 0
            self.x = random.randint(0, aWidth)

    #interaction with player (add points)
    def addPoints(self, target, aWidth):
        if target.ratRect.colliderect(self.crumbRect):
            target.points += 1
            self.y = 0
            self.x = random.randint(0, aWidth)
            print("point added")