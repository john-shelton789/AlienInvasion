import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0,0, 3, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - 20

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = (16, 12, 255)
        self.speed_factor = ai_settings.bullet_speed_factor

        # Play laser sound effect
        self.bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        self.bullet_sound.set_volume(0.1)
        self.bullet_sound.play()

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet2(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet2, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - 20

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class AlienBullet(Sprite):
    """A class to manage bullets fired from aliens"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet object at the alien's current position"""
        super(AlienBullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.top + 70

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # Play laser sound effect
        self.bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        self.bullet_sound.set_volume(0.1)
        self.bullet_sound.play()


    def update(self):
        """Move the bullet down the screen"""
        # Update the decimal position of the bullet.
        self.y += self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)