#####
# This file will hold all of the main functionality of our game
#####
import pygame 
from Crumb import Crumb
from Knife import Knife
from Rat import Rat

# define the size of the game window
WIDTH = 1200   
HEIGHT = 800  

# make the game window option
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Remy's Day Off")
# frame rate of game per second
FPS = 60
#creating a player
player = Rat(WIDTH/2 - 50, 675)
#making a crumb
crumb = Crumb(300, 100)
#making a knife
knife = Knife(500, 100)

def main():
    # make a clock object that will be used
    # to make the game run at a constant frame rate, regulate the frame rate
    clock = pygame.time.Clock()

    # make boolean that represents whether the game should be running or not
    running = True
    # while the game is running
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        #handle player movement from key presses
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

         # if the 'w' key is pressed
        if keysPressed[pygame.K_a] == True:
            player.x -= player.speed
        elif keysPressed[pygame.K_d] == True:
            player.x += player.speed
    
        crumb.y += crumb.speed
        knife.y += knife.speed

        if crumb.y >= HEIGHT:
            crumb.y = 0
        
        if knife.y >= HEIGHT:
            knife.y = 0


        # This fills the game window to be the given RGB color
        WINDOW.fill((0,0,0))
        
        player.render(WINDOW)
        crumb.render(WINDOW)
        knife.render(WINDOW)
        # put code here that should be ran every frame
        pygame.display.update()




#******************
#code to run
#******************

main()