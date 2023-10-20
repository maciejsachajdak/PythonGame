import os

import pygame

pygame.font.init()

star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "star.png")), (23, 23))
dark = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "dark.png")), (1300, 700))
choose_enemy = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "choose_enemy.png")), (180, 40))


class Button:
    """
    guziki dla menu wiez
    """

    def __init__(self, menu, image, name):
        self.name = name
        self.image = image
        self.y = menu.y - 108
        self.menu = menu
        self.x = self.menu_x()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def menu_x(self):
        if self.name == "Upgrade":
            return self.menu.x - self.menu.background.get_width() / 2 + 15
        elif self.name == "Sell":
            return self.menu.x + self.menu.background.get_width() / 2 - 73
        elif self.name == "back":
            return self.menu.x
        else:
            return self.menu.x

    def click(self, X, Y):
        """
        jak kliknie sie w guzik zwraca prawde
        :param X: int
        :param Y: int
        :return: bool
        """
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
                return True
        return False

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def update(self):
        if self.name == "Upgrade":
            self.x = self.menu.x - self.menu.background.get_width() / 2 + 15
            self.y = self.menu.y - 108
        elif self.name == "Sell":
            self.x = self.menu.x + self.menu.background.get_width() / 2 - 73
            self.y = self.menu.y - 108
        elif self.name == "back":
            self.x = self.menu.x - choose_enemy.get_width() // 2 + 10
            self.y = self.menu.y + choose_enemy.get_height() + 10
        elif self.name == "next":
            self.x = self.menu.x + choose_enemy.get_width() // 2 - 40
            self.y = self.menu.y + choose_enemy.get_height() + 10


class WaveControlButton(Button):
    def __init__(self, play_image, pause_image, speed_image, x, y):
        self.flipped = False
        self.image = play_image
        self.play = play_image
        self.pause = pause_image
        self.speed_image = speed_image
        self.speed = speed_image
        self.rotate_speed = pygame.transform.flip(speed_image, True, False)
        self.speed_button_shift = 100
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def change_image(self):
        if self.image == self.play:
            self.image = self.pause
        else:
            self.image = self.play

    def change_speed_image(self):
        if self.speed_image == self.speed:
            self.flipped = True
            self.speed_image = self.rotate_speed
        else:
            self.flipped = False
            self.speed_image = self.speed

    def draw(self, window):
        super().draw(window)
        if not self.flipped:
            window.blit(self.speed_image, (self.x + self.speed_button_shift, self.y))
        else:
            window.blit(self.speed_image, (self.x + self.speed_button_shift - 2, self.y))

    def click_speed_button(self, X, Y):
        if self.x + self.width + self.speed_button_shift >= X >= self.x + self.speed_button_shift:
            if self.y + self.height >= Y >= self.y:
                return True
        return False


