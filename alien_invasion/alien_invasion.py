import pygame

from settings import Settings

from ship import Ship

import game_func as gf

from pygame.sprite import Group


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(('Alien Invasion'))
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ship, ai_settings, screen, bullets)

        ship.update()

        bullets.update()

        gf.update_screen(ai_settings, screen, ship, bullets)



run_game()