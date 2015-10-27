#! usr/bin/python

import pygame, sys

from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)

pygame.display.set_caption('Drawing')

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
ORANGE = (200,100,0)
PURPLE = (100,0,200)
RAND = (100,50,20)

LEN = 20
X = 100
Y = 100

# draw on the surface object
DISPLAYSURF.fill(WHITE)
#T piece
pygame.draw.polygon(DISPLAYSURF, GREEN, ((X, Y), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN,Y + 2*LEN),
					 (X + 2*LEN, Y + 2*LEN), (X + 2*LEN, Y + LEN), (X + LEN,Y + LEN), (X + LEN,Y)) )
#L piece
pygame.draw.polygon(DISPLAYSURF, BLUE, ((2*X, Y), (2*X, Y + 3*LEN), (2*X + LEN, Y + 3*LEN),
					(2*X + LEN,Y + LEN), (2*X + 2*LEN,Y+LEN), (2*X+2*LEN,Y))) 
#back L piece
pygame.draw.polygon(DISPLAYSURF, RAND, ((4*X, 3*Y), (4*X, 3*Y + 3*LEN), (4*X - LEN, 3*Y + 3*LEN),
					(4*X - LEN,3*Y + LEN), (4*X - 2*LEN,3*Y+LEN), (4*X-2*LEN,3*Y))) 
#| piece
pygame.draw.polygon(DISPLAYSURF, BLACK, ((3*X, Y), (3*X, Y + 3*LEN), (3*X + LEN, Y + 3*LEN),
					(3*X + LEN,Y)) )
#square piece
pygame.draw.polygon(DISPLAYSURF, RED, ((4*X, Y), (4*X, Y + 2*LEN), (4*X + 2*LEN, Y + 2*LEN),
					(4*X + 2*LEN,Y)) )
#z piece
pygame.draw.polygon(DISPLAYSURF, ORANGE, ((X, 3*Y), (X, 3*Y + LEN), (X + LEN, 3*Y + LEN), (X + LEN,3*Y + 2*LEN),
					 (X + 3*LEN, 3*Y + 2*LEN), (X + 3*LEN, 3*Y + LEN), (X + 2*LEN,3*Y + LEN), 
					 (X + 2*LEN,3*Y)) )
#back z piece
pygame.draw.polygon(DISPLAYSURF, PURPLE, ((3*X, 3*Y), (3*X, 3*Y + LEN), (3*X - LEN, 3*Y + LEN), (3*X - LEN,3*Y + 2*LEN),
					 (3*X - 3*LEN, 3*Y + 2*LEN), (3*X - 3*LEN, 3*Y + LEN), (3*X - 2*LEN,3*Y + LEN), 
					 (3*X - 2*LEN,3*Y)) )


def rotatePoint(centerPoint,point):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(90)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

#rect1 = pygame.Rect(200, 150, 20, 50)
#rect2 = pygame.Rect(202, 100, 100, 50)
#rect3 = rect1.union(rect2)
#pygame.draw.rect(DISPLAYSURF,GREEN, rect3, 1)

while True: # main game loop
    for event in pygame.event.get():
	if event.type == QUIT:
	    pygame.quit()
	    sys.exit()
    pygame.display.update()

#sys.stdin.readlines()
