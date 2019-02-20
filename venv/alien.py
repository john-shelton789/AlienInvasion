import pygame
from pygame.sprite import Sprite
import spritesheet
import random
from game_stats import GameStats

class GreenAlien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, images):
        """Initialize the alien and set its starting position."""
        super(GreenAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.images = images
        # Load the alien image and set its rect attribute

        self.aindex = 14

        self.image = self.images[14]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

        # Store the current frame
        self.current_frame = 0
        self.animation_frames = 120
        self.points = 150

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.current_frame = self.current_frame + 1

        # Animate the alien, switching between two frames
        if self.current_frame > self.animation_frames:
            self.current_frame = 0
            if self.aindex == 14:
                self.image = self.images[15]
                self.aindex = 15
            elif self.aindex == 15:
                self.image = self.images[14]
                self.aindex = 14


    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

class YellowAlien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, images):
        """Initialize the alien and set its starting position."""
        super(YellowAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.images = images
        # Load the alien image and set its rect attribute

        self.aindex = 23

        self.image = self.images[23]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

        # Store the current frame
        self.current_frame = 0
        self.animation_frames = 120
        self.points = 100

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.current_frame = self.current_frame + 1

        # Animate the alien, switching between two frames
        if self.current_frame > self.animation_frames:
            self.current_frame = 0
            if self.aindex == 23:
                self.image = self.images[24]
                self.aindex = 24
            elif self.aindex == 24:
                self.image = self.images[23]
                self.aindex = 23


    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

class RedAlien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, images):
        """Initialize the alien and set its starting position."""
        super(RedAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.images = images
        # Load the alien image and set its rect attribute

        self.aindex = 16

        self.image = self.images[16]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

        # Store the current frame
        self.current_frame = 0
        self.animation_frames = 120
        self.points = 50

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.current_frame = self.current_frame + 1

        # Animate the alien, switching between two frames
        if self.current_frame > self.animation_frames:
            self.current_frame = 0
            if self.aindex == 16:
                self.image = self.images[17]
                self.aindex = 17
            elif self.aindex == 17:
                self.image = self.images[16]
                self.aindex = 16


    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

class BigBlueAlien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, images, stats, sb):
        """Initialize the alien and set its starting position."""
        super(BigBlueAlien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.images = images
        # Load the alien image and set its rect attribute

        self.aindex = 0

        self.image = self.images[0]

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

        # Store the current frame
        self.current_frame = 0
        self.animation_frames = 120
        self.points = random.randint(50, 1000)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return False
        elif self.rect.left <= 0:
            return False

    def update(self):
        """Move the alien right."""
        self.x += (2 *(self.ai_settings.alien_speed_factor))
        self.rect.x = self.x
        self.current_frame = self.current_frame + 1

        # Animate the alien, switching between two frames
        if self.current_frame > self.animation_frames:
            self.current_frame = 0
            if self.aindex == 0:
                self.image = self.images[1]
                self.aindex = 1
            elif self.aindex == 1:
                self.image = self.images[0]
                self.aindex = 0


    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