class MainMenu:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.buttons = []
        self.items = 0
        self.background = image
        self.font = pygame.font.SysFont("comicsans", 20)
        self.title = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "title.png")), (750, 200))
        self.music_button_on = pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/GUI", "button_music.png")), (75, 75))
        self.music_button_off = pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/GUI", "music_off.png")), (75, 75))
        self.sound_button_on = pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/GUI", "button_sound.png")), (75, 75))
        self.sound_button_off = pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/GUI", "button_sound_off.png")), (75, 75))

    def music_off_on(self):
        for button in self.buttons:
            if button.name == "music":
                if button.image == self.music_button_off:
                    button.image = self.music_button_on
                else:
                    button.image = self.music_button_off

    def sound_off_on(self):
        for button in self.buttons:
            if button.name == "sound":
                if button.image == self.sound_button_off:
                    button.image = self.sound_button_on
                else:
                    button.image = self.sound_button_off

    def add_button(self, image, name):
        """
        dodaje przyciski
        :param image: surface
        :param name: str
        :return: None
        """
        self.items += 1
        self.buttons.append(MainMenuButton(self, image, name))

    def get_clicked(self, X, Y):
        """
        zwraca nazwe kliknietego przycisku
        :param X: int
        :param Y: int
        :return: str
        """
        for button in self.buttons:
            if button.click(X, Y):
                return button.name

        return None

    def draw(self, window):
        window.blit(self.background, (self.x, self.y))
        window.blit(self.title, (self.background.get_width() // 2 - self.title.get_width() // 2,
                                 self.y + self.background.get_height() // 2 - self.title.get_height() * 1.5))
        for item in self.buttons:
            item.draw(window)


class MainMenuButton(Button):

    def __init__(self, menu, image, name):
        super().__init__(menu, image, name)
        self.x = self.menu.width // 2 - image.get_width() // 2
        self.y = self.menu.height // 2 - image.get_height() // 2

    def draw(self, window):
        if self.name == "map1":
            self.x = 45
            self.y = self.menu.height // 2
        elif self.name == "map2":
            self.x = self.menu.width // 2 - self.image.get_width() // 2
            self.y = self.menu.height // 2
        elif self.name == "map3":
            self.x = self.menu.width - self.image.get_width() - 45
            self.y = self.menu.height // 2
        elif self.name == "back" or self.name == "music":
            self.x = 30
            self.y = self.menu.height - 100
        elif self.name == "sound":
            self.x = 50 + self.image.get_width()
            self.y = self.menu.height - 100

        window.blit(self.image, (self.x, self.y))


class Menu(MainMenu):
    """
    menu dla wiez na ulepszenie i sprzedaz
    """

    def __init__(self, tower, x, y, image, item_cost, sell_cost):
        super().__init__(x, y, image)
        self.items_cost = item_cost
        self.sell_cost = sell_cost
        self.font = pygame.font.SysFont("comicsans", 20)
        self.tower = tower
        self.counter = 0

    def get_item_cost(self):
        """
        zwraca koszt ulepszenia na wyzszy poziom
        :return: int
        """
        return self.items_cost[self.tower.level - 1]

    def add_button(self, image, name):
        self.items += 1
        self.buttons.append(Button(self, image, name))

    def draw(self, window):
        """
        rysowanie menu i przyciskow
        :param window: surface
        :return: None
        """
        if isinstance(self.tower, ArcherTowerLong) or isinstance(self.tower, ArcherTowerShort):
            window.blit(choose_enemy, (self.x - choose_enemy.get_width() // 2, self.y + self.tower.height // 2))
            enemy_to_attack = ["FIRST", "LAST", "STRONG"]
            text = self.font.render(enemy_to_attack[self.counter], 1, (255, 255, 255))
            window.blit(text, (self.x -text.get_width()//2,  self.y + self.tower.height // 2 +text.get_height()//5))

        window.blit(self.background, (self.x - self.background.get_width() / 2 - 5, self.y - 130))

        for item in self.buttons:
            item.draw(window)
            if item.name != "back" and item.name != "next":
                if item.name == "Upgrade":
                    text = self.font.render(str(self.items_cost[self.tower.level - 1]), 1, (255, 255, 255))
                elif item.name == "Sell":
                    text = self.font.render(str(self.sell_cost[self.tower.level - 1]), 1, (255, 255, 255))
                window.blit(star, (item.x + item.width // 2 + 14, item.y + 49))
                window.blit(text, (item.x - 8, item.y + item.height // 2 + 25))

    def get_clicked(self, X, Y):
        return super().get_clicked(X, Y)

    def update(self):
        """
        po ruszaniu wieza updateuje pozycje przycisku
        :return: None
        """
        for button in self.buttons:
            button.update()


class VerticalMenu(MainMenu):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.font = pygame.font.SysFont("comicsans", 20)

    def draw(self, window):
        window.blit(self.background, (self.x - self.background.get_width() / 2 - 30, self.y - 130))
        for item in self.buttons:
            window.blit(star, (item.x + item.width // 2 + 15, item.y + 80))
            text = self.font.render(str(item.cost), 1, (255, 255, 255))
            window.blit(text, (item.x + item.width // 4 - 10, item.y + item.height // 2 + 35))
            item.draw(window)

    def add_button(self, image, name, cost):
        self.items += 1
        button_x = self.x - self.width // 2 - 17.5
        button_y = self.y + (self.items - 1) * 108 - 125
        self.buttons.append(VerticalButton(button_x, button_y, image, name, cost))

    def get_item_cost(self, name):
        for button in self.buttons:
            if button.name == name:
                return button.cost
        return -1


class VerticalButton(Button):

    def __init__(self, x, y, image, name, cost):
        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.cost = cost


class PauseMenuButton(Button):

    def __init__(self, menu, image, name):
        super().__init__(menu, image, name)

    def draw(self, window):
        if self.name == "pause":
            self.x = 10
            self.y = 80
        elif self.name == "back":
            self.x = dark.get_width() // 2 - self.menu.width // 2
            self.y = dark.get_height() // 2 - self.image.get_height() // 2
        elif self.name == "home":
            self.x = dark.get_width() // 2 + self.image.get_width()
            self.y = dark.get_height() // 2 - self.image.get_height() // 2
        elif self.name == "music":
            self.x = dark.get_width() // 2 - self.image.get_width() * 1.5
            self.y = dark.get_height() // 2 - self.image.get_height() // 2
        elif self.name == "sound":
            self.x = dark.get_width() // 2 - self.image.get_width() // 6
            self.y = dark.get_height() // 2 - self.image.get_height() // 2
        elif self.name == "home1":
            self.x = dark.get_width() // 2 - self.image.get_width() * 1.5
            self.y = dark.get_height() // 2 + self.image.get_height() // 1.5
        elif self.name == "restart" or self.name == "next":
            self.x = dark.get_width() // 2 - self.image.get_width() // 5
            self.y = dark.get_height() // 2 + self.image.get_height() // 1.5

        window.blit(self.image, (self.x, self.y))


class PauseMenu(MainMenu):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def add_button(self, image, name):
        self.items += 1
        self.buttons.append(PauseMenuButton(self, image, name))

    def get_clicked(self, X, Y):
        for button in self.buttons:
            if button.click(X, Y):
                return button.name

        return None

    def draw(self, window, button_clicked):
        if button_clicked:
            window.blit(dark, (0, 0))
            window.blit(self.background, (self.x, self.y))

            for item in self.buttons:
                if item.name != 'pause':
                    item.draw(window)

        for item in self.buttons:
            if item.name == 'pause':
                item.draw(window)


from towers.archerTower import ArcherTowerLong, ArcherTowerShort
