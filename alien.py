import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс для прибульця"""

    def __init__(self, ai_game):
        """Инициалицуе прибульця та задае його позицию"""
        super().__init__()
        self.creen = ai_game.creen
        self.settings = ai_game.settings

        # Завантаження зображення та вызначення rect
        self.image = pg.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Кошен новий прибулець з'являеться в ливому верхньому кути екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Збереження точної горизонтальної позиції прибульця
        self.x = float(self.rect.x)

    def chek_edges(self):
        """Повертає True, якщо прибулець біля краю екрана"""
        creen_rect = self.creen.get_rect()
        if self.rect.right >= creen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        """Переміщує прибульця праворуч"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
