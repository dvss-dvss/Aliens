import sys

import pygame as pg

from settings import Settings


class AlienInvasion:
    """Класс для управлиння ресурсами та повединкою гри"""

    def __init__(self):
        """Инициализуэ гру та створюе игрови ресурси"""
        pg.init()
        self.settings = Settings()

        self.creen = pg.display.set_mode((self.settings.creen_width, self.settings.creen_height))
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            #Видслидкування подий клавиатури та миши
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # За кожнойи интерацийи циклу оновлюэться екран
            self.creen.fill(self.settings.bg_color)

            # Видображення останнього прорисованого украну
            pg.display.flip()

if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
