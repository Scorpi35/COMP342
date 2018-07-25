#Rotation
import pygame
from OpenGL.GL import *
import time
from numpy import matmul
import numpy as np
import math as math
from math import pi


def rotation(x1, y1, x2, y2, R):
    point_surface = pygame.Surface((1, 1))
    point_surface.fill((255, 0, 0))
    gameDisplay.blit(point_surface, (400, 400))

    #Radian value of given angle
    radian = (pi/180) * R

    #Rotation matrix
    Rm = [[math.cos(radian), math.sin(radian), 0],
          [-(math.sin(radian)), math.cos(radian), 0],
          [0, 0, 1]]

    x, y = x1, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))
        lmatrix = [x, y, 1]
        xr, yr, zr = np.matmul(lmatrix, Rm)
        x = x + Xinc
        y = y + Yinc
        gameDisplay.blit(point_surface, (400 + xr, 400 - yr))



#This is the main fucntion
def main(x1, y1, x2, y2, R):

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        rotation(x1, y1, x2, y2, R)

        pygame.display.update()
        pygame.time.wait(10)


x1 = int(input('Enter x co-ordinate of starting point'))
y1 = int(input('Enter y co-ordinate of starting point'))
x2 = int(input('Enter x co-ordinate of ending point'))
y2 = int(input('Enter y co-ordinate of ending point'))
R = int(input('Enter angle for rotation'))

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Rotation')
main(x1, y1, x2, y2, R)
