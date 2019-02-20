import pygame
from pygame.sprite import Sprite
import spritesheet

class Explosion(Sprite):

    def __init__(self, screen, x_coord, y_coord, images):
        """Initialize the ship and set its starting position"""
        super(Explosion, self).__init__()
        self.screen = screen

        # Load the explosion image and get its rect.
        self.images = images
        self.image = self.images[2]
        self.aindex = 2
        self.framecounter = 0
        self.framelimit = 30

        # Play explosion sound
        self.explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
        self.explosion_sound.set_volume(0.1)
        self.explosion_sound.play()


        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each explosion wherever the alien that died is
        self.rect.centerx = x_coord
        self.rect.centery = y_coord

    def update(self):
        """Move the explosion along, then delete it when it gets to the end"""
        self.framecounter = self.framecounter + 1

        if self.framecounter >= self.framelimit:
            self.framecounter = 0
            if self.aindex == 2:
                self.image = self.images[3]
                self.aindex = 3
            elif self.aindex == 3:
                self.image = self.images[4]
                self.aindex = 4
            elif self.aindex == 4:
                self.image = self.images[5]
                self.aindex = 5
            elif self.aindex == 5:
                self.image = self.images[6]
                self.aindex = 6
            elif self.aindex == 6:
                self.image = self.images[7]
                self.aindex = 7
            elif self.aindex == 7:
                self.image = self.images[8]
                self.aindex = 8
            elif self.aindex == 8:
                self.image = self.images[9]
                self.aindex = 9
            elif self.aindex == 9:
                self.image = self.images[10]
                self.aindex = 10
            elif self.aindex == 10:
                self.image = self.images[11]
                self.aindex = 11
            elif self.aindex == 11:
                self.image = self.images[12]
                self.aindex = 12
            elif self.aindex == 12:
                self.image = self.images[13]
                self.aindex = 13
            elif self.aindex == 13:
                self.kill()

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


class UFOExplosion(Sprite):

    def __init__(self, screen, x_coord, y_coord, points):
        super(UFOExplosion, self).__init__()

        # Show text when a UFO explodes
        self.screen = screen
        self.x = x_coord
        self.y = y_coord
        self.points = points
        self.framecount = 0
        self.font = pygame.font.SysFont(None, 32)
        self.ufo_point_display = self.font.render(str(self.points), False, (255, 255, 255))

        self.image = self.ufo_point_display
        self.rect = self.image.get_rect()
        # Display the text where the UFO exploded
        self.rect.centerx = x_coord
        self.rect.centery = y_coord

        # Set how long the text should display
        self.framecount = 0
        self.framelimit = 300

    def update(self):
        self.framecount += 1
        if self.framecount > self.framelimit:
            self.kill()


    def blitme(self):
        """Draw the UFO's Point number"""
        self.screen.blit(self.image, self.rect)
