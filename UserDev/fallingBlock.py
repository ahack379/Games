#! usr/bin/python

import pygame, sys
import random
import math
from pygame.locals import *
from Base.boardBase import BoardBase as board
import Base.color as c
import Base.shapesOriginal as s

import numpy as np

def main():

    global DISPLAYSURF, drawEveryTime,grid, border_color


    FPS = 20 # frames per second setting
    fpsClock = pygame.time.Clock()

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400,600),0,32)
    DISPLAYSURF.fill(c.BLACK)
    y_trans = 0 
    x_trans = 0

    enter = False
    right = False
    left  = False
    down  = False
    new   = True

    drawEveryTime = []

    grid = np.matrix( [[0]*20] * 29 )
    grid = np.vstack([grid,[1]*20])
    grid[:,0] = 2 
    grid[:,19] = 2

    border_color = c.DARKGRAY

    MOVE_Y = pygame.USEREVENT+1
    pygame.time.set_timer(MOVE_Y,500)

    while True: # main game loop

	move	     = False

	if new :
	    color, points_start, box_start = randomSelection()
	    new_points = points_start 
	    new_box  = box_start 
	    new = False

	for event in pygame.event.get():
	    
	    keys = pygame.key.get_pressed()

	    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
		pygame.quit()
		sys.exit()
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
	    new_box = rotatePoint(box_start[1],new_box)
	    new_points = rotatePoint(box_start[1],new_points)

	    fallingPiece(color,new_points,new_box,drawEveryTime) 
	    pygame.display.update()
	    pygame.time.wait(140)

	if y_trans >= 700: 
	    pygame.quit()
	    print "********\nquitting now"
	    sys.exit()
	    
	maxMinArray = maxMinXY(new_box)

	if right or left or down or move:
	    if right and maxMinArray[1] < 360:
		x_trans += 20
		print "right"
	    elif left and maxMinArray[0] > 40:
		x_trans -= 20
		print "lefT"
	    elif down and maxMinArray[3] < 540 :
		print "down"
		y_trans += 40
	    elif move :
		y_trans += 20; 

	    new_points, new_box, hit = translatePoint(new_points,new_box,x_trans,y_trans)
	    
	    if hit:
		drawEveryTime.append((color,new_points))
		new = True

	    else:
#		if new_box != box_start:
#		    print grid
        	for b in new_box:
        	    grid[int(b[1]/20),int(b[0]/20)] = 2 

        	for b in box_start:
		    
        	    if b not in new_box:
        	        grid[int(b[1]/20),int(b[0]/20)] = 0
			box_start = new_box

	    fallingPiece(color,new_points,new_box,drawEveryTime) 
	    pygame.display.update()
	    pygame.time.wait(140)
	    pygame.display.set_mode((400,600),0,32)
	    y_trans = 0
	    x_trans = 0



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

    return min_x, max_x, min_y, max_y

def fallingPiece(color,points,box,drawEveryTime):

    DISPLAYSURF.fill(c.BLACK)

    if len(points) == 8:
      pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7]))
      pygame.draw.polygon(DISPLAYSURF,border_color,(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7]),1 )
   #   pygame.draw.polygon(DISPLAYSURF,c.ORANGE,(box[0],box[1],box[2],box[3]),1 )
    elif len(points) == 6:
      pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3],points[4],points[5]) )
      pygame.draw.polygon(DISPLAYSURF,border_color,(points[0],points[1],points[2],points[3],points[4],points[5]),1 )
    #  pygame.draw.polygon(DISPLAYSURF,color,(box[0],box[1],box[2],box[3]),1 )
    elif len(points) == 4: # and len(box) == 4:
      pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3]))
      pygame.draw.polygon(DISPLAYSURF,border_color,(points[0],points[1],points[2],points[3]),1 )
     # pygame.draw.polygon(DISPLAYSURF,color,(box[0],box[1],box[2],box[3]),1 )
 #   else:
#      pygame.draw.polygon(DISPLAYSURF,color,(points[0],points[1],points[2],points[3]),1 )
      #pygame.draw.polygon(DISPLAYSURF,color,(box[0],box[1],box[2]),1 )


    for pts in drawEveryTime:
	if len(pts[1]) == 8:
    	  pygame.draw.polygon(DISPLAYSURF,pts[0],(pts[1][0],pts[1][1],pts[1][2],pts[1][3],pts[1][4],pts[1][5],pts[1][6],pts[1][7]))
    	  pygame.draw.polygon(DISPLAYSURF,border_color,(pts[1][0],pts[1][1],pts[1][2],pts[1][3],pts[1][4],pts[1][5],pts[1][6],pts[1][7]),2)
    	elif len(pts[1]) == 6:
    	  pygame.draw.polygon(DISPLAYSURF,pts[0],(pts[1][0],pts[1][1],pts[1][2],pts[1][3],pts[1][4],pts[1][5]))
    	  pygame.draw.polygon(DISPLAYSURF,border_color,(pts[1][0],pts[1][1],pts[1][2],pts[1][3],pts[1][4],pts[1][5]),2)
    	elif len(pts[1]) == 4:
	  pygame.draw.polygon(DISPLAYSURF,pts[0],(pts[1][0],pts[1][1],pts[1][2],pts[1][3]))
	  pygame.draw.polygon(DISPLAYSURF,border_color,(pts[1][0],pts[1][1],pts[1][2],pts[1][3]),2)

def randomSelection():

    colors = [ c.MINT, c.GRAY,c.RED,c.GREEN,
               c.BLUE,c.ORANGE,c.PURPLE,c.YELLOW,c.RANDO ]
    
    shapes = [ s.T,s.L,s.L_back,s.I,s.Box,s.Z,s.Z_back ] 
    boxes  = [s.T_box,s.L_box,s.L_back_box,s.I_box,s.Box_box,s.Z_box,s.Z_back_box]

    r_colors = random.randint(0,len(colors)-1)
    r_shapes = random.randint(0,len(shapes)-1)

    return colors[r_colors], shapes[r_shapes], boxes[r_shapes]


def rotatePoint(centerPoint,points):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""

    angle = math.radians(90)
    new_points = []

    for p in points:
	p = list(p)
	temp_point = p[0]-centerPoint[0] , p[1]-centerPoint[1]
    	temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    	temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
	new_points.append(temp_point)

    return new_points 

def translatePoint(points,box,x,y):
    """Translate the point based on the 'gravity' of the game, and x movement
    of the user"""
    
    new_points = [] 
    new_box = [] 
    hit = False

    for pt in points:

	list_pt = list(pt)
	list_pt[0] += x 
	list_pt[1] += y
	new_points.append((list_pt[0],list_pt[1]))
 
    print "grid indices and grid:" 
    for b in box:

	list_b = list(b)
	list_b[0] += x 
	list_b[1] += y
	new_box.append((list_b[0],list_b[1]))

	print grid[int(list_b[1]/20),int(list_b[0]/20)], ", ", int(list_b[0]/20), int(list_b[1]/20)

	if ( grid[int(list_b[1]/20),int(list_b[0]/20)] == 1):

	    hit = True

    if hit == True:
	for b in box:
	    list_b = list(b)
	    grid[int(list_b[1]/20),int(list_b[0]/20)] = 1
	    print "grid indices: ", int(list_b[0]/20), int(list_b[1]/20)
	print grid
	return points, box, hit
	    
    else:
	return new_points, new_box, hit

if __name__ =='__main__':
    main()
