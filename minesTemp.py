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
# 4) Clean up code.  Consider using classes to organize functionality/reset variables between games.

# Things to do for this and other projects:
# 0) Create class which contains commonly used gaming needs
# ie: Initialize board, convert mouse to box coords, define colors


import pygame, sys, os
import random
#from myMemAttempt import convertToBox

from pygame.locals import *

# set up the colors
#	   R     G    B
BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
RED   =  (255,   0,   0)
GREEN =  (  0, 255,   0)
BLUE  =  (  0,   0, 255)
GRAY  =  (100, 100, 100)


NSQUARE_X    = 10 
NSQUARE_Y    = 10
MINES        = 6 
BOX 	     = 50	
SIZE 	     = 70
BOARDWIDTH   = NSQUARE_X * 80 
BOARDHEIGHT  = NSQUARE_Y * 60

START_X  = (BOARDWIDTH - NSQUARE_X*BOX) / 2
START_Y  = (BOARDHEIGHT - NSQUARE_Y*BOX) / 2

birdImg = pygame.image.load('pics/turk.png')
birdImg = pygame.transform.scale(birdImg, (BOX*7/10, BOX*7/10))

sweepImg = pygame.image.load('pics/SWEEPER.png')
sweepImg = pygame.transform.scale(sweepImg, (BOX*7/10, BOX*7/10))




def main():

    os.system('clear')
    global DISPLAYSURF
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH,BOARDHEIGHT),0,32)
    pygame.display.set_caption('DON"T SWEEP THE BIRDS')
    initBoard() 
    mineLocations = placeMines()
    boardValues = getBoardValues(mineLocations)
    foundMine   = 0 
    correct = [] 
    clicked = []
    rightClicked = []

    
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
        boxX, boxY = convertToBox(mouseX, mouseY)

        if boxX == None or boxY == None:
	    continue 

	if mouseClicked and boxX >=0 and boxX < NSQUARE_X \
			and boxY >=0 and boxY < NSQUARE_Y \
			and clickFlag == 1 \
			and (boxX, boxY) not in clicked:

	    if (boxX,boxY) in rightClicked:
		pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + boxX*BOX - SIZE/4, START_Y + boxY*BOX -SIZE/4, SIZE/2, SIZE/2))
		rightClicked.remove( (boxX, boxY) )

	    else:
		pygame.draw.rect(DISPLAYSURF, GREEN, (START_X + boxX*BOX - SIZE/4, START_Y + boxY*BOX -SIZE/4, SIZE/2, SIZE/2))
		DISPLAYSURF.blit(sweepImg,(START_X + boxX*BOX - SIZE/4-1, START_Y + boxY*BOX -SIZE/4-1, SIZE/2, SIZE/2))
		pygame.display.update()
		rightClicked.append( (boxX,boxY) ) 

	if mouseClicked and boxX >=0 and boxX < NSQUARE_X \
			and boxY >=0 and boxY < NSQUARE_Y \
			and clickFlag == 0 \
			and (boxX,boxY) not in rightClicked:

	    if (boxX, boxY) in mineLocations: 
		foundMine += 1
		DISPLAYSURF.blit(birdImg,(START_X + boxX*BOX - SIZE/4 , START_Y + boxY*BOX -SIZE/4 , SIZE/2, SIZE/2))
		pygame.display.update()

	    else:
		clicked.append( (boxX,boxY) )
		fillUsersBoxes(boxX,boxY,boardValues,mineLocations,correct)
		pygame.display.update()
#		print "CORRECT NUMBER OF BOXES: ", len(correct) 

	    #Can make this more robust.  Add list of indices which have been right clicked--when 
	    #they are correct, AND the number of clicked.  
	    if len(correct) == (NSQUARE_X * NSQUARE_Y - MINES)  :
		for (x,y) in mineLocations:
		    if (x,y) not in clicked:
			pygame.draw.rect(DISPLAYSURF, GREEN, (START_X + x*BOX - SIZE/4, START_Y + y*BOX -SIZE/4, SIZE/2, SIZE/2))
			DISPLAYSURF.blit(sweepImg,(START_X + x*BOX - SIZE/4-1, START_Y + y*BOX -SIZE/4-1, SIZE/2, SIZE/2))
		pygame.display.update()
		    
		print "\n\n\nYOU WIIIIIIN!" 
		    
  	    	pygame.time.wait(2000)
		pygame.init()

		DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH,BOARDHEIGHT),0,32)
		pygame.display.set_caption('DON"T SWEEP THE BIRDS')
		initBoard() 
	        mineLocations = placeMines()
    		boardValues = getBoardValues(mineLocations)
    		foundMine   = 0 
    		correct = [] 
    		clicked = []
		rightClicked = []
		os.system('clear')

	    if foundMine == 1:
		print "\n\n\nEXPOOOOOOOOOOSION"
  	    	print "You lose"
  	    	pygame.time.wait(1000)
		pygame.quit()
  	    	sys.exit()
	    
#Based on the position user clicks, fill in the space.  
#Return the number of filled boxes, so can determine when user wins. 
def fillUsersBoxes(i,j,boardValues,mines,correctlyFilledIndices):

