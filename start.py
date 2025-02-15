import sys

import pygame


class AlienInvasion:
    """Класс для управлиння ресурсами та повединкою гри"""

    def __init__(self):
        """Инициализуэ гру та створюе игрови ресурси"""
        pygame.init()

        self.creen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            #Видслидкування подий клавиатури та миши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Видображення останнього прорисованого украну
            pygame.display.flip()

if __name__ == '__main__':
    # Cndjhtyyz trptvgkzhe nf pfgecr uhb
    ai = AlienInvasion()
    ai.run_game()
