import pygame, sys
import random
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()


# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('../pics/cat.png')
turkImg = pygame.image.load('../pics/dash.png')
catx = 500
caty = 120 
turkeyx = 300 
turkeyy = 100 

Tdirection = 'left' #'right'
Cdirection = 'left' #'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
#    r = random.randint(0,3)
#    if r==0:
#        direction = 'right'
#    elif r==1:
#        direction = 'left'
#    elif r==2:
#        direction = 'up'
#    elif r==3:
#        direction = 'down'

    if turkeyx < 1:
	Tdirection='down'
    if catx < 1:
	Cdirection='down'
    if turkeyy > 250:
	Tdirection='right'
    if caty > 300:
	Cdirection='right'
    if turkeyx > 300:
	Tdirection='up'
#    print Cdirection
    if catx > 400 and Cdirection != 'left':
	Cdirection='up'

    if Tdirection == 'left':
	turkeyx -= 8 
    if Tdirection == 'right':
	turkeyx += 7 
    if Tdirection == 'up':
	turkeyy -= 4.8
    if Tdirection == 'down':
	turkeyy += 6

    if Cdirection == 'left':
	catx -= 8.5 
    if Cdirection == 'right':
	catx += 6.5
    if Cdirection == 'up':
	caty -= 10 
    if Cdirection == 'down':
	caty += 5

    
    DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.display.update()
    DISPLAYSURF.blit(turkImg, (turkeyx, turkeyy))
   # pygame.display.update()
    
    for event in pygame.event.get():
	if event.type == QUIT or caty < -20:
	    pygame.quit()
	    sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)
