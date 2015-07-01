from boardBase import BoardBase 
import pygame
import random, sys
import color as c

from pygame.locals import *

class MineGame(BoardBase):

    def __init__(self):
	
	BoardBase.__init__(self) 
	self.MINES        = 10 
    	pygame.display.set_caption('DON"T SWEEP THE BIRDS')
    	self.mineLocations = self.placeMines()
    	self.boardValues = self.getBoardValues()
    	self.foundMine   = 0 
    	self.correct = []  
    	self.clicked = []
    	self.rightClicked = []
	self.correctlyFilledIndices = []


    # copy constructor
    def setMines(self,mines):
	self.MINES = mines
    	self.mineLocations = self.placeMines()


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

	print "Number of mines we're placing them....", self.MINES 
        return pairs


    #calculate the number of mines each square touches and return this matrix 
    def getBoardValues(self):
    
        temp2 = [[0 for x in range(self.NSQUARE_Y) ] for x in range(self.NSQUARE_X)]
    
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



	#Based on the position user clicks, fill in the space.  
	#Return the number of filled boxes, so can determine when user wins. 
    def fillUsersBoxes(self,i,j):

	font = pygame.font.SysFont('Arial',26)

        indices = [(i,j)]
        printTheseIndices = [(i,j)]
    
        while len(indices) > 0 : 

	    (x,y) = indices[0]
            if (x,y) in self.mineLocations:
                continue
            #print "\nNEW Coords: ", (x,y), " and count: ", boardValues[x][y]
            if self.boardValues[x][y] != 0:
		#print "Fill in clicked space..." 
            	pygame.draw.rect(self.DISPLAYSURF, c.WHITE, (self.START_X + x*self.BOX - self.SIZE/4, self.START_Y + y*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2))
            	self.DISPLAYSURF.blit(font.render(str(self.boardValues[x][y]), True, (255,0,0)), (self.START_X + x*self.BOX - self.SIZE/4+10, self.START_Y + y*self.BOX -self.SIZE/4+4, self.SIZE/2, self.SIZE/2))
            	pygame.draw.rect(self.DISPLAYSURF, c.BLUE, (self.START_X + x*self.BOX - self.SIZE/4, self.START_Y + y*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2),3)

	    elif self.boardValues[x][y] == 0:
                pygame.draw.rect(self.DISPLAYSURF, c.GRAY, (self.START_X + x*self.BOX - self.SIZE/4, self.START_Y + y*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2))
    
            if (x,y) not in self.correctlyFilledIndices:
                self.correctlyFilledIndices.append((x,y))


#           print "INDICES: ", indices
            indices.remove((x,y))

#	    print "What does this think x and y are: ", self.NSQUARE_X, self.NSQUARE_Y

            if self.boardValues[x][y] == 0 : 
		for ii in xrange(x-1,x+2):
            	    for jj in xrange(y-1,y+2):


            	        if ii >= self.NSQUARE_X or jj >= self.NSQUARE_Y or ii < 0 or jj < 0:
            	            continue

#			print "INDICES: " , (ii,jj)

            	        if (ii,jj) == (x,y):
			    continue

			if self.boardValues[ii][jj] == 0 and ((ii,jj) not in printTheseIndices): #and len(indices) is not 0: 
                    	    indices.append((ii,jj))
                    	    printTheseIndices.append((ii,jj))

                    	if self.boardValues[ii][jj] != 99 :
                    	    if self.boardValues[ii][jj] is 0:
                    	        pygame.draw.rect(self.DISPLAYSURF, c.GRAY, (self.START_X + ii*self.BOX - self.SIZE/4, self.START_Y + jj*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2))
                    	    else:
                    	        pygame.draw.rect(self.DISPLAYSURF, c.WHITE, (self.START_X + ii*self.BOX - self.SIZE/4, self.START_Y + jj*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2))
                    	        self.DISPLAYSURF.blit(font.render(str(self.boardValues[ii][jj]), True, (255,0,0)), (self.START_X + ii*self.BOX - self.SIZE/4+10, self.START_Y + jj*self.BOX -self.SIZE/4+4, self.SIZE/2, self.SIZE/2))
                    	        pygame.draw.rect(self.DISPLAYSURF, c.BLUE, (self.START_X + ii*self.BOX - self.SIZE/4, self.START_Y + jj*self.BOX -self.SIZE/4, self.SIZE/2, self.SIZE/2),3)

                    	    if (ii,jj) not in self.correctlyFilledIndices:
                    	        self.correctlyFilledIndices.append((ii,jj))
	return



	



def main():

    print "DO WE GET HERE"
    m = MineGame()

    m.fillUsersBoxes(0,1)

    while True: # main game loop
	for event in pygame.event.get():
	    if event.type == QUIT:
		pygame.quit()
		sys.exit()


if __name__=='__main__':
    main()
