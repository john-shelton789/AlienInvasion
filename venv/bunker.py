import pygame
from pygame.sprite import Sprite
import spritesheet

class Bunker(Sprite):

    def __init__(self, ai_settings, bunker_x, bunker_y, screen, images):
        """Initialize the ship and set its starting position"""
        super(Bunker, self).__init__()
        self.screen = screen
        self.images = images

        self.image = self.images[18]

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new bunker at the bottom of the screen
        self.rect.centerx = bunker_x
        self.rect.bottom = bunker_y

        # Store a decimal value for the ship's center.
        #self.center = float(self.rect.centerx)

        self.bunker_health = 5

    def update(self):
        """Track the HP of the bunker"""
        if self.bunker_health == 0:
            self.kill()

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


