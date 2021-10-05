import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx       #Положение корабля по центру
        self.rect.bottom = self.screen_rect.bottom      #Корабль в нижней части экрана
        self.center = float(self.rect.centerx)
        self.moving_right = False                       #Флаги передвижения
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # self.rect.centery = self.screen_rect.bottom - 15
        # self.centery = float(self.rect.centery)


    def blitme(self):
        """Отрисовка корабля на экране"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Управляет положением корабля на экране"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor

        # if self.moving_up and self.rect.top > 0:
        #     self.centery -= self.ai_settings.ship_speed_factor
        # if self.moving_down and self.rect.bottom  < self.screen_rect.bottom:
        #     self.centery += self.ai_settings.ship_speed_factor


        # self.rect.centery = self.centery
        self.rect.centerx = self.center
