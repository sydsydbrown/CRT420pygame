import random
import pygame

from main import WIDTH

class Knife:

    #class vars with constant starting vals
    width = 10
    height = 10
    speed = 7

    #constructor funtion
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    #render function
    def render(self, _surface):
        knifeRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (122, 117, 106), knifeRect)

    #movement function
    def knifeMove(self):
        self.y += 7
    
    #interaction with player (take health)
    def takeHealth(self, target):
        if target.rect.collideRect(self.rect):
            target.health -= 1
            self.y = 0
            self.x = random(0, WIDTH)
            print("taken health")