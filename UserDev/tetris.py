#! usr/bin/python

import pygame, sys
from pygame.locals import *

from boardBase import BoardBase as board
import color as c


pygame.display.set_caption('Drawing')

#pygame.draw.polygon(ttttttttttt, c.GREEN, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))


NSQUARE_X    = 4
NSQUARE_Y    = 5
MINES        = 3
BOX          = 50
SIZE         = 70
BOARDWIDTH   = NSQUARE_X * 80
BOARDHEIGHT  = NSQUARE_Y * 60

START_X  = (BOARDWIDTH - NSQUARE_X*BOX) / 2
START_Y  = (BOARDHEIGHT - NSQUARE_Y*BOX) / 2

car = False 


#pygame.display.set_caption('Hello World!')

def main():

    global DISPLAYSURF

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((500,400),0,32)

    while True: # main game loop
        clickFlag = 0 
        mouseClicked = False
	for event in pygame.event.get():
#	    print "this is it" 
	    
	    mouseX = 0 
	    mouseY = 0 
	    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
		pygame.quit()
		sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
		mouseX, mouseY = event.pos
		mouseClicked = True
		if event.button==3:
		    clickFlag = 1 



	    if car :
		pygame.time.wait(2000)
		pygame.quit()
		print "quitting now"
		sys.exit()


    
	    for i in xrange(20):
		i *= 3; 
		fallingPiece(i) 

		pygame.display.update()

	    boxX, boxY = convertToBox(mouseX, mouseY)

def fallingPiece(y):
	#pygame.draw.rect(DISPLAYSURF, c.GREEN, (200, 150, 100, 50))
    pygame.draw.rect(DISPLAYSURF, c.GREEN, (200, y, 100, 50))
    print "this is x" 
    
    
def convertToBox(mouseX,mouseY):

    tempX = int(( mouseX - (START_X - BOX/2))/BOX)
    tempY = int(( mouseY - (START_Y - BOX/2))/BOX)
    return (tempX, tempY)
    
    


#while True: # main game loop
#    for event in pygame.event.get():
#	if event.type == QUIT:
#	    pygame.quit()
#	    sys.exit()
#    pygame.display.update()

#sys.stdin.readlines()

if __name__ =='__main__':
    main()
