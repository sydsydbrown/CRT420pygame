import pygame

class Button:
    #class vars with constant starting vals
    isPressed = False

    #constructor funtion
    def __init__(self, _x, _y, _width, _height):
        self.x = _x
        self.y = _y
        self.width = _width
        self.height = _height
    
    #render function
    def render(self, _surface):
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (255, 0, 255), self.buttonRect)

    #collision detection
    def clickButton(self):
        
        if pygame.mouse.get_pressed == True:
            if pygame.mouse.rect.colliderect(self.buttonRect):
                self.isPressed = True
                print("button was pressed")
        
        if self.isPressed == True:
            self.isPressed = False
