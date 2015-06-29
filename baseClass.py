# Base class implementation for games using boards
# Typical things to initialize include : board dimensions, 
# number of boxes and location, conversion from mouse to box
# Ariana Hackenburg

import pygame

# set up the colors
#           R     G     B
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


class BoardBase: 
    
    def __init__(self):

        self.NSQUARE_X    = 10
        self.NSQUARE_Y    = 10
        self.BOX          = 50
        self.SIZE         = 70
	self.COLOR	  = WHITE
        self.BOARDWIDTH   = self.NSQUARE_X * 80
        self.BOARDHEIGHT  = self.NSQUARE_Y * 60
        self.START_X  = (self.BOARDWIDTH  - self.NSQUARE_X * self.BOX) / 2 
        self.START_Y  = (self.BOARDHEIGHT - self.NSQUARE_Y * self.BOX) / 2 

	pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((self.BOARDWIDTH, self.BOARDHEIGHT),0,32)
	self.initBoard()

    # copy constructor
    def setVariables(self,nsquare_X,nsquare_Y,box,size):
        self.NSQUARE_X    = nsquare_X 
        self.NSQUARE_Y    = nsquare_Y
        self.BOX          = box 
        self.SIZE         = size
        self.BOARDWIDTH   = self.NSQUARE_X * 80
        self.BOARDHEIGHT  = self.NSQUARE_Y * 60
        self.START_X  = (self.BOARDWIDTH  - self.NSQUARE_X * self.BOX) / 2 
        self.START_Y  = (self.BOARDHEIGHT - self.NSQUARE_Y * self.BOX) / 2 

    #Convert mouse coordinates to iterative box-values 
    #ie, associate clicks to individual squares
    def convertToBox(self,mouseX,mouseY):
    
        tempX = int(( mouseX - (self.START_X - self.BOX/2))/self.BOX)
        tempY = int(( mouseY - (self.START_Y - self.BOX/2))/self.BOX)
        return (tempX, tempY)
    
    
    #Draws initial white squares
    def initBoard(self):
    
        for i in xrange(self.NSQUARE_X):
            for j in xrange(self.NSQUARE_Y):
                pygame.draw.rect(self.DISPLAYSURF, self.COLOR, (self.START_X + i*self.BOX - self.SIZE/4, self.START_Y + j*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2))
    


