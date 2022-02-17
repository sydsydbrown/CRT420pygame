import random
import pygame
WIDTH = 1200   
HEIGHT = 800  
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
knifeItem = pygame.image.load("data/knifeItem.png")

class Knife:

    #class vars with constant starting vals
    width = 10
    height = 10

    #constructor funtion
    def __init__(self, _x, _y, _speed):
        self.x = _x
        self.y = _y
        self.speed = _speed
    
    #render function
    def render(self, _surface):
        self.knifeRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        WINDOW.blit(knifeItem, (self.x,self.y)) 

    #movement function
    def knifeMove(self, _width, _height):
        self.y += self.speed
        if self.y >= _height:
            self.y = 0
            self.x = random.randint(10, _width - 10)
    
    #interaction with player (take health)
    def takeHealth(self, _target, _width):
        if _target.ratRect.colliderect(self.knifeRect):
            _target.health -= 1
            self.y = 0
            self.x = random.randint(10, _width - 10)
            print("taken health")