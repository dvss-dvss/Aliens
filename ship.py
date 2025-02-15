import pygame as pg


class Ship:
    """Класс для управлиння кораблем"""

    def __init__(self, ai_game):
        """Инициализуэ корабель та встановлюе його початкову позицию"""
        self.creen = ai_game.creen
        self.creen_rect = ai_game.creen.get_rect()

        # Завантаження зобравження корабля и отримання поверхни
        self.image = pg.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являэться в нижний чатсини екрану
        self.rect.midbottom = self.creen_rect.midbottom

        # Флаг перемищення
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисуэ корабель в поточний позицийи"""
        self.creen.blit(self.image, self.rect)
    
    def update(self):
        """Оновлюэ позицию корабля з урахування флагу"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1