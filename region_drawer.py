# draws regions
import numpy as np
import pygame
pygame.init()
win = pygame.display.set_mode((800, 800))
zoom = 10
def inRegion(x, y):
    try:
        #if x + y >= 0 and x + y <= 4 and x <= y and y <= 3 * x: return True
        #if 0.5 * x <= y  and y <= x and 1 <= x * y and x * y <= 2: return True
        #if 0 <= x and x <= 2 and 0 <= y and y <= 1: return True
        if 1 <= y and y <= 4 and 1 <= x * y and x * y <= 4: return True
    except: pass
    return False

xs = np.linspace(-5, 5, 1000)
ys = np.linspace(-5, 5, 1000)

for x in xs:
    for y in ys:
        if inRegion(x, y): pygame.draw.circle(win, color=(25, 255, 255), center=(x * zoom + 400, -1 * y * zoom + 400), radius=1)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False