import sys

import pygame as pg

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управлиння ресурсами та повединкою гри"""

    def __init__(self):
        """Инициализуэ гру та створюе игрови ресурси"""
        pg.init()
        self.settings = Settings()

        self.creen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.creen_width = self.creen.get_rect().width
        self.settings.creen_height = self.creen.get_rect().height
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

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

    def _change_fleet_direction(self):
        """Опускае весь флот та звинюе напрям руху"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """Реагуе на досягненя прибульця краю екрана"""
        for alien in self.aliens.sprites():
            if alien.chek_edges():
                self._change_fleet_direction()
                break

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
                # Перемищуэмо корабель праворуч
                self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pg.K_ESCAPE:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Створюе флот прибульцив"""
        # Створення прибульця и вызначення килькости прибульцив в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.creen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)
 
        # Визначення кількості рядів
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.creen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)
 
        # Створення флоту прибульців
        for row_number in range(number_rows):
            # Створення ряду прибульців
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _fire_bullet(self):
        """Створюе новий снаряд та додаэ його до групи"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        """Оновлює позиції всіх прибульців флоту"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_bullets(self):
        """Оновлює позиції снарядів"""
        self.bullets.update()
        #print(len(self.bullets))

        # Видалення снарядів, що вилетіли за край екрану
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)             

    def _update_screen(self):
        """Оновлюэ зображення на екрани та видображаэ новий екран"""
        self.creen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.creen)

        # Відображення останнього прорисованого екрану
        pg.display.flip()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            #Видслидкування подий клавиатури та миши
            self._chek_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
