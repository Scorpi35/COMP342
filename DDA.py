#DDA line drawing algorithm
import pygame
from OpenGL.GL import *

def point():
    point_surface = pygame.Surface((1, 1))
    point_surface.fill((255, 0, 0))
    gameDisplay.blit(point_surface, (100, 100))

    x = 100
    y = 100

    dx = 300 - 100
    dy = 500 - 100

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
