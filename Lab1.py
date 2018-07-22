import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (0, 0, -1),
    (0.3, 0, -1),
    (0, -1, -1),
    (0.3, -1, -1),
    (-1, -1, -1),
    (1, -1, -1),
    (-1, 1, -1),
    (1, 1, -1),
    (0.3, 1.5, -1),
    (-1.5, 1.5, -1),
    (-1.5, -0.7, -1),
    (-2, 1, -1),
    (-2, -0.8, -1),
    (-0.3, 0.3, -1),
    (-0.3, 0.7, -1),
    (-0.8, 0.3, -1),
    (-0.8, 0.7, -1),
    (0.3, 0.3, -1),
    (0.3, 0.7, -1),
    (0.8, 0.3, -1),
    (0.8, 0.7, -1)


)

edges = (
    (0, 1),
    (0, 2),
    (1, 3),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 6),
    (9, 11),
    (11, 12),
    (4, 12),
    (13, 14),
    (13, 15),
    (14, 16),
    (15, 16),
    (17, 18),
    (17, 19),
    (18, 20),
    (19, 20)

)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()


def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #it clears the frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()




