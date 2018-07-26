#Bounce Ball
import pygame
from OpenGL.GL import *
from pygame import *

#This is the function for Bounce Ball

def BounceBall():

    total = 0
    height = 680
    width = 780

    animationTimer = time.Clock()

    x = 400
    y = 400
    # how fast in direction x
    dx = 10
    # how fast in direction y
    dy = 15
    endProgram = False

    while not endProgram:
        for e in event.get():
            if e.type == QUIT:
                endProgram = True

        # update position
        x += dx
        y += dy

        # border check
        if y < 20 or y > height - 100:
            dy *= -1
            total = total + 1
        if x < 20 or x > width - 100:
            dx *= -1
            total = total + 1

        if total == total_strikes:
            gameDisplay.fill((0, 0, 0))
            animationTimer.tick(100)
            pygame.display.update()
        else:
            gameDisplay.fill((0, 0, 0))
            rectangle()
            pygame.draw.ellipse(gameDisplay, (255, 255, 0), (x, y, 100, 100))
            # limit to 30 frames per second
            animationTimer.tick(100)
            # updating the screen
            pygame.display.update()

#This is the function for drawing rectangle
def rectangle():
    point_surface = pygame.Surface((1, 1))
    point_surface.fill((255, 0, 0))

    xs, ys = 10, 690
    xe, ye = 790, 10

    #line1
    x = xs
    y = ys

    dx = xe - xs
    dy = ys - ys

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

    #line2
    x = xe
    y = ys

    dx = xe - xe
    dy = ye - ys

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

    #line3
    x = xe
    y = ye

    dx = xs - xe
    dy = ye - ye

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

    #line4
    x = xs
    y = ye

    dx = xs - xs
    dy = ys - ye

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
def main(total_strikes):

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        rectangle()
        BounceBall()

        pygame.display.update()
        pygame.time.wait(10)


total_strikes = int(input('Enter total number of strikes:-'))

pygame.init()
gameDisplay = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Bounce Ball')
main(total_strikes)