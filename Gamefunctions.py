import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)





def update_screen(ai_settings, screen, ship, aliens , bullets):
    # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
    # Make the most recently drawn screen visible.
        pygame.display.flip()

def check_keydown_events(event,ai_settings, screen, ship, bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            #Ek time per screen per sirf 5 bullets hongi, so u cant kill every alien

            if len(bullets) < ai_settings.bullets_allowed:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)

def check_keyup_events(event, ship):

        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_bullets(bullets):
  """Update position of bullets and get rid of old bullets."""
  # Update bullet positions.
  bullets.update()

  # Get rid of bullets that have disappeared.
  for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
          bullets.remove(bullet)


def get_number_aliens_x(ai_settings, alien_width):
 """Determine the number of aliens that fit in a row."""
 available_space_x = ai_settings.screen_width - alien_width
 number_aliens_x = int(available_space_x / (alien_width))
 return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
 """Create an alien and place it in the row."""
 alien = Alien(ai_settings, screen)
 alien_width = alien.rect.width
 alien.x = alien_width + alien_width * alien_number
 alien.rect.y = alien.rect.height +  alien.rect.height * row_number
 alien.rect.x = alien.x
 aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
  """Determine the number of rows of aliens that fit on the screen."""
  available_space_y = (ai_settings.screen_height -  alien_height - ship_height)
  number_rows = int(available_space_y / ( alien_height))
  return number_rows



def create_fleet(ai_settings, screen, ship,  aliens):
 """Create a full fleet of aliens."""
 # Create an alien and find the number of aliens in a row.
 alien = Alien(ai_settings, screen)
 number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
 number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
 # Create the first row of aliens.
 for row_number in range(number_rows):
   for alien_number in range(number_aliens_x):
     create_alien(ai_settings, screen, aliens, alien_number, row_number)