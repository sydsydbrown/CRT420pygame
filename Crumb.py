import pygame

class Crumb:

    #class vars with constant starting vals
    width = 10
    height = 10
    speed = 10

    #constructor funtion
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    #render function
    def render(self, _surface):
        crumbRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (255, 200, 200), crumbRect)