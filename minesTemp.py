#! usr/bin/python

# Project 3 
# Minesweeper
# 6/21/15
# Ariana Hackenburg

# Features still unimplemented:
# 0) Introductory screen which explains controls to player
# DONE: 1) Implement feature to make protective sweeper impossible to click on until you un-right click him
# 2) Make winning and losing screens:
#    a) Winning: All the turkey's being swept away
#    b) Losing: Turkey running away from broom
# 3) Store high scores for future reference
# 4) Clean up code.  
# MOSTLY DONE,STILL SOME BUGS : 5) Implement classes to organize functionality/reset variables between games.

# Things to do for this and other projects:
# 0) Create class which contains commonly used gaming needs
# ie: Initialize board, convert mouse to box coords, define colors


import pygame, sys, os
import random
#from myMemAttempt import convertToBox

from pygame.locals import *
from minesClass import MineGame
import color as c

def main():

    os.system('clear')
    pygame.init()

    m = MineGame()
    birdImg = pygame.image.load('pics/turk.png')
    birdImg = pygame.transform.scale(birdImg, (m.BOX*7/10, m.BOX*7/10))
    
    sweepImg = pygame.image.load('pics/SWEEPER.png')
    sweepImg = pygame.transform.scale(sweepImg, (m.BOX*7/10, m.BOX*7/10))

    introScreen(m,birdImg,sweepImg)

    m.initBoard()

   # print "mines : ", m.MINES 



    while True: # main game loop
	clickFlag = 0
	mouseClicked = False
        for event in pygame.event.get():
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

    
        pygame.display.update()
        boxX, boxY = m.convertToBox(mouseX, mouseY)

        if boxX == None or boxY == None:
	    continue 

	if mouseClicked and boxX >=0 and boxX < m.NSQUARE_X \
			and boxY >=0 and boxY < m.NSQUARE_Y \
			and clickFlag == 1 \
			and (boxX, boxY) not in m.clicked:

	    if (boxX,boxY) in m.rightClicked:
		pygame.draw.rect(m.DISPLAYSURF, c.WHITE, (m.START_X + boxX*m.BOX - m.SIZE/4, m.START_Y + boxY*m.BOX -m.SIZE/4, m.SIZE/2, m.SIZE/2))
		m.rightClicked.remove( (boxX, boxY) )

	    else:
		pygame.draw.rect(m.DISPLAYSURF, c.GREEN, (m.START_X + boxX*m.BOX - m.SIZE/4, m.START_Y + boxY*m.BOX -m.SIZE/4, m.SIZE/2, m.SIZE/2))
		m.DISPLAYSURF.blit(sweepImg,(m.START_X + boxX*m.BOX - m.SIZE/4-1, m.START_Y + boxY*m.BOX -m.SIZE/4-1, m.SIZE/2, m.SIZE/2))
		pygame.display.update()
		m.rightClicked.append( (boxX,boxY) ) 

	if mouseClicked and boxX >=0 and boxX < m.NSQUARE_X \
			and boxY >=0 and boxY < m.NSQUARE_Y \
			and clickFlag == 0 \
			and (boxX,boxY) not in m.rightClicked:

	    if (boxX, boxY) in m.mineLocations: 
		m.foundMine += 1
		m.DISPLAYSURF.blit(birdImg,(m.START_X + boxX*m.BOX - m.SIZE/4 , m.START_Y + boxY*m.BOX -m.SIZE/4 , m.SIZE/2, m.SIZE/2))
		pygame.display.update()

	    else:
		m.clicked.append( (boxX,boxY) )
		m.fillUsersBoxes(boxX,boxY)
		pygame.display.update()
#		print "CORRECT NUMBER OF BOXES: ", len(m.correctlyFilledIndices) 

	    if len(m.correctlyFilledIndices) == (m.NSQUARE_X * m.NSQUARE_Y - m.MINES)  :
		for (x,y) in m.mineLocations:
		    if (x,y) not in m.clicked:
			pygame.draw.rect(m.DISPLAYSURF, c.GREEN, (m.START_X + x*m.BOX - m.SIZE/4, m.START_Y + y*m.BOX -m.SIZE/4, m.SIZE/2, m.SIZE/2))
			m.DISPLAYSURF.blit(sweepImg,(m.START_X + x*m.BOX - m.SIZE/4-1, m.START_Y + y*m.BOX -m.SIZE/4-1, m.SIZE/2, m.SIZE/2))
		pygame.display.update()
		    
		print "\n\n\nYOU WIIIIIIN!" 
		    
  	    	pygame.time.wait(2000)
		pygame.init()

		m = MineGame()
		m.initBoard()
		#os.system('clear')

	    if m.foundMine == 1:
		print "\n\n\nEXPOOOOOOOOOOSION"
  	    	print "You lose"
  	    	pygame.time.wait(2000)
		pygame.quit()
  	    	sys.exit()
	    
