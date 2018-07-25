#Shearing
import pygame
from OpenGL.GL import *
import time
from numpy import matmul
import numpy as np
import math as math
from math import pi


def shearing(x1, y1, x2, y2, Sx, Sy):
    point_surface = pygame.Surface((2, 2))
    point_surface.fill((255, 0, 0))

    #Shearing matrix along x
    Shxm = [[1, 0, 0],
            [Sx, 1, 0],
            [0, 0, 1]]

    #Shearing matrix along y
    Shym = [[1, Sy, 0],
            [0, 1, 0],
            [0, 0, 1]]


    #Drawing line 1
    dx = x2 - x1
    dy = y1 - y1
    x = x1
    y = y1

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc


    #Drawing line 2
    dx = x2 - x2
    dy = y2 - y1
    x = x2
    y = y1

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc

    #Drawing line 3
    dx = x1 - x2
    dy = y2 - y2
    x = x2
    y = y2

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc


    #Drawing line 4
    dx = x1 - x1
    dy = y1 - y2
    x = x1
    y = y2

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc

    #After shearing
    #Along x
    xs1, sy1, sz1 = np.matmul([x2, y1, 1], Shxm)
    #Along y
    xs2, sy2, sz2 = np.matmul([x2, y2, 1], Shym)

    #Line 1
    dx = xs1 - x1
    dy = y1 - y1
    x = x1
    y = y1

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc

    #line 2
    dx = xs2 - xs2
    dy = sy2 - y1
    x = xs1
    y = y1

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc

    #lin3
    dx = x1 - xs1
    dy = sy2 - sy2
    x = xs1
    y = sy2

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc


    #line4
    dx = x1 - x1
    dy = y1 - sy2
    x = x1
    y = sy2

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        x = x + Xinc
        y = y + Yinc


#This is the main fucntion
def main(x1, y1, x2, y2, Sx, Sy):

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        shearing(x1, y1, x2, y2, Sx, Sy)

        pygame.display.update()
        pygame.time.wait(10)


x1 = int(input('Enter x co-ordinate of corner 1'))
y1 = int(input('Enter y co-ordinate of corner 1 '))
x2 = int(input('Enter x co-ordinate of corner 2'))
y2 = int(input('Enter y co-ordinate of corner 2'))
Sx = int(input('Enter shearing factor along x-axis'))
Sy = int(input('Enter Shearing factor along y-axis'))

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Shearing')
main(x1, y1, x2, y2, Sx, Sy)
