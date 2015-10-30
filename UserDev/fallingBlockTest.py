#! usr/bin/python

import pygame, sys
import random
import math
from pygame.locals import *
from Base.boardBase import BoardBase as board
import Base.color as c
import Base.shapesTest as s


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
    drawEveryTime = []
    y_level = [380] * 21 
    

    MOVE_Y = pygame.USEREVENT+1
    pygame.time.set_timer(MOVE_Y,1100)
    DISPLAYSURF.fill(c.BLACK)

    # Goal: store upper y layer in order to stack blocks-- 
    # Note to self: How do we store block location, so we
    # can build blocks on top of one another? I suspect the
    # answer involves storing x,y iterative information based
    # on where blocks land.  Currently, storing y information
    # for each block individually. Need to also store x information.  
    # perhaps make pairs for each shape, corresponding to each side at
    # each y.


    while True: # main game loop
        clickFlag = 0 
        mouseClicked = False
	move	     = False

	if new :
	    color, points_start = randomSelection()
	    new = False
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

	if y_trans >= 500: 
	    pygame.quit()
	    print "quitting now"
	    sys.exit()
	    
	if move:
	    y_trans += 20; 

	trans_pts = translatePoint(new_points,x_trans,y_trans)
	maxMinArray = maxMinXY(trans_pts)
	
	if right or left or down:
	    if right and maxMinArray[2] < 460:
		x_trans += 20
	    elif left and maxMinArray[1] > 40:
		x_trans -= 20
	    elif down and maxMinArray[0] < 320 :
		y_trans += 40

#	print "x_trans is now, after trans : ", x_trans

	fallingPiece(color, trans_pts,drawEveryTime) 

	maxMinArray = maxMinXY(trans_pts)

	pygame.display.update()
	pygame.time.wait(100)

	y_move = -1 

	for p in trans_pts:
	    print "UGH: ", p[0], p[0]-40, (p[0]-40)/20
	    if( p[0] == maxMinArray[3] ):
		continue
	    if p[1] >= (y_level[int(p[0]-40)/20]-10):
		y_move = y_level[int(p[0]-40)/20]-10
		break 

	if y_move != -1:   
	    t = translatePoint(trans_pts,0,y_level[int(p[0]-40)/20] - p[1])

	    print "Here's how much we;re moving: ", y_level[int(p[0]-40)/20],  p[0], p[1]
#	if maxMinArray[0] >= 370: # or (maxMinArray[0] == 380 and down):
#	    if maxMinArray[0] >=340:
	    #t = translatePoint(trans_pts,0,380 - maxMinArray[0])
	    drawEveryTime.append((color,t))	
	    fallingPiece(color,t,drawEveryTime) 
	    pygame.display.update()
	    pygame.time.wait(300)

	    maxMinArray = maxMinXY(trans_pts)

            for p in t:
            #   print "Landed points: ", p

               if p[0] != maxMinArray[2]:
                   x = int(p[0] - 40 )/20 
                   print "Bin in x: ", x, p[1]
                   y_level[x] = p[1]  

	    print "New y level: ", y_level

	     #minX, -60 is min value
#	    x = int(maxMinArray[1] - 40)/20 
#	    y_level[x] -= (maxMinArray[0] - maxMinArray[3])


#	    pygame.display.set_mode((500,400),0,32)
	    y_trans = -50
	    x_trans = 0
	    new     = True


def maxMinXY(points):

    list(points)
    max_y = -100
    min_y = 500
    max_x = -100
    min_x = 500 
    for pt in points:
	if pt[0] > max_x:
	    max_x = pt[0]
	if pt[0] < min_x:
	    min_x = pt[0]
	if pt[1] > max_y:
	    max_y = pt[1]
	if pt[1] < min_y:
	    min_y = pt[1]

 #   print "what y are we returnign", max_y

    return max_y, min_x, max_x, min_y

def fallingPiece(color,points,drawEveryTime):

    DISPLAYSURF.fill(c.BLACK)

    if len(points) == 8:
      pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7]),1 )
    else:
      pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7],points[8],points[9]),1 )


    for pts in drawEveryTime:
#	print " inside drawEveryTIme" , len(pts[1])
	if len(pts[1]) == 8:
    	  pygame.draw.polygon(DISPLAYSURF,pts[0],(pts[1][0],pts[1][1],pts[1][2],pts[1][3],pts[1][4],pts[1][5],pts[1][6],pts[1][7]),3)
#	  print "Why are we not in here? "
	elif len(pts[1]) == 10: 
#	  print "Why are we not in here? "
    	  pygame.draw.polygon(DISPLAYSURF,pts[0],(pts[1][0],pts[1][1],pts[1][2],pts[1][3],pts[1][4],pts[1][5],pts[1][6],pts[1][7],pts[1][8],pts[1][9]),3)
	    

#    pygame.display.update()
    
    
def convertToBox(mouseX,mouseY):

    tempX = int(( mouseX - (START_X - BOX/2))/BOX)
    tempY = int(( mouseY - (START_Y - BOX/2))/BOX)
    return (tempX, tempY)
    

def randomSelection():

    colors = [ c.GRAY,c.WHITE,c.RED,c.GREEN,
               c.BLUE,c.ORANGE,c.PURPLE,c.YELLOW,c.RANDO ]
    
    shapes = [ s.T,s.L,s.L_back,s.I,s.Box,s.Z,s.Z_back ] 

    r_colors = random.randint(0,len(colors)-1)
    r_shapes = random.randint(0,len(shapes)-1)

    return colors[r_colors], shapes[4] #r_shapes]


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
	list_pt = list(pt)
	list_pt[0] += x 
	list_pt[1] += y
	new_points.append((list_pt[0],list_pt[1]))
	
    return new_points

if __name__ =='__main__':
    main()
