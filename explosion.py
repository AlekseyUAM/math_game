import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):

    def __init__(self, screen):
        super(Explosion, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/exp1_6.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 20
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        self.screen.blit(self.image, self.rect)
