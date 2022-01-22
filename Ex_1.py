import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    bg_color = (0,0,230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()
run_game()