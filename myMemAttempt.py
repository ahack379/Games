#! usr/bin/python

# Project 2 
# Memory Game
# 6/14/15
# Ariana Hackenburg

# A memoryGame written using some pygame tips from pygams manual 
# There are a few bugs: if you click on the same match 2x, it counts
# it 2x towards your correct match total. There are others
# no one will care about I suspect because only turkeys will play
# https://inventwithpython.com/makinggames.pdf

import pygame, sys
import random
import time

from pygame.locals import *

BOARDWIDTH   = 500
BOARDHEIGHT  = 400 
NSQUARE_Y    = 3 
NSQUARE_X    = 4 
BOX          = 60
SIZE 	     = 80
FPS 	     = 2
START_X      = (BOARDWIDTH - NSQUARE_X*BOX) / 2
START_Y      = (BOARDHEIGHT - NSQUARE_Y*BOX) / 2

assert NSQUARE_Y*NSQUARE_X % 2 == 0, "Can't have an odd number of squares"

# set up the colors
#	    R     G     B
BLACK  = (  0,    0,    0)
GRAY   = (100,  100,  100)
WHITE  = (255,  255,  255)

RED    = (255,    0,    0)
GREEN  = (  0,  255,    0)
BLUE   = (  0,    0,  255)
ORANGE = (255,  128,    0)
PURPLE = (255,    0,  255)
YELLOW = (255,  255,    0)

RANDO  = (100,  200,  209)

CIRCLE   = 'circle'
SQUARE   = 'square'
DONUT    = 'donut'
LINE     = 'line'
ELLIPSE	 = 'ellipse'


ALLCOLORS = [RED, GREEN, BLUE, ORANGE, PURPLE, YELLOW]
ALLSHAPES = [CIRCLE, SQUARE, DONUT, LINE, ELLIPSE ]
assert (len(ALLCOLORS) * len(ALLSHAPES) * 2) >= NSQUARE_Y * NSQUARE_X, "Don't have enough shapes, colors for this board"



def main(): 

    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH,BOARDHEIGHT),0,32)
    DISPLAYSURF.fill(BLACK)

    pygame.display.set_caption('How\'s your memory?')

    mainBoard = getBoard()

    pygame.display.update()
    pygame.time.wait(1000)
    getPiecesCover()

    clicks   	   = 0
    correctMatches = 0
    while True: # main game loop
	mouseClicked = False
        for event in pygame.event.get():
	   # if event.type == QUIT:
	     if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                 pygame.quit()
                 sys.exit()
             elif event.type == MOUSEMOTION:
                 mouseX, mouseY = event.pos
             elif event.type == MOUSEBUTTONUP:
                 mouseX, mouseY = event.pos
                 mouseClicked = True


	boxX, boxY = convertToBox(mouseX, mouseY)
	if boxX == None or boxY == None:
	   continue 

#	if not mouseClicked and boxX >= 0 and boxX < NSQUARE_X \
#	    and boxY >= 0 and boxY < NSQUARE_Y:
#	    drawHighlight(GREEN,boxX,boxY)
		
#	drawHighlight(BLACK,boxX,boxY)

	     
	if mouseClicked and boxX >= 0 and boxX < NSQUARE_X \
			and boxY >= 0 and boxY < NSQUARE_Y:
	    
	    color, shape = getShapeColor(mainBoard,boxX,boxY)	    
	    revealBox(shape,color,boxX,boxY)
	    pygame.display.update()

	    if clicks == 0 :
		box1X = boxX
		box1Y = boxY
		color1 = color
		shape1 = shape

	    clicks+=1

	    if clicks == 2 :
		clicks = 0
		if color == color1 and shape == shape1 and ( boxX != box1X or boxY != box1Y) :
		    correctMatches += 1

		else :
		    pygame.time.wait(1000)
		    pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + boxX*BOX - SIZE/4, START_Y + boxY*BOX -SIZE/4, SIZE/2, SIZE/2))
		    pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + box1X*BOX - SIZE/4, START_Y + box1Y*BOX -SIZE/4, SIZE/2, SIZE/2))

	if correctMatches == NSQUARE_X * NSQUARE_Y / 2:
	    youWin(mainBoard)
	    pygame.time.wait(1000)
            pygame.quit()
            sys.exit()
	    
        pygame.display.update()

