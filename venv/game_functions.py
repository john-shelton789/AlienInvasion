import sys
from time import sleep
import pygame
import random
from bullet import Bullet, Bullet2, AlienBullet
from alien import GreenAlien, YellowAlien, RedAlien, BigBlueAlien
from explosion import Explosion, UFOExplosion
from bunker import Bunker
from high_scores import HighScores
from game_stats import GameStats


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (1 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number, images):
    """Create an alien and place it in a row"""
    alien = GreenAlien(ai_settings, screen, images)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.0 * alien.rect.height * row_number
    aliens.add(alien)

def create_yellow_alien(ai_settings, screen, aliens, alien_number, row_number, images):
    """Create an alien and place it in a row"""
    alien = YellowAlien(ai_settings, screen, images)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.2 * alien.rect.height * row_number
    aliens.add(alien)

def create_red_alien(ai_settings, screen, aliens, alien_number, row_number, images):
    """Create an alien and place it in a row"""
    alien = RedAlien(ai_settings, screen, images)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.2 * alien.rect.height * row_number
    aliens.add(alien)

def create_ufo(ai_settings, screen, aliens, images, stats, sb):
    """Create an alien and place it in a row"""
    alien = BigBlueAlien(ai_settings, screen, images, stats, sb)
    alien_width = alien.rect.width
    alien.x = 0
    alien.rect.x = alien.x
    alien.rect.y = 50
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens, images, bunkers, stats):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row
    alien = GreenAlien(ai_settings, screen, images)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    create_bunkers(ai_settings = ai_settings, screen = screen, bunkers = bunkers, images = images)

    # play bgm
    pygame.mixer.quit()
    pygame.mixer.init(44100 + (5000 * (stats.level - 1)))
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            if row_number == 0 or row_number == 1:
                create_alien(ai_settings = ai_settings, screen = screen, aliens = aliens, alien_number = alien_number, row_number = row_number, images = images)
            if row_number == 2 or row_number == 3:
                create_yellow_alien(ai_settings = ai_settings, screen = screen, aliens = aliens, alien_number = alien_number, row_number = row_number, images = images)
            if row_number == 4 or row_number == 5:
                create_red_alien(ai_settings = ai_settings, screen = screen, aliens = aliens, alien_number = alien_number, row_number = row_number, images = images)


