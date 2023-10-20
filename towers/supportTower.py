import math
import os

import pygame

from menu.Menu import Menu
from towers.tower import Tower, menu_background, upgrade_button, sell_button


def load_image_tower(start, end):
    tower_images = []

    for x in range(start, end):
        tower_images.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/supportTower/" + str(x) + ".png")),
            (90, 90)))

    return tower_images


class RangeTower(Tower):
    """
    Dodaje zasieg
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 90
        self.effect = [30, 60, 100]
        self.tower_images = load_image_tower(4, 7)[:]
        self.width = self.height = self.tower_images[0].get_width()
        self.price = [1500, 3000, "MAX"]
        self.sell_price = [250, 750, 1500]
        self.effected = []
        self.name = "support1"

        self.menu = Menu(self, self.x, self.y, menu_background, self.price, self.sell_price)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.menu.add_button(sell_button, "Sell")

    def draw(self, window):
        super().draw_range(window)
        super().draw(window)

    def support(self, towers):
        """
        dodawanie efektu do wiez w poblizu
        :param towers: list
        :return: None
        """
        for tower in towers:
            x = tower.x
            y = tower.y
            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if distance <= self.range + tower.width / 2:
                self.effected.append(tower)

        for tower in self.effected:
            tower.range = tower.original_range + self.effect[self.level - 1]


class DamageTower(RangeTower):
    """
    dodawanie obrazen wiezy
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_images = load_image_tower(7, 10)[:]
        self.effect = [1, 1.5, 2]
        self.price = [2000, 4000, "MAX"]
        self.sell_price = [375, 1000, 2000]
        self.name = "support2"

        self.menu = Menu(self, self.x, self.y, menu_background, self.price, self.sell_price)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.menu.add_button(sell_button, "Sell")

    def support(self, towers):
        """
        dodaje efekt do wiez w otoczneiu
        :param towers: list
        :return: None
        """
        for tower in towers:
            x = tower.x
            y = tower.y
            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if distance <= self.range + tower.width / 2:
                self.effected.append(tower)

        for tower in self.effected:
            tower.damage = tower.original_damage + self.effect[self.level - 1]


class StarFarm(DamageTower):
    """
    dodawanie kasy
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_images = load_image_tower(11, 13)[:]
        self.effect = [20, 40, 60]
        self.price = [3000, 5000, "MAX"]
        self.sell_price = [1000, 1500, 2500]
        self.name = "support3"
        self.range = 100

        self.menu = Menu(self, self.x, self.y, menu_background, self.price, self.sell_price)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.menu.add_button(sell_button, "Sell")

    def support(self, towers):
        for tower in towers:
            x = tower.x
            y = tower.y
            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if distance <= self.range + tower.width / 2:
                self.effected.append(tower)

        for tower in self.effected:
            tower.support_by_star_farm = True
            tower.add_money = self.effect[self.level - 1]
