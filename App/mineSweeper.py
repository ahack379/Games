#! usr/bin/python

# Project 3 
# Minesweeper
# 6/21/15
# Ariana Hackenburg

# Features still unimplemented:
# DONE: 0) Introductory screen which explains controls to player
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
import time
import shutil, tempfile
#from myMemAttempt import convertToBox

from pygame.locals import *
from Base.minesClass import MineGame
import Base.color as c

def main():

    os.system('clear')
    pygame.init()



    start = time.time()

    m = MineGame()
    birdImg = pygame.image.load('../pics/turk.png')
    birdImg = pygame.transform.scale(birdImg, (m.BOX*7/10, m.BOX*7/10))
    
    sweepImg = pygame.image.load('../pics/SWEEPER.png')
    sweepImg = pygame.transform.scale(sweepImg, (m.BOX*7/10, m.BOX*7/10))

  #  m.introScreen()

    m.initBoard()


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

	    if len(m.correctlyFilledIndices) == (m.NSQUARE_X * m.NSQUARE_Y - m.MINES)  :
		for (x,y) in m.mineLocations:
		    if (x,y) not in m.clicked:
			pygame.draw.rect(m.DISPLAYSURF, c.GREEN, (m.START_X + x*m.BOX - m.SIZE/4, m.START_Y + y*m.BOX -m.SIZE/4, m.SIZE/2, m.SIZE/2))
			m.DISPLAYSURF.blit(sweepImg,(m.START_X + x*m.BOX - m.SIZE/4-1, m.START_Y + y*m.BOX -m.SIZE/4-1, m.SIZE/2, m.SIZE/2))
		pygame.display.update()
		    
		print "\n\n\nYOU WIIIIIIN!" 
		#scoreKeep(start) #,scores)
		    
  	    	pygame.time.wait(2000)
		pygame.init()

		m = MineGame()
		m.initBoard()
		start = time.time()
		#os.system('clear')

	    if m.foundMine == 1:
		print "\n\n\nI'm sorry. You've been eaten. Better luck next time"
  	    	pygame.time.wait(2000)
		pygame.quit()
  	    	sys.exit()

def scoreKeep(start): #,target):
    
    target = open("scores.txt",'rw')

    nScores = 5
    time.clock()    
    elapsed = 0
    elapsed = time.time() - start
    print "The game took you: ",  elapsed, " seconds." 
    name = raw_input("Enter your name: ")
#    print "Writing your score to file..." 
    
    score    = []

#    for line in target:
#	score.append((target[0],target[1]))
#	print "Score starts as: ", score
    
    score.append((name,elapsed))    
#    score.sort(key = lambda x: x[1] )
#    print "Score array now is : ", score 


    length = len(score)  

    tempFile = open("temp.txt",'w+b')

    for line in tempFile:
	print "Line is: ", line

    tempFile.seek(0)
 #   tempFile.write(" PLAYER   SCORE\n" )
    if length > nScores:
	for x in xrange(nScores):
	    tempFile.write(str(score[x])) 

    else: 
	for x in xrange(length):
	    tempFile.write(str(score[x]))
	    print "Writing score to file..." 


#    for line in tempFile:
#	print "this is my line " , line
    #target = tempFile 

#    os.system("cp temp.txt temp2.txt")   
 #   os.system("rm temp.txt" )

    time.sleep(1)  	    

if __name__ == '__main__':
    main()
    
