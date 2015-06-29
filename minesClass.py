from baseClass import BoardBase 
import pygame
import random, sys

from pygame.locals import *

class MineGame(BoardBase):

    def __init__(self):
	
	BoardBase.__init__(self) 
	self.MINES        = 6
    	#self.DISPLAYSURF = pygame.display.set_mode((self.BOARDWIDTH, self.BOARDHEIGHT),0,32)
    	pygame.display.set_caption('DON"T SWEEP THE BIRDS')
    #	self.initBoard() 
    	self.mineLocations = self.placeMines()
    	self.boardValues = self.getBoardValues()
#	self.placeMines()
    	self.foundMine   = 0 
    	self.correct = []  
    	self.clicked = []
    	self.rightClicked = []

    # copy constructor
    def setVariables(self,mines):
	self.MINES = mines


    #Randomly assign mine placement
    def placeMines(self):
    
        taken = []
    
        mines = self.MINES
        while mines > 0:
            r = random.randint(0,self.NSQUARE_X*self.NSQUARE_Y-1)
            if r not in taken :
                taken.append(r)
    
            mines -= 1
    
        yBox  = []
        xBox  = []
        pairs = []
        for i in taken:
            yBox = ( int( i / self.NSQUARE_X) )
            xBox = (i % self.NSQUARE_X )
            pairs.append( (xBox, yBox) )
    
        #print pairs
        #print "Mines 0-35: ", taken 
        return pairs


    #calculate the number of mines each square touches and return this matrix 
    def getBoardValues(self):
    
        temp2 = [[0 for x in range(self.NSQUARE_Y) ] for x in range(self.NSQUARE_X)]
    
	print self.NSQUARE_X, " SAKJHDS"
        for i in xrange(0,self.NSQUARE_X):
            for j in xrange(0,self.NSQUARE_Y):
                if (i,j) in self.mineLocations:
                    temp2[i][j] = 99
                    continue
                for ii in xrange(i-1,i+2):
                    for jj in xrange(j-1,j+2):
                        if (ii,jj) in self.mineLocations:
                            temp2[i][j]+=1
    
        return temp2


	



def main():

   # pygame.init()
    print "DO WE GET HERE"
   # DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
    m = MineGame()
    #pygame.display.update()
    #foundMine = 0

#    DISPLAYSURF.fill(WHITE)

    while True: # main game loop
	for event in pygame.event.get():
	    if event.type == QUIT:
		pygame.quit()
		sys.exit()







#print "How many found mines? ", s.foundMine
#print "Board params: ", s.NSQUARE_X, s.NSQUARE_Y, s.BOX
#
#s.setVariables(6)
#print "Board params: ", s.NSQUARE_X, s.NSQUARE_Y, s.BOX
#
##print s.getBoardValues( [(0,1)] )
#
#print s.convertToBox( 0,0.331 )

if __name__=='__main__':
    main()
