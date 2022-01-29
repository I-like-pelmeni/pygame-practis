import sys
import pygame

class Person:
    def __init__(self):

        self.image = pygame.image.load('images/khj.png')
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class BG:
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

