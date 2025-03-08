class Settings:
    """Класс для збригання всих налаштувань гри"""

    def __init__(self):
       #Параметри екрану
       self.creen_width = 1300
       self.creen_height = 700
       self.bg_color = (230, 230, 230)

       # Параметри корабля
       self.ship_speed = 5

       # Параметри снаряду
       self.bullet_speed = 3
       self.bullet_width = 3
       self.bullet_height = 15
       self.bullet_color = (60, 60, 60)
       self.bullets_allowed = 3

       # Параметри прибульців
       self.alien_speed = 1.0
       self.fleet_drop_speed = 10
       # fleet_direction = 1 якщо флот рухається праворуч, -1 якщо ліворуч
       self.fleet_direction = 1