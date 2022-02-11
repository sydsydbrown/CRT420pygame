import pygame

class Button:
    #class vars with constant starting vals
    width = 100
    height = 100
    isPressed = False

    #constructor funtion
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    #render function
    def render(self, _surface):
        buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #drawing rectangle
        pygame.draw.rect(_surface, (255, 0, 255), buttonRect)

    #collision detection
    def clickButton(self):
        if isPressed == True:
            isPressed = False
        
        if pygame.mouse.get_pressed == True:
            if pygame.mouse.rect.collideRect(self.rect):
                isPressed = True
                print("button was pressed")
