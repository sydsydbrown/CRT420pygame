import random
import pygame


class Knife:

    #class vars with constant starting vals
    width = 10
    height = 10
    speed = random.randint(10, 15)

    #constructor funtion
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    #render function
    def render(self, _surface):
        self.knifeRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (122, 117, 106), self.knifeRect)

    #movement function
    def knifeMove(self, aWidth, aHeight):
        self.y += self.speed
        if self.y >= aHeight:
            self.y = 0
            self.x = random.randint(0, aWidth)
    
    #interaction with player (take health)
    def takeHealth(self, target, aWidth):
        if target.ratRect.colliderect(self.knifeRect):
            target.health -= 1
            self.y = 0
            self.x = random.randint(0, aWidth)
            print("taken health")