def create_bunkers(ai_settings, screen, bunkers, images):
    """Create an alien and place it in a row"""
    for bunkernum in range(3):
        bunkerx = bunkernum * 300 + 300
        bunkery = 675
        bunker = Bunker(ai_settings, bunkerx, bunkery, screen, images)
        bunkers.add(bunker)

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, images, bunkers, high_scores_button, back_button):
    # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, play_button = play_button, ship = ship, aliens = aliens, bullets = bullets, mouse_x = mouse_x, mouse_y = mouse_y, images = images, bunkers = bunkers)
                check_high_scores_button(ai_settings = ai_settings, screen = screen, stats = stats, high_scores_button = high_scores_button, mouse_x = mouse_x, mouse_y = mouse_y)
                check_back_button(ai_settings = ai_settings, back_button = back_button, stats = stats, mouse_x = mouse_x, mouse_y = mouse_y)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        ship.is_firing = True
    if event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    new_bullet = Bullet(ai_settings, screen, ship)
    # new_bullet2 = Bullet2(ai_settings, screen, ship)
    bullets.add(new_bullet)
    # bullets.add(new_bullet2)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_SPACE:
        ship.is_firing = False

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y, images, bunkers):
    """Start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()



        # Create a new fleet and center the ship.
        create_fleet(ai_settings = ai_settings, screen = screen, ship = ship, aliens = aliens, images = images, bunkers = bunkers, stats = stats)
        # create_bunkers(ai_settings = ai_settings, screen = screen, bunkers = bunkers, images = images)
        ship.center_ship

def check_high_scores_button(ai_settings, screen, stats, high_scores_button, mouse_x, mouse_y):
    button_clicked = high_scores_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.scores_visible = True

def check_back_button(ai_settings, back_button, stats, mouse_x, mouse_y):
    button_clicked = back_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.scores_visible = False


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, images, explosions, bunkers):
    """Update position of bullets and get rid of old bullets"""
    time = pygame.time.get_ticks()
    if time % 100 == 0:
        if ship.is_firing:
            fire_bullet(ai_settings = ai_settings, screen = screen, ship = ship, bullets = bullets)

    bullets.update()



    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        if bullet.rect.top >= 800:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, ship = ship, aliens = aliens, bullets = bullets, images = images, explosions = explosions, bunkers = bunkers)
    check_bullet_bunker_collisions(ai_settings = ai_settings, screen = screen, bullets = bullets, bunkers = bunkers, images = images, explosions = explosions)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, images, explosions, bunkers):
    """Respond to bullet-alien collisions"""

    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    for collision in collisions:
        stats.score += collision.points
        sb.prep_score()
        check_high_score(stats=stats, sb=sb)

        if  collision.points == 50:
            explosion = Explosion(screen, collision.rect.centerx, collision.rect.centery, images)
            explosions.add(explosion)
        elif  collision.points == 100:
            explosion = Explosion(screen, collision.rect.centerx, collision.rect.centery, images)
            explosions.add(explosion)
        elif  collision.points == 150:
            explosion = Explosion(screen, collision.rect.centerx, collision.rect.centery, images)
            explosions.add(explosion)
        else:
            ufopoints = UFOExplosion(screen, collision.rect.centerx, collision.rect.centery, collision.points)
            explosions.add(ufopoints)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings = ai_settings, screen = screen, ship = ship, aliens = aliens, images = images, bunkers = bunkers, stats = stats)

def check_bullet_bunker_collisions(ai_settings, screen, bullets, bunkers, images, explosions):
    """Respond to bullet-alien collisions"""

    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, bunkers, True, True)

    for collision in collisions:

        explosion = Explosion(screen, collision.rect.centerx, collision.rect.centery, images)
        explosions.add(explosion)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings = ai_settings, aliens = aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, images, bunkers, explosions):
    """Respond to ship being hit by an alien"""
    explosion = Explosion(screen, ship.rect.centerx, ship.rect.centery, images)
    explosions.add(explosion)

    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings = ai_settings, screen = screen, ship = ship, aliens = aliens, images = images, bunkers = bunkers, stats = stats)
        ship.center_ship()

        # Pause.
        sleep(0.5)
    else:

        high_score_int = int(round(stats.high_score, -1))
        high_score_str = str(high_score_int)
        high_scores = open("images/high_scores.txt", "a")
        pygame.mixer.quit()

        if not high_score_int == stats.high_score:
            high_scores.write(high_score_str)
            high_scores.write("\n")
            high_scores.close()


        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, images, explosions):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.left >= screen_rect.right:
            aliens.remove(alien)
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, ship = ship, aliens = aliens, bullets = bullets, images = images, explosions = explosions)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, images, bunkers, explosions):
    """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    alien_number = 1
    for alien in aliens:
        randnum = random.randint(1, 1001)
        alien_number += 1
        if alien_number > len(aliens) - 8:
            if randnum <= 1:
                new_bullet = AlienBullet(ai_settings, screen, alien)
                bullets.add(new_bullet)

    # spawn a UFO randomly
    randufo = random.randint(1, 8000)
    if randufo == 1:
        create_ufo(ai_settings = ai_settings, screen = screen, aliens = aliens, images = images, stats = stats, sb = sb)

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, ship = ship, aliens = aliens, bullets = bullets, images = images, bunkers = bunkers, explosions = explosions)

    # Look for bullet collisions
    if pygame.sprite.spritecollideany(ship, bullets):
        ship_hit(ai_settings = ai_settings, screen = screen, stats = stats, sb = sb, ship = ship, aliens = aliens, bullets = bullets, images = images, bunkers = bunkers, explosions = explosions)


    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings=ai_settings, screen=screen, stats=stats, sb=sb, ship=ship, aliens=aliens, bullets=bullets, images = images, explosions = explosions)



def update_screen(ai_settings, screen, stats, sb, ship, aliens, explosions, bullets, play_button, bunkers, images, high_scores, high_scores_button, back_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    explosions.update()
    explosions.draw(screen)
    bunkers.draw(screen)

    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        pygame.font.init()
        titlefont = pygame.font.SysFont(None, 108)
        pointsfont = pygame.font.SysFont(None, 32)
        titleline1 = titlefont.render('SPACE', False, (255, 255, 255))
        titleline2 = titlefont.render('INVADERS', False, (78, 244, 66))
        greensurface = pointsfont.render('= 150', False, (78, 244, 66))
        yellowsurface = pointsfont.render('= 100', False, (78, 244, 66))
        redsurface = pointsfont.render('= 50', False, (78, 244, 66))
        bluesurface = pointsfont.render('= ???', False, (78, 244, 66))

        # Paint the screen black
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1200, 800))


        #get images for all aliens for scoring info
        greenImage = images[14]
        yellowImage = images[23]
        redImage = images[16]
        blueImage = images[0]

        #if not looking at the high scores menu, show the main menu
        if not stats.scores_visible:
            screen.blit(greenImage, (250, 500))
            screen.blit(yellowImage, (550, 500))
            screen.blit(redImage, (850, 500))
            screen.blit(blueImage, (550, 650))
            #blit the title
            screen.blit(titleline1, (470,100))
            screen.blit(titleline2, (410,200))
            #blit the alien points
            screen.blit(greensurface, (320, 532))
            screen.blit(yellowsurface, (620, 532))
            screen.blit(redsurface, (920, 532))
            screen.blit(bluesurface, (620, 672))
            #draw the buttons
            high_scores_button.draw_button()
            play_button.draw_button()

        if stats.scores_visible:
            high_scores1 = HighScores(screen)
            high_scores1.show_score()
            back_button.draw_button()




    # Make the most recently drawn screen visible.
    pygame.display.flip()

