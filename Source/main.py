import pygame, sys, random
from pygame.locals import *


# Initialize Pygame
pygame.init()

# Set up the window
title = "Pac-man Game"
WINDOWWIDTH = 950
WINDOWHEIGHT = 700
# windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
screen = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)

pygame.display.set_caption(title)

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)


# Set up the variables
player = pygame.Rect(400, 300, 40, 40)

MOVELEFT = False
MOVERIGHT = False
MOVEUP = False
MOVEDOWN = False
SPEED = 6
score = 0
gameOver = False

# Run the game loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    