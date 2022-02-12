import pygame
import sys
from pygame.locals import *

pygame.init()

color1 = (44, 31, 39)
color2 = (230, 0, 0)

size = width, height = 600, 600
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color1)
    
    pygame.draw.rect(screen, color2, (210, 210, 200, 200), 100)

    pygame.display.flip()

    clock.tick(10)