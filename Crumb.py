import random
import pygame

WIDTH = 1200   
HEIGHT = 800  
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
crumbItem = pygame.image.load("data/crumbItem.png")

class Crumb:

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
        self.crumbRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        WINDOW.blit(crumbItem, (self.x,self.y)) 

    #movement function
    def crumbMove(self, _width, _height):
        self.y += self.speed
        if self.y >= _height:
            self.y = 0
            self.x = random.randint(10, _width - 10)

    #interaction with player (add points)
    def addPoints(self, target, _width):
        if target.ratRect.colliderect(self.crumbRect):
            target.points += 1
            self.y = 0
            self.x = random.randint(10, _width - 10)
            print("point added")