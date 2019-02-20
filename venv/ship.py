import pygame
from pygame.sprite import Sprite
import spritesheet

class Ship(Sprite):

    def __init__(self, ai_settings, screen, images):
        """Initialize the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        # self.image = pygame.image.load('images/ship.bmp')

        self.images = images

        self.image = self.images[19]
        self.aindex = 19
        self.framecounter = 0
        self.framelimit = 60



        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

        # Firing flag.
        self.is_firing = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.framecounter = self.framecounter + 1


        if self.framecounter >= self.framelimit:
            self.framecounter = 0
            if self.aindex == 19:
                self.image = self.images[20]
                self.aindex = 20
            elif self.aindex == 20:
                self.image = self.images[21]
                self.aindex = 21
            elif self.aindex == 21:
                self.image = self.images[22]
                self.aindex = 22
            elif self.aindex == 22:
                self.image = self.images[19]
                self.aindex = 19

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
