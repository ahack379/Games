# Base class implementation for games using boards
# Typical things to initialize include : board dimensions, 
# number of boxes and location, conversion from mouse to box
# Ariana Hackenburg

import pygame
import color as c

class BoardBase: 
    
    def __init__(self):

        self.NSQUARE_X    = 4 
        self.NSQUARE_Y    = 5
        self.BOX          = 50
        self.SIZE         = 70
	self.COLOR	  = c.WHITE
        self.BOARDWIDTH   = self.NSQUARE_X * 80
        self.BOARDHEIGHT  = self.NSQUARE_Y * 60
        self.START_X  = (self.BOARDWIDTH  - self.NSQUARE_X * self.BOX) / 2 
        self.START_Y  = (self.BOARDHEIGHT - self.NSQUARE_Y * self.BOX) / 2 

	pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((self.BOARDWIDTH, self.BOARDHEIGHT),0,32)
	self.initBoard()

    #Set box width, and spacing + box width
    def setBoardVariables(self,nsquare_X,nsquare_Y):
        self.NSQUARE_X    = nsquare_X 
        self.NSQUARE_Y    = nsquare_Y
        self.BOARDWIDTH   = self.NSQUARE_X * 80
        self.BOARDHEIGHT  = self.NSQUARE_Y * 60
        self.START_X  = (self.BOARDWIDTH  - self.NSQUARE_X * self.BOX) / 2 
        self.START_Y  = (self.BOARDHEIGHT - self.NSQUARE_Y * self.BOX) / 2 
	return


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
    


