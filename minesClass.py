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



    def introScreen(self):
        font = pygame.font.SysFont('Arial',26)
        DISPLAY = pygame.display.set_mode((self.BOARDWIDTH, self.BOARDHEIGHT),0,32)   
    
        text = font.render(' The turkies are loose! Your help needed to sweep them all up. ', True, c.BLACK, c.YELLOW)
        textRect = text.get_rect()
        textRect.centerx = DISPLAY.get_rect().centerx
        textRect.centery = DISPLAY.get_rect().centery - self.BOARDHEIGHT/2 * 0.5 
        DISPLAY.blit(text,textRect)
        pygame.display.update()
    
        scale = self.MINES * 0.3 
        turkey2 = pygame.image.load('pics/turk.png')
        turkey2 = pygame.transform.scale(turkey2, (2*self.BOX, 2*self.BOX))
    
        for i in xrange(self.MINES*3):
    
            rx = random.randint(10, self.BOARDWIDTH - self.BOARDWIDTH * 0.15)
            ry = random.randint(0 + self.BOARDHEIGHT/3 , self.BOARDHEIGHT - self.BOARDHEIGHT*0.2)
            DISPLAY.blit(turkey2,(rx,ry,self.SIZE*scale, self.SIZE*scale))
            pygame.display.update()
            pygame.time.wait(60)
    
        pygame.time.wait(1000)
        
    
        textRect.centerx = DISPLAY.get_rect().centerx - 25  
        text2 = font.render(' Be careful though! Get too near a turkey and brotha may eat you... ', True, c.BLACK, c.GREEN)
        DISPLAY.blit(text2,textRect)
        pygame.display.update()
        pygame.time.wait(3000)
    
    
        openImg = pygame.image.load('pics/open.png')
        openImg = pygame.transform.scale(openImg, (10*self.BOX, 10*self.BOX))
        textRect.centerx = DISPLAY.get_rect().centerx - 40
        text3 = font.render(' Left click on the squares for clues about where turkeys are lurking... ', True, c.BLACK, c.YELLOW)
        DISPLAY.blit(text3,textRect)
        pygame.display.update()
        pygame.time.wait(3000)
    
        DISPLAY.fill(c.BLACK)
        DISPLAY.blit(openImg,(self.BOARDWIDTH/6,self.BOARDHEIGHT/8,self.SIZE*scale, self.SIZE*scale))
        textRect.centerx = DISPLAY.get_rect().centerx - 10
        textRect.centery = DISPLAY.get_rect().centery - self.BOARDHEIGHT/2 * 0.8
        text4 = font.render(' Red numbers indicate how many turkeys threaten your location. ', True, c.BLACK, c.YELLOW)
        DISPLAY.blit(text4,textRect)
        pygame.display.update()
        pygame.time.wait(3000)
    
    
        protect = pygame.image.load('pics/protect.png')
        protect = pygame.transform.scale(protect, (10*self.BOX, 10*self.BOX))
        DISPLAY.fill(c.BLACK)
        DISPLAY.blit(protect,(self.BOARDWIDTH/6,self.BOARDHEIGHT/8,self.SIZE*scale, self.SIZE*scale))
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
        textRect.centerx = DISPLAY.get_rect().centerx + 100
        textRect.centery = DISPLAY.get_rect().centery
        DISPLAY.blit(text7,textRect)
        pygame.display.update()
        pygame.time.wait(3000)
    
        DISPLAY.fill(c.BLACK)







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