def youWin(board):


    color0 = RANDO
    color1 = BLACK
    pygame.display.set_caption('YOU WIN!')
    
    for i in xrange(10):
	color0, color1 = color1, color0
	DISPLAYSURF.fill(color0)
	drawMainBoard(board)
        pygame.display.update()
	pygame.time.wait(200)
    
    
def revealBox(shape,color,boxX,boxY):
#    FPSCLOCK.tick(FPS)
    pygame.draw.rect(DISPLAYSURF, BLACK, (START_X + boxX*BOX - SIZE/4, START_Y + boxY*BOX -SIZE/4, SIZE/2, SIZE/2))
    drawShape(shape,color, boxX,boxY)
#    for i in xrange(SIZE/2+1):
#	pygame.draw.rect(DISPLAYSURF, GREEN, (START_X + boxX*BOX - SIZE/4, START_Y + boxY*BOX -SIZE/4, SIZE/2-i, SIZE/2-i))
#        pygame.display.update()



def getPiecesCover():
    for i in xrange(NSQUARE_X):
	for j in xrange(NSQUARE_Y):
	    pygame.draw.rect(DISPLAYSURF, WHITE, (START_X + i*BOX - SIZE/4, START_Y + j*BOX -SIZE/4, SIZE/2, SIZE/2))
	    

def getShapeColor(mainBoard,boxX, boxY):
    color = mainBoard[boxX][boxY][0]
    shape = mainBoard[boxX][boxY][1]

    return (color,shape)
    

def drawHighlight(color,boxX, boxY):
    SIZE = 100
    pygame.draw.rect(DISPLAYSURF, color, (START_X + boxX*BOX - SIZE/4, START_Y + boxY*BOX -SIZE/4, SIZE/2, SIZE/2),2)
    

def convertToBox(mouseX,mouseY):

    tempX = int(( mouseX - (START_X - BOX/2))/BOX)
    tempY = int(( mouseY - (START_Y - BOX/2))/BOX)
    return (tempX, tempY) 

#Get the correct number of shapes and colors 
def getBoard():
    pairs = []
    for i in ALLCOLORS:
	for j in ALLSHAPES:
	    pairs.append( (i,j))

    random.shuffle(pairs)

    #print NSQUARE_Y * NSQUARE_X /2 
    boardPieces = pairs[:int(NSQUARE_Y*NSQUARE_X/2)]
    boardPieces *= 2 
    random.shuffle(boardPieces)

    board = []
    for c in xrange(NSQUARE_X):
	row = []
	for r in xrange(NSQUARE_Y):
	    row.append(boardPieces[c*NSQUARE_Y + r])
	board.append(row)

    drawMainBoard(board)

    return board

def drawMainBoard(board):
    for i in xrange(NSQUARE_X):
#	print 'NEW COLUMN!'
	for j in xrange(NSQUARE_Y):
	    color = board[i][j][0]
	    shape = board[i][j][1]
	    drawShape(shape,color, i,j)
    
	
#Draw shape given its indices in the board
def drawShape(shape, color, posX, posY):
#    print "Should be drawing a ",color,shape

    if shape == CIRCLE: 
	pygame.draw.circle(DISPLAYSURF,color, (START_X + posX*BOX, START_Y + posY*BOX),12)
    elif shape == SQUARE:	
	pygame.draw.rect(DISPLAYSURF, color, (START_X + posX*BOX -7.5, START_Y + posY*BOX -7.5, 15, 15))
    elif shape == DONUT:
	pygame.draw.circle(DISPLAYSURF, color, (START_X + posX*BOX, START_Y + posY*BOX), 12, 5)
    elif shape == LINE:
	pygame.draw.line(DISPLAYSURF, color, (START_X + posX*BOX - 5, START_Y + posY*BOX + 8), (START_X + posX*BOX + 5, START_Y +posY*BOX - 8), 3)
    elif shape == ELLIPSE:
	pygame.draw.ellipse(DISPLAYSURF, color, (START_X + posX*BOX - 15, START_Y + posY*BOX-7.5, 30, 15))
    else:
	print "Something went wrong-- no shape detected" 




if __name__=='__main__':
    main()
