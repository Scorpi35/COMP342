#Bresenham Line Drawing Algorithm
import pygame
from OpenGL.GL import *
import time


def point():
    point_surface = pygame.Surface((1, 1))
    point_surface.fill((255, 0, 0))
    gameDisplay.blit(point_surface, (100, 100))

    x1 = 100
    y1 = 100
    x2 = 300
    y2 = 500

    x, y = x1, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx < dy:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    #Initialization of initial discision parameter
    p = 2 * dy - dx

    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        # delay for 0.01 secs
        time.sleep(0.01)

        gameDisplay.blit(point_surface, (x, y))


#This is the main fucntion
def main():

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        point()

        pygame.display.update()
        pygame.time.wait(10)


pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bresenham Line Drawing Algo')
main()