#m is mineClass
def introScreen(m,turkey,sweeper):
    font = pygame.font.SysFont('Arial',26)
    DISPLAY = pygame.display.set_mode((m.BOARDWIDTH, m.BOARDHEIGHT),0,32)   

    text = font.render(' The turkies are lose! Your help needed to sweep them all up. ', True, c.BLACK, c.YELLOW)
    textRect = text.get_rect()
    textRect.centerx = DISPLAY.get_rect().centerx
    textRect.centery = DISPLAY.get_rect().centery - m.BOARDHEIGHT/2 * 0.5
    DISPLAY.blit(text,textRect)
    pygame.display.update()

    scale = m.MINES * 0.3 
    turkey2 = pygame.image.load('pics/turk.png')
    turkey2 = pygame.transform.scale(turkey2, (2*m.BOX, 2*m.BOX))

    for i in xrange(m.MINES*3):

	rx = random.randint(10, m.BOARDWIDTH - m.BOARDWIDTH * 0.15)
	ry = random.randint(0 + m.BOARDHEIGHT/3 , m.BOARDHEIGHT - m.BOARDHEIGHT*0.2)
	DISPLAY.blit(turkey2,(rx,ry,m.SIZE*scale, m.SIZE*scale))
	pygame.display.update()
	pygame.time.wait(100)

    pygame.time.wait(1000)
	

#    DISPLAY.fill(c.BLACK)
    textRect.centerx = DISPLAY.get_rect().centerx - 25 
    text2 = font.render(' Be careful though! Get too near a turkey and brotha may eat you... ', True, c.BLACK, c.GREEN)
    DISPLAY.blit(text2,textRect)
    pygame.display.update()
    pygame.time.wait(3000)


    openImg = pygame.image.load('pics/open.png')
    openImg = pygame.transform.scale(openImg, (10*m.BOX, 10*m.BOX))
    textRect.centerx = DISPLAY.get_rect().centerx - 40
    text3 = font.render(' Left click on the squares for clues about where turkeys are lurking... ', True, c.BLACK, c.YELLOW)
    DISPLAY.blit(text3,textRect)
    pygame.display.update()
    pygame.time.wait(3000)
    
    DISPLAY.fill(c.BLACK)
    DISPLAY.blit(openImg,(m.BOARDWIDTH/6,m.BOARDHEIGHT/8,m.SIZE*scale, m.SIZE*scale))
    textRect.centerx = DISPLAY.get_rect().centerx - 10
    textRect.centery = DISPLAY.get_rect().centery - m.BOARDHEIGHT/2 * 0.8
    text4 = font.render(' Red numbers indicate how many turkeys threaten your location. ', True, c.BLACK, c.YELLOW)
    DISPLAY.blit(text4,textRect)
    pygame.display.update()
    pygame.time.wait(3000)


    protect = pygame.image.load('pics/protect.png')
    protect = pygame.transform.scale(protect, (10*m.BOX, 10*m.BOX))
    DISPLAY.fill(c.BLACK)
    DISPLAY.blit(protect,(m.BOARDWIDTH/6,m.BOARDHEIGHT/8,m.SIZE*scale, m.SIZE*scale))
    text5 = font.render('Right click on a suspicious location for protection. ', True, c.BLACK, c.GREEN)
    textRect.centerx = DISPLAY.get_rect().centerx + 50
    DISPLAY.blit(text5,textRect)
    pygame.display.update()
    pygame.time.wait(3000)

    text6 = font.render(' A sweeper will appear to protect your feathers for the rest of the game. ', True, c.BLACK, c.YELLOW)
    textRect.centerx = DISPLAY.get_rect().centerx - 55 
    DISPLAY.blit(text6,textRect)
    pygame.display.update()
    pygame.time.wait(3000)


    DISPLAY.fill(c.BLACK)
    text7 = font.render(' Find all safe locations to win. Good luck! ', True, c.GREEN, c.BLACK)
    textRect.centerx = DISPLAY.get_rect().centerx + 80 
    textRect.centery = DISPLAY.get_rect().centery 
    DISPLAY.blit(text7,textRect)
    pygame.display.update()
    pygame.time.wait(3000)
    
    DISPLAY.fill(c.BLACK)


if __name__ == '__main__':
    main()
    
