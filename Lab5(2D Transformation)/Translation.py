# Implementation of translation
import pygame
from OpenGL.GL import *
from numpy import matmul
import numpy as np


# Function for translation
def translation():
    point_surface = pygame.Surface((1, 1))
    point_surface.fill((255, 0, 0))

    tx = 200
    ty = 200

    # The translation matrix
    Mt = [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    result = [[0], [0], [0]]

    #The points of a triangle
    x1, y1, z1 = [200, 100, 1]
    x2, y2, z2 = [300, 200, 1]
    x3, y3, z3 = [100, 200, 1]


    dx1 = x2 - x1
    dy1 = y2 - y1

    if abs(dx1) > abs(dy1):
        Steps = abs(dx1)
    else:
        Steps = abs(dy1)

    Xinc = dx1 / Steps
    Yinc = dy1 / Steps

    for num in range(0, Steps):
        x1 = x1 + Xinc
        y1 = y1 + Yinc
        gameDisplay.blit(point_surface, (x1, y1))
        l1 = x1, y1, z1 = [x1, y1, 1]
        xt1, yt1, zt1 = np.matmul(l1, Mt)
        gameDisplay.blit(point_surface, (xt1, yt1))

    x1, y1, z1 = (200, 100, 1)
    x2, y2, z2 = (300, 200, 1)
    x3, y3, z3 = (100, 200, 1)

    #Another line
    dx2 = -x1 + x3
    dy2 = -y1 + y3

    if abs(dx2) > abs(dy2):
        Steps = abs(dx2)
    else:
        Steps = abs(dy2)

    Xinc = dx2 / Steps
    Yinc = dy2 / Steps

    for num in range(0, Steps):
        x1 = x1 + Xinc
        y1 = y1 + Yinc
        gameDisplay.blit(point_surface, (x1, y1))
        l2 = x1, y1, z1 = [x1, y1, 1]
        xt2, yt2, zt2 = np.matmul(l2, Mt)
        gameDisplay.blit(point_surface, (xt2, yt2))

    x1, y1, z1 = (200, 100, 1)
    x2, y2, z2 = (300, 200, 1)
    x3, y3, z3 = (100, 200, 1)

    #Another line
    dx3 = x2 - x3
    dy3 = y2 - y3

    if abs(dx3) > abs(dy3):
        Steps = abs(dx3)
    else:
        Steps = abs(dy3)

    Xinc = dx3 / Steps
    Yinc = dy3 / Steps

    for num in range(0, Steps):
        x3 = x3 + Xinc
        y3 = y3 + Yinc
        gameDisplay.blit(point_surface, (x3, y3))
        l3 = x1, y1, z1 = [x3, y3, 1]
        xt3, yt3, zt3 = np.matmul(l3, Mt)
        gameDisplay.blit(point_surface, (xt3, yt3))




# this is the main function
def main():
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        translation()
        pygame.display.update()
        pygame.time.wait(10)


pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Example of translation')
main()
