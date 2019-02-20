import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
import explosion
import spritesheet
import game_functions as gf
from high_scores import HighScores


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.pre_init(44100)
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    screen_rect = screen.get_rect()


    menuRect = pygame.Rect(0, 0, ai_settings.screen_width, ai_settings.screen_height)

    # Show buttons
    play_button = Button(ai_settings, screen, "Play", (600, 400))
    high_scores_button = Button(ai_settings, screen, "High Scores", (screen_rect.centerx, 460))
    back_button = Button(ai_settings, screen, "Back", (screen_rect.centerx, 700))
    # Open the high scores list
    high_scoresfile = open("images/high_scores.txt", "r")


    # Load the alien image and set its rect attribute
    spriteframes = spritesheet.spritesheet("images/SpaceInvadersSprites.png")
    # Indexes for everything: UFO: 0-1, explosion: 2-13, green alien: 14-15, red alien: 16-17, shield: 18, ship: 19-22, yellow alien: 23-24
    images = spriteframes.images_at([(0, 0, 64, 64), (0, 64, 64, 64), (0, 128, 64, 64), (0, 192, 64, 64), (0, 256, 64, 64), (0, 320, 64, 64), (0, 384, 64, 64), (0, 448, 64, 64), (0, 512, 64, 64), (0, 576, 64, 64), (0, 640, 64, 64), (0, 704, 64, 64), (0, 768, 64, 64), (0, 832, 64, 64), (0, 896, 64, 64), (0, 960, 64, 64), (0, 1024, 64, 64), (0, 1088, 64, 64), (0, 1152, 64, 32), (0, 1184, 64, 64), (0, 1248, 64, 64), (0, 1312, 64, 64), (0, 1376,  64, 64), (0, 1440, 64, 64), (0, 1504, 64, 64)], colorkey=(0, 0, 0))

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, images)
    high_scores = HighScores(screen)

    # Set the background color.
    bg_color = (230, 230, 230)





    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen, images)
    bullets = Group()
    alienbullets = Group()
    aliens = Group()
    explosions = Group()
    bunkers = Group()

    # Create the fleet of aliens.
    # gf.create_fleet(ai_settings = ai_settings, screen = screen, ship = ship, aliens = aliens, images = images, bunkers = bunkers, level = level)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, play_button = play_button, ship = ship, aliens = aliens, bullets = bullets, images = images, bunkers = bunkers, high_scores_button = high_scores_button, back_button = back_button)




        if stats.game_active:
            # current_frame = current_frame + 1
            ship.update()
            gf.update_bullets(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, ship = ship, aliens = aliens, bullets = bullets, images = images, explosions = explosions, bunkers = bunkers)
            gf.update_aliens(ai_settings = ai_settings, stats = stats, sb = sb, screen = screen, ship = ship, aliens = aliens, bullets = bullets, images = images, bunkers = bunkers, explosions = explosions)

        gf.update_screen(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, ship = ship, aliens = aliens, bullets = bullets, play_button = play_button, explosions = explosions, bunkers = bunkers, images = images, high_scores = high_scores, high_scores_button = high_scores_button, back_button = back_button)


run_game()
