import time

import pygame
import os

from enemies.enemy import Enemy

images_run = []
images_ult = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    images_run.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/boss/run", "0_boss_run_0" + add_str) + ".png"),
        (80, 80)))

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    if x >= 8:
        for i in range(10):
            images_ult.append(pygame.transform.scale(
                pygame.image.load(
                    os.path.join("game_assets/enemies/boss/ult", "0_boss_specialty_0" + add_str) + ".png"),
                (80, 80)))
    images_ult.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/boss/ult", "0_boss_specialty_0" + add_str) + ".png"),
        (80, 80)))


class Boss(Enemy):

    def __init__(self, path):
        super().__init__(path)
        self.images = images_run[:]
        self.max_health = 500
        self.name = "boss"
        self.money = 200
        self.health = self.max_health
        self.timer = time.time()

    def ultra_on(self):
        self.images = images_ult[:]
        if self.flipped:
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)
            self.flipped = False
        self.ult = True

    def ultra_off(self):
        self.images = images_run[:]
        self.ult = False
        self.reset_ult = False