#    correctlyFilledBoxes = 0
    font = pygame.font.SysFont('Arial',26)

    indices = [(i,j)]
    printTheseIndices = [(i,j)]
  #  correctlyFilledIndices = []

    while len(indices) > 0 :
	#correctlyFilledBoxes +=1  

	(x,y) = indices[0]
	if (x,y) in mines:
	    continue
	#print "\nNEW Coords: ", (x,y), " and count: ", boardValues[x][y]
	if boardValues[x][y] != 0:
	    #print "Fill in clicked space..." 
	    pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + x*BOX - SIZE/4, START_Y + y*BOX -SIZE/4, SIZE/2, SIZE/2))
	    DISPLAYSURF.blit(font.render(str(boardValues[x][y]), True, (255,0,0)), (START_X + x*BOX - SIZE/4+10, START_Y + y*BOX -SIZE/4+4, SIZE/2, SIZE/2))
	    pygame.draw.rect(DISPLAYSURF, BLUE, (START_X + x*BOX - SIZE/4, START_Y + y*BOX -SIZE/4, SIZE/2, SIZE/2),3)

	elif boardValues[x][y] == 0:
	    pygame.draw.rect(DISPLAYSURF, GRAY, (START_X + x*BOX - SIZE/4, START_Y + y*BOX -SIZE/4, SIZE/2, SIZE/2))
	    
	if (x,y) not in correctlyFilledIndices:
	    correctlyFilledIndices.append((x,y))


#	print "INDICES: ", indices
	indices.remove((x,y))


	if boardValues[x][y] == 0 :
	    for ii in xrange(x-1,x+2):
		for jj in xrange(y-1,y+2):

		    if ii >= NSQUARE_X or jj >= NSQUARE_Y or ii < 0 or jj < 0:
			continue

		    if (ii,jj) == (x,y):
			continue

		    if boardValues[ii][jj] == 0 and ((ii,jj) not in printTheseIndices): #and len(indices) is not 0: 
		#	print "Adding ", (ii,jj), "to indices" 
			indices.append((ii,jj))
			printTheseIndices.append((ii,jj))

	    	    if boardValues[ii][jj] != 99 :
			if boardValues[ii][jj] is 0:
			    pygame.draw.rect(DISPLAYSURF, GRAY, (START_X + ii*BOX - SIZE/4, START_Y + jj*BOX -SIZE/4, SIZE/2, SIZE/2))
			else:
			    pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + ii*BOX - SIZE/4, START_Y + jj*BOX -SIZE/4, SIZE/2, SIZE/2))
			    DISPLAYSURF.blit(font.render(str(boardValues[ii][jj]), True, (255,0,0)), (START_X + ii*BOX - SIZE/4+10, START_Y + jj*BOX -SIZE/4+4, SIZE/2, SIZE/2))
			    pygame.draw.rect(DISPLAYSURF, BLUE, (START_X + ii*BOX - SIZE/4, START_Y + jj*BOX -SIZE/4, SIZE/2, SIZE/2),3)

			if (ii,jj) not in correctlyFilledIndices:
			    correctlyFilledIndices.append((ii,jj))


#	    print "AFTER IT ALL : ", indices

 

   # return len(correctlyFilledIndices)


#calculate the number of mines each square touches and return this matrix 
def getBoardValues(mineLocations):

    temp2 = [[0 for x in range(NSQUARE_Y) ] for x in range(NSQUARE_X)] 

    for i in xrange(0,NSQUARE_X):
	for j in xrange(0,NSQUARE_Y):
	    if (i,j) in mineLocations:
		temp2[i][j] = 99
		continue
	    for ii in xrange(i-1,i+2):
		for jj in xrange(j-1,j+2):
		    if (ii,jj) in mineLocations:
			temp2[i][j]+=1
			
    return temp2

#Convert mouse coordinates to iterative box-values 
#ie, associate clicks to individual squares
def convertToBox(mouseX,mouseY):

    tempX = int(( mouseX - (START_X - BOX/2))/BOX)
    tempY = int(( mouseY - (START_Y - BOX/2))/BOX)
    return (tempX, tempY) 
    

#Draws initial white squares
def initBoard():

    for i in xrange(NSQUARE_X):
	for j in xrange(NSQUARE_Y):
            pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + i*BOX - SIZE/4, START_Y + j*BOX -SIZE/4, SIZE/2, SIZE/2))

#Randomly assign mine placement
def placeMines():

    taken = []

    mines = MINES
    while mines > 0:
	r = random.randint(0,NSQUARE_X*NSQUARE_Y-1)
	if r not in taken :
	    taken.append(r)

	mines -= 1

    yBox  = [] 
    xBox  = []
    pairs = []
    for i in taken:
	yBox = ( int( i / NSQUARE_X) )
	xBox = (i % NSQUARE_X )
	pairs.append( (xBox, yBox) )
	
    #print pairs
    #print "Mines 0-35: ", taken 
    return pairs
   

if __name__ == '__main__':
    main()
    
