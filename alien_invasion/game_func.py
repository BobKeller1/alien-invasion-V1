import sys

import pygame

from bullet import Bullet

from pygame.sprite import Sprite, Group


def check_events(ship, ai_settings, bullets, screen):
    """События клавиатуры"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship, ai_settings, screen, bullets)

def check_key_down_events(event, ship, ai_settings, screen, bullets):
    """Обрабатывает нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)



def check_key_up_events(event, ship, ai_settings, screen, bullets):
    """Обрабатывает отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def fire_bullet(ai_settings,screen,ship,bullets):

    # if len(bullets) <= ai_settings.bullets_allowed:

        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
