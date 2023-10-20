import pygame
import os

from enemies.enemy import Enemy

images =[]

for x in range(10):
    images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/10", "2_enemies_1_RUN_00" + str(x)) + ".png"),
        (64, 64)))


class Enemy3(Enemy):

    def __init__(self, path):
        super().__init__(path)
        self.images = images[:]
        self.max_health = 40
        self.name = "enemy3"
        self.money = 75
        self.health = self.max_health
