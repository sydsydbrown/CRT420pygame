import pygame
WIDTH = 1200   
HEIGHT = 800  
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
remyPlayer = pygame.image.load("data/remyPlayer.JPG").convert()

class Rat:

    #class vars with constant starting vals
    health = 5
    width = 100
    height = 100
    speed = 10
    points = 0
    isDead = False

    #constructor funtion
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    #render function
    def render(self, _surface):
        self.ratRect = remyPlayer.get_rect()

        #drawing rectangle
        pygame.draw.rect(_surface, (255, 0, 255), remyPlayer.get_rect())

        