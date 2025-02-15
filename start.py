import sys

import pygame as pg


class AlienInvasion:
    """Класс для управлиння ресурсами та повединкою гри"""

    def __init__(self):
        """Инициализуэ гру та створюе игрови ресурси"""
        pg.init()

        self.creen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Alien Invasion")

        # Призначення колиру фону
        self.bg_color = (230, 230, 230) # RGB

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            #Видслидкування подий клавиатури та миши
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # За кожнойи интерацийи циклу оновлюэться екран
            self.creen.fill(self.bg_color)

            # Видображення останнього прорисованого украну
            pg.display.flip()

if __name__ == '__main__':
    # Cndjhtyyz trptvgkzhe nf pfgecr uhb
    ai = AlienInvasion()
    ai.run_game()
