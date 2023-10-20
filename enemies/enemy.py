import pygame
import math


class Enemy:
    def __init__(self, path):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.velocity = 3
        self.path = path
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.move_distance = 0
        self.dis = 0
        self.images = []
        self.flipped = False
        self.max_health = 0
        self.ult = False
        self.reset_ult = False

    def draw(self, window):
        """
        rysowanie przeciwnikow
        :param window: surface
        :return: None
        """

        self.img = self.images[self.animation_count]

        window.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2))
        self.draw_health_bar(window)

    def draw_health_bar(self, window):
        """
        rysuje pasek z hp
        :param window: surface
        :return: None
        """
        length = 60
        health_percent = self.health / self.max_health
        health_bar = health_percent * length

        if not self.flipped:
            pygame.draw.rect(window, (255, 0, 0), (self.x - 37, self.y - 40, length, 10), 0)
            pygame.draw.rect(window, (0, 255, 0), (self.x - 37, self.y - 40, health_bar, 10), 0)
            if self.ult:
                pygame.draw.rect(window, (0, 0, 255), (self.x - 37, self.y - 40, length, 10), 0)
        else:
            pygame.draw.rect(window, (255, 0, 0), (self.x - 12, self.y - 40, length, 10), 0)
            pygame.draw.rect(window, (0, 255, 0), (self.x - 12, self.y - 40, health_bar, 10), 0)
            if self.ult:
                pygame.draw.rect(window, (0, 0, 255), (self.x - 37, self.y - 40, length, 10), 0)

    def move(self):
        """
        ruch przeciwnikow
        :return: None
        """
        self.animation_count += 1
        if self.animation_count >= len(self.images):  # reset the animation
            if self.ult:
                self.reset_ult = True
            self.animation_count = 0

        if not self.ult:
            x1, y1 = self.path[self.path_pos]
            if self.path_pos + 1 >= len(self.path):
                x2, y2 = (1300, 400) #punkt jak skonczy sie sciezka
            else:
                x2, y2 = self.path[self.path_pos + 1]

            dirn = ((x2 - x1) * 2, (y2 - y1) * 2) #wspolrzedne
            length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2) #dlugosc wektora
            dirn = (dirn[0] / length, dirn[1] / length) #normalizacja

            move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

            self.x = move_x
            self.y = move_y

            # Go to next point
            if dirn[0] >= 0:  # moving right
                if dirn[1] >= 0:  # moving down
                    if self.x >= x2 and self.y >= y2:
                        self.path_pos += 1
                elif dirn[1] <= 0:  # moving up
                    if self.x >= x2 and self.y <= y2:
                        self.path_pos += 1
            else:  # moving left
                if dirn[1] >= 0:  # moving down
                    if self.x <= x2 and self.y <= y2:
                        self.path_pos += 1
                elif dirn[1] <= 0:  # moving up
                    if self.x <= x2 and self.y <= y2:
                        self.path_pos += 1

            # flip enemy
            if dirn[0] < 0 and not self.flipped:
                self.flipped = True
                for x, img in enumerate(self.images):
                    self.images[x] = pygame.transform.flip(img, True, False)
            elif dirn[0] > 0 and self.flipped:
                self.flipped = False
                for x, img in enumerate(self.images):
                    self.images[x] = pygame.transform.flip(img, True, False)

    def hit(self, damage):
        """
        jak dostanie hit odejmuje hp i zwraca prawde jak umiera
        :return:Bool
        """
        if not self.ult:
            self.health -= damage
        if self.health <= 0:
            return True
        return False
