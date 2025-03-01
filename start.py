import sys

import pygame as pg

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управлиння ресурсами та повединкою гри"""

    def __init__(self):
        """Инициализуэ гру та створюе игрови ресурси"""
        pg.init()
        self.settings = Settings()

        self.creen = pg.display.set_mode((self.settings.creen_width, self.settings.creen_height))
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _chek_events(self):
        """Обробляэ натиснення клавиш та подйи миши"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                    self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
                # Перемищуэмо корабель праворуч
                self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pg.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        """Оновлюэ зображення на екрани та видображаэ новий екран"""
        self.creen.fill(self.settings.bg_color)
        self.ship.blitme()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            #Видслидкування подий клавиатури та миши
            self._chek_events()
            self.ship.update()
            self._update_screen()

            # Видображення останнього прорисованого украну
            pg.display.flip()

if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
