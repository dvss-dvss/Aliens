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
       self.bullet_speed = 1
       self.bullet_width = 3
       self.bullet_height = 15
       self.bullet_color = (60, 60, 60)
       