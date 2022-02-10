#####
# This file will hold all of the main functionality of our game
#####
import pygame 

# define the size of the game window
WIDTH = 1200   
HEIGHT = 800  

# make the game window option
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Best Game")
# frame rate of game per second

# yellow ship image

yellowShipImg = pygame
FPS = 60

def main():
    # make a clock object that will be used
    # to make the game run at a constant frame rate, regulate the frame rate
    clock = pygame.time.Clock()

    # make boolean that represents whether the game should be running or not
    running = true
    # while the game is running
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = false

        # put code here that should be ran every frame
        pygame.display.update()

##please work
