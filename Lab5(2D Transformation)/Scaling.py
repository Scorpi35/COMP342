#Scaling
import pygame
from OpenGL.GL import *
import time
from numpy import matmul
import numpy as np


def point(x1, y1, x2, y2, Sx, Sy):
    point_surface = pygame.Surface((1, 1))
    point_surface.fill((255, 0, 0))
    gameDisplay.blit(point_surface, (100, 100))
    
    #Scaling matrix
    S = [[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]


    x, y = x1, y1

    #Starting point matrix
    Ms = [x1, y1, 1]

    #Ending point matrix
    Me = [x2, y2, 1]

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        x = x + Xinc
        y = y + Yinc
        gameDisplay.blit(point_surface, (x, y))

    #Here scaling is done
    x11, y11, z11 = np.matmul(Ms, S)
    x22, y22, z22 = np.matmul(Me, S)

    dx = abs(x11 - x22)
    dy = abs(y11 - y22)

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    tx = 200
    ty = 200

    # The translation matrix
    Mt = [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    for num in range(0, Steps):
        x11 = x11 + Xinc
        y11 = y11 + Yinc
        l1 = [x11, y11, 1]
        xt1, yt1, zt1 = np.matmul(l1, Mt)
        gameDisplay.blit(point_surface, (xt1, yt1))




#This is the main fucntion
def main(x1, y1, x2, y2, Sx, Sy):

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        point(x1, y1, x2, y2, Sx, Sy)

        pygame.display.update()
        pygame.time.wait(10)

x1 = int(input('Enter x co-ordinate of starting point'))
y1 = int(input('Enter y co-ordinate of starting point'))
x2 = int(input('Enter x co-ordinate of ending point'))
y2 = int(input('Enter y co-ordinate of ending point'))
Sx = int(input('Enter scaling factor for x'))
Sy = int(input('Enter scaling factor for y'))

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Scaling')
main(x1, y1, x2, y2, Sx, Sy)
