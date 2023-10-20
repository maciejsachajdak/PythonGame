import math
import os

import pygame
from pygame import mixer

from towers.tower import Tower, menu_background, upgrade_button, sell_button, back_button, next_button
from menu.Menu import Menu

pygame.mixer.init()
sound = mixer.Sound("music/hit.wav")


def load_image_tower(start, end, number):
    tower_images = []

    for x in range(start, end):
        tower_images.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/archerTower" + str(number) + "/tower", str(x)) + ".png"),
            (90, 90)))

    return tower_images


def load_image_archer(start, end, number):
    archer_images = []

    for x in range(start, end):
        archer_images.append(
            pygame.image.load(os.path.join("game_assets/archerTower" + str(number) + "/archer", str(x)) + ".png"))

    return archer_images


class ArcherTowerLong(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = load_image_tower(7, 10, 1)[:]
        self.archer_images = load_image_archer(64, 70, 1)[:]
        self.archer_count = 0
        self.range = 150
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage
        self.width = self.height = self.tower_images[0].get_width()
        self.price = [2000, 3000, "MAX"]
        self.sell_price = [500, 1000, 1500]
        self.name = "archer1"
        self.attacked_enemy = None
        self.support_by_star_farm = False
        self.add_money = 0

        self.menu = Menu(self, self.x, self.y, menu_background, self.price, self.sell_price)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.menu.add_button(sell_button, "Sell")
        self.menu.add_button(back_button, "back")
        self.menu.add_button(next_button, "next")

    def draw(self, window):
        super().draw_range(window)
        super().draw(window)

        archer = self.archer_images[self.archer_count // 3]

        if self.left:
            add = -25
        else:
            add = - archer.get_width() / 2 - 5
        window.blit(archer, (self.x + add, self.y - archer.get_height() - 25))

    def attack(self, enemies, sound_on):
        """
        atakuje wrogow z listy i ja modyfikuje (usuwanie)
        :param enemies: list od enemies
        :return: None
        """
        money = 0
        monster_beat = 0

        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 3:
                self.archer_count = 0
        else:
            self.archer_count = 0

        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if distance < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        if len(enemy_closest) > 0:
            if self.menu.counter < 2:
                enemy_closest.sort(key=lambda en: en.x)
                if self.menu.counter == 0:
                    self.attacked_enemy = enemy_closest[len(enemy_closest) - 1]
                elif self.menu.counter == 1:
                    self.attacked_enemy = enemy_closest[0]
            else:
                enemy_closest.sort(key=lambda en: en.health)
                self.attacked_enemy = enemy_closest[len(enemy_closest) - 1]
            if self.archer_count == 6:
                if self.attacked_enemy.hit(self.damage):
                    monster_beat += 1
                    if sound_on:
                        sound.play()
                    if self.support_by_star_farm:
                        money = self.attacked_enemy.money + self.add_money
                    else:
                        money = self.attacked_enemy.money
                    enemies.remove(self.attacked_enemy)

            if self.attacked_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
            elif self.attacked_enemy.x < self.x and self.left:
                self.left = False
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)

        return money, monster_beat


class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = load_image_tower(10, 13, 2)[:]
        self.archer_images = load_image_archer(51, 57, 2)[:]
        self.archer_count = 0
        self.range = 100
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 3
        self.original_damage = self.damage
        self.width = self.height = self.tower_images[0].get_width()
        self.price = [2500, 4000, "MAX"]
        self.sell_price = [750, 1250, 2000]
        self.name = "archer2"

        self.menu = Menu(self, self.x, self.y, menu_background, self.price, self.sell_price)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.menu.add_button(sell_button, "Sell")
        self.menu.add_button(back_button, "back")
        self.menu.add_button(next_button, "next")
