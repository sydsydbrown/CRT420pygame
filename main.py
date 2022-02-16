#####
# This file holds all of the main functionality of our game
#####
import pygame 
import random
from Crumb import Crumb
from Knife import Knife
from Rat import Rat

# define the size of the game window
WIDTH = 1200   
HEIGHT = 800  

# load in image for play screen and win/lose/title
kitchenFloor = pygame.image.load("data/kitchenFloor.JPG")
loseScreen = pygame.image.load("data/loseScreen.JPEG")

# make the game window option
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Remy's Day Off")
# frame rate of game per second
FPS = 60
# busted switch case
switchVal = 0
# creating a player
player = Rat(WIDTH/2 - 50, 675)
# making crumbs
crumb1 = Crumb(random.randint(10, WIDTH - 10), 0, random.randint(5, 10))
crumb2 = Crumb(random.randint(10, WIDTH - 10), 0, random.randint(5, 10))
crumb3 = Crumb(random.randint(10, WIDTH - 10), 0, random.randint(5, 10))
# making knives
knife1 = Knife(random.randint(10, WIDTH - 10), 0, random.randint(10, 15))
knife2 = Knife(random.randint(10, WIDTH - 10), 0, random.randint(10, 15))

# fill background with image for play screen
WINDOW.blit(kitchenFloor, (0,0))

# this function makes you win the game with 15 points and lose if you've died
def gameConditions():
    global switchVal

    if player.points == 15:
         if player.isDead == False:
                switchVal = 2
    if player.isDead == True:
        switchVal = 3

# this function handles key presses for movement and resets
def buttonPresses():
    global switchVal

    #handle player movement from key presses
    #also handle my busted switch case if elif statement ladder
    # this gets a list of booleans showing which keys are currently pressed
    keysPressed = pygame.key.get_pressed()

    # if the 'r' key is pressed start the game
    if keysPressed[pygame.K_r] == True:
        if switchVal == 0:
            switchVal = 1
    
    # if the 'f' key is pressed go to the menu
    if keysPressed[pygame.K_f] == True:
        if switchVal > 0:
            switchVal = 0

    # if the 'a' key is pressed move left
    if keysPressed[pygame.K_a] == True:
        player.x -= player.speed

    #if the 'd' key is pressed move right
    elif keysPressed[pygame.K_d] == True:
        player.x += player.speed


def main():
# this funtion makes the window and runs the game
# it's also where other functions are called

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

        #starting/menu screen
        if switchVal == 0:
            buttonPresses()
            player.health = 5
            player.points = 0
            player.isDead = False
            #write code stuffs to put in menu screen
        
        #playing screen
        if switchVal == 1:
            # fill background with image for play screen
            WINDOW.blit(kitchenFloor, (0,0)) 

            #generic functions
            buttonPresses()
            gameConditions()

            #player functions
            player.render(WINDOW)
            player.ratDeath()

            #i need to make a function in the rat class that displays points and health with text

            # yes i could have used lists for the crumbs and knives
            # no i did not want to

            #crumb functions
            crumb1.render(WINDOW)
            crumb1.crumbMove(WIDTH, HEIGHT)
            crumb1.addPoints(player, WIDTH)
            crumb2.render(WINDOW)
            crumb2.crumbMove(WIDTH, HEIGHT)
            crumb2.addPoints(player, WIDTH)
            crumb3.render(WINDOW)
            crumb3.crumbMove(WIDTH, HEIGHT)
            crumb3.addPoints(player, WIDTH)
 
            #knife functions
            knife1.render(WINDOW)
            knife1.knifeMove(WIDTH, HEIGHT)
            knife1.takeHealth(player, WIDTH)
            knife2.render(WINDOW)
            knife2.knifeMove(WIDTH, HEIGHT)
            knife2.takeHealth(player, WIDTH)
 

        #winning screen
        if switchVal == 2:
            buttonPresses()
            #put in stuff here to load the winning screen

        #losing screen
        if switchVal == 3:
            buttonPresses()
            #put in stuff here to load the losing screen

        # put code here that should be ran every frame
        pygame.display.update()


#******************
#code to run
#******************

main()
