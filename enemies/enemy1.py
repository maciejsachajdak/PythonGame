import pygame
import os

from enemies.enemy import Enemy

images = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
        images.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/enemies/2", "2_enemies_1_run_0" + add_str) + ".png"),
            (64, 64)))


class Enemy1(Enemy):

    def __init__(self,path):
        super().__init__(path)
        self.images = images[:]
        self.max_health = 15
        self.name = "enemy1"
        self.money = 25
        self.health = self.max_health
