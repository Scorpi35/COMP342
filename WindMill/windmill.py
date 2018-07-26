#Wind Mill using pygame
import pygame
from math import sin, cos, radians, pi
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 250, 0)

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Wind Mill")

window.fill(black)
pygame.draw.polygon(window, white, ((175, 380), (225, 380), (175, 175)))


def rotate(x, y, xr, yr, angle):
    A = [[cos(angle), -sin(angle), (xr * (1 - cos(angle))) + (yr * (sin(angle)))],
         [sin(angle), cos(angle), (yr * (1 - cos(angle))) - (xr * (sin(angle)))],
         [0, 0, 1]]

    B = [[x], [y], [1]]

    result = [[0], [0], [0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result[0][0], result[1][0]


a1, b1, a2, b2 = 200, 100, 280, 140
c1, d1, c2, d2 = 270, 220, 220, 265
e1, f1, e2, f2 = 130, 230, 115, 175

pygame.draw.polygon(window, red, ((200, 175), (a1, b1), (a2, b2)))
pygame.draw.polygon(window, red, ((200, 175), (c1, d1), (c2, d2)))
pygame.draw.polygon(window, red, ((200, 175), (e1, f1), (e2, f2)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    angle = radians(1)
    a1, b1 = rotate(a1, b1, 200, 175, angle)
    a2, b2 = rotate(a2, b2, 200, 175, angle)
    c1, d1 = rotate(c1, d1, 200, 175, angle)
    c2, d2 = rotate(c2, d2, 200, 175, angle)
    e1, f1 = rotate(e1, f1, 200, 175, angle)
    e2, f2 = rotate(e2, f2, 200, 175, angle)

    pygame.display.update()
    window.fill(black)
    pygame.draw.polygon(window, white, ((175, 420), (225, 420), (200, 175)))
    pygame.draw.polygon(window, red, ((200, 175), (a1, b1), (a2, b2)))
    pygame.draw.polygon(window, red, ((200, 175), (c1, d1), (c2, d2)))
    pygame.draw.polygon(window, red, ((200, 175), (e1, f1), (e2, f2)))
    pygame.display.update()

