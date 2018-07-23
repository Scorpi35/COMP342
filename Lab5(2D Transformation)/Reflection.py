#Reflection
import pygame
from OpenGL.GL import *
from numpy import matmul
import numpy as np

def reflection(x1, y1, x2, y2):
    point_surface = pygame.Surface((3, 3))
    point_surface.fill((255, 0, 0))

    #The reflection matrix along x-axis
    Rmx = [[1, 0, 0],
          [0, -1, 0],
          [0, 0, 1]]

    #Reflection matrix along y-axis
    Rmy = [[-1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if abs(dx) > abs(dy):
        Steps = abs(dx)
    else:
        Steps = abs(dy)

    Xinc = dx / Steps
    Yinc = dy / Steps

    for num in range(0, Steps):
        gameDisplay.blit(point_surface, (400 + x1, 400 - y1))
        Pm = [x1, y1, 1]
        x, y, z = np.matmul(Pm, Rmx)
        xy, yy, zz = np.matmul(Pm, Rmy)
        x1 = x1 + Xinc
        y1 = y1 + Yinc
        #Reflection along x-axis
        gameDisplay.blit(point_surface, (400 + x, 400 - y))

        #Reflection along y-axis
        gameDisplay.blit(point_surface, (400 + xy, 400 - yy))



#This is the main fucntion
def main(x1, y1, x2, y2):

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        reflection(x1, y1, x2, y2)

        pygame.display.update()
        pygame.time.wait(10)


x1 = int(input('Enter start x co-ordinate of a line'))
y1 = int(input('Enter start y co-ordinate of a line'))
x2 = int(input('Enter end x co-ordinate of a line'))
y2 = int(input('Enter end x co-ordinate of a line'))
pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Reflection')
main(x1, y1, x2, y2)
