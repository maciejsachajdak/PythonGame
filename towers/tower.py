import math
import os

import pygame

from menu.Menu import Menu

menu_background = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "towerMenu.png")),
                                         (250, 100))
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "upgrade.png")), (50, 45))
sell_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "sell.png")), (50, 45))
back_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "back_button.png")), (30, 30))

next_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_right.png")), (30, 30))


class Tower:
    """
    Abstrakcyjna klasa wiezy
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.tower_images = []
        self.damage = 1
        self.range = None
        self.original_damage = self.damage
        self.original_range = self.range
        self.moving = False

        # menu ulepszenia i sprzedazy i przyciski
        self.menu = Menu(self, self.x, self.y, menu_background, self.price, self.sell_price)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.menu.add_button(sell_button, "Sell")

    def draw(self, window):
        img = self.tower_images[self.level - 1]
        window.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

        # draw menu
        if self.selected:
            self.menu.draw(window)

    def get_item_cost(self):
        return self.menu.get_item_cost()

    def draw_range(self, window):
        if self.selected:
            # rysowanko kolka z zasiegiem
            circle_surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            window.blit(circle_surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        """
        zwraca prawde jak sie kliknie w wieze
        :param X: int
        :param Y: int
        :return: bool
        """
        if self.x + self.width // 2 - 10 >= X >= self.x - self.width // 2:
            if self.y + self.height // 2 >= Y >= self.y - self.height // 2:
                return True
        return False

    def sell(self):
        """
        zwraca cene sprzedazy
        :return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        ulepszenie wiezy
        :return: None
        """
        if self.level < len(self.tower_images):
            self.level += 1
            self.damage += 1
            self.range += 20
            self.original_damage = self.damage

    def get_upgrade_cost(self):
        """
        zwraca koszt ulepszenia
        :return: int
         """
        return self.price[self.level - 1]

    def move(self, x, y):
        """
        przesuwa wieze na dany x i y
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()
