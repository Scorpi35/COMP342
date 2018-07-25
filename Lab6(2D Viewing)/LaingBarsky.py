import pygame

pygame.init()

xwmin = int(input('Enter starting x co-ordinate of clipping window'))
ywmin = int(input('Enter starting y co-ordinate of clipping window'))
xwmax = int(input('Enter ending x co-ordinate of a clipping window'))
ywmax = int(input('Enter ending y co-ordinate of a clipping window'))

x1 = int(input('Enter starting x co-ordinate of a line'))
y1 = int(input('Enter starting y co-ordinate of a line'))
x2 = int(input('Enter ending x co-ordinate of a line'))
y2 = int(input('Enter ending y co-ordinate of a line'))

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Illustration of Liang Barsky")

white = (255, 255, 255)
black = (0, 0, 0)

window.fill(white)


pygame.draw.polygon(window, black, ((400 + xwmin, 400 - ywmin),
                                    (400 + xwmax, 400 - ywmin),
                                    (400 + xwmax, 400 - ywmax),
                                    (400 + xwmin, 400 - ywmax)), 1)

pygame.draw.line(window, black, (x1, y1), (x2, y2), 1)

dx = x2 - x1
dy = y2 - y1

P1 = -dx
P2 = dx
P3 = -dy
P4 = dy

q1 = x1 - xwmin
q2 = xwmax - x1
q3 = y1 - ywmin
q4 = ywmax - y1

r1 = q1 / P1
r2 = q2 / P2
r3 = q3 / P3
r4 = q4 / P4

a = []
b = []
if P1 < 0:
    a.append(r1)
else:
    b.append(r1)
if P2 < 0:
    a.append(r2)
else:
    b.append(r2)
if P3 < 0:
    a.append(r3)
else:
    b.append(r3)
if P4 < 0:
    a.append(r4)
else:
    b.append(r4)

u1 = max(0, max(a))
u2 = min(1, min(b))

if u1 > u2:
    pass
else:
    x11 = x1 + (u1 * dx)
    y11 = y1 + (u1 * dy)
    x21 = x1 + (u2 * dx)
    y21 = y1 + (u2 * dy)

pygame.display.update()
window.fill(white)
pygame.draw.polygon(window, black, ((400 + xwmin, 400 - ywmin),
                                    (400 + xwmax, 400 - ywmin),
                                    (400 + xwmax, 400 - ywmax),
                                    (400 + xwmin, 400 - ywmax)), 1)
pygame.draw.line(window, black, (400 + x11, 400 - y11), (400 + x21, 400 - y21), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
