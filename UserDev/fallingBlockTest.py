#! usr/bin/python

import pygame, sys
import random
import math
from pygame.locals import *
from Base.boardBase import BoardBase as board
import Base.color as c


FPS = 20 # frames per second setting
fpsClock = pygame.time.Clock()

NSQUARE_X    = 4
NSQUARE_Y    = 5
BOX          = 50
SIZE         = 70
BOARDWIDTH   = NSQUARE_X * 80
BOARDHEIGHT  = NSQUARE_Y * 60

START_X  = (BOARDWIDTH - NSQUARE_X*BOX) / 2
START_Y  = (BOARDHEIGHT - NSQUARE_Y*BOX) / 2

X = 100
Y = 100
LEN = 20

car = False 
pygame.display.set_caption('Don\'t get hit')


def main():

    global DISPLAYSURF

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
    y_trans = -50 
    x_trans = 0

    enter = False
    right = False
    left  = False
    down  = False
    new   = True
    color = c.GREEN

    MOVE_Y = pygame.USEREVENT+1
    pygame.time.set_timer(MOVE_Y,1100)

    while True: # main game loop
        clickFlag = 0 
        mouseClicked = False
	move	     = False

	if new :
	    color = randomSelection()
	    new = False
	    points_start = [(X, Y), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN,Y + 2*LEN),(X + 2*LEN, Y + 2*LEN), (X + 2*LEN, Y + LEN), (X + LEN,Y + LEN), (X + LEN,Y) ]
	    new_points = points_start 

	for event in pygame.event.get():
	    
	    points_array = []
	    mouseX = 0 
	    mouseY = 0 

	    keys = pygame.key.get_pressed()

	    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
		pygame.quit()
		sys.exit()
            if event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            if event.type == MOUSEBUTTONUP:
		mouseX, mouseY = event.pos
		mouseClicked = True
		if event.button==3:
		    clickFlag = 1 
	    if event.type == MOVE_Y:
		move = True
		print "move is in business"

	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RETURN:
		    enter = True
		elif event.key == pygame.K_RIGHT:
		    right = True
		elif event.key == pygame.K_LEFT:
		    left  = True
		elif event.key == pygame.K_DOWN:
		    down = True

	    elif event.type == pygame.KEYUP:
		if event.key == pygame.K_RETURN:
		    enter = False 
		elif event.key == pygame.K_RIGHT:
		    right = False
		elif event.key == pygame.K_LEFT:
		    left  = False
		elif event.key == pygame.K_DOWN:
		    down  = False

	    
	if enter:
	    for i in xrange(len(points_start)):
	        list(new_points)
	        new_pt = rotatePoint(points_start[3],new_points[i])
	        new_points[i] = new_pt

	    pygame.display.update()

	if maxY(new_points) >= 350:
	    translatePoint(new_points,x_trans,370 - maxY(new_points))
	    pygame.display.update()
	    
	
	if right or left or down:
	    if right and x_trans < 320:
		x_trans += 30
	    elif left and x_trans > -70:
		x_trans -= 30
	    elif down and y_trans <= 200 :
		y_trans += 60

	if y_trans >= 500: 
	    pygame.quit()
	    print "quitting now"
	    sys.exit()
	    
	if move:
	    y_trans += 30; 
	    pygame.display.update()

	trans_pts = translatePoint(new_points,x_trans,y_trans)
	for pt in trans_pts:
	    print "New points are: ", pt[0], pt[1]
	fallingPiece(color, trans_pts) 
	pygame.display.update()
	pygame.time.wait(100)

	if y_trans > 200: #maxY(trans_pts) > 350:
	    pygame.time.wait(300)
	    pygame.display.set_mode((500,400),0,32)
	    y_trans = -50
	    x_trans = 0
	    new     = True
	    print "back to y and x = 0 "
	
#	    boxX, boxY = convertToBox(mouseX, mouseY)

def maxY(points):

    list(points)
    max_y = -100
    for pt in points:
	print 'x and y : ', pt[0], pt[1]
	if pt[1] > max_y:
	   max_y = pt[1]

    print "what y are we returnign", max_y

    return max_y

def fallingPiece(color,points):

    DISPLAYSURF.fill(c.BLACK)
    pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7]) )
    pygame.display.update()
    for pt in points:
	print "god damn new point is: ", pt
    
    
def convertToBox(mouseX,mouseY):

    tempX = int(( mouseX - (START_X - BOX/2))/BOX)
    tempY = int(( mouseY - (START_Y - BOX/2))/BOX)
    return (tempX, tempY)
    

def randomSelection():

    colors = [ c.GRAY,c.WHITE,c.RED,c.GREEN,
               c.BLUE,c.ORANGE,c.PURPLE,c.YELLOW,c.RANDO ]
    
    r = random.randint(0,len(colors)-1)

    return colors[r]

def rotatePoint(centerPoint,point):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(90)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

def translatePoint(points,x,y):
    """Translate the point based on the 'gravity' of the game, and x movement
    of the user"""
    
    new_points = [] 

    for pt in points:
#	print "old points", pt
	list_pt = list(pt)
	list_pt[0] += x 
	list_pt[1] += y
	new_points.append((list_pt[0],list_pt[1]))
	
#	print "new points: ", list_pt

    return new_points

if __name__ =='__main__':
    main()
