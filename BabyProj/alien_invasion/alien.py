import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        """Init the alien"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
