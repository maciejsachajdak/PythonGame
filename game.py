import os
import random
import time

import pygame
from pygame import mixer

from enemies.boss import Boss
from enemies.enemy1 import Enemy1
from enemies.enemy2 import Enemy2
from enemies.enemy3 import Enemy3
from menu.Menu import MainMenu, VerticalMenu, WaveControlButton, PauseMenu
from towers.archerTower import ArcherTowerLong, ArcherTowerShort
from towers.supportTower import DamageTower, RangeTower, StarFarm

pygame.font.init()
pygame.mixer.init()

lives_img = pygame.image.load(os.path.join("game_assets/GUI", "heart.png"))
star_img = pygame.image.load(os.path.join("game_assets/GUI", "star.png"))
side_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "verticalMenu.png")),
                                       (110, 550))
main_menu_img = pygame.image.load(os.path.join("game_assets/GUI", "mainMenu.png"))
pause_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "pause_menu.png")),
                                        (400, 100))
fail_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "fail.png")),
                                       (250, 320))
win_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "win.png")),
                                      (250, 320))
settings_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/GUI", "button_settings.png")),
                                         (75, 75))

map1 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "map1.png")), (302, 170))
map2 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "map2.png")), (302, 170))
map3 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "map3.png")), (302, 170))

back_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "back_button.png")), (75, 75))

next_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_right.png")), (75, 75))

restart_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_restart.png")), (75, 75))

music_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_music.png")), (75, 75))

sound_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_sound.png")), (75, 75))

home_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "home_btn.png")), (75, 75))

play_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_play.png")), (150, 150))

summary = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "summary.png")), (180, 110))

archer_tower_button_img1 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "archerButton1.png")), (85, 85))
archer_tower_button_img2 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "archerButton2.png")), (85, 85))
support_tower_button_img1 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "supportButton1.png")), (85, 85))
support_tower_button_img2 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "supportButton2.png")), (85, 85))
support_tower_button_img3 = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "supportButton3.png")), (85, 85))

wave_start_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_start.png")), (75, 75))
wave_pause_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_pause.png")), (75, 75))
wave_faster_button = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "button_quick.png")), (75, 75))

waveBackground = pygame.transform.scale(
    pygame.image.load(os.path.join("game_assets/GUI", "waveBackground.png")), (200, 60))

attack_tower_names = ["archer1", "archer2"]
support_tower_names = ["support1", "support2", "support3"]

path1 = [(-10, 460), (181, 460), (222, 515), (287, 525), (361, 495), (433, 525), (710, 530),
         (782, 496), (808, 452), (808, 415), (784, 351), (700, 313), (480, 310), (449, 270), (418, 207),
         (442, 141), (495, 96), (750, 85), (1301, 85)]
path2_1 = [(-10, 553), (4, 553), (75, 554), (334, 550), (380, 521), (416, 445), (440, 368), (481, 345), (546, 336),
           (611, 368), (665, 399), (752, 366), (791, 292), (809, 209), (879, 170), (1107, 167), (1245, 222),
           (1300, 222)]
path2_2 = [(-10, 548), (203, 548), (353, 543), (414, 471), (437, 390), (497, 330), (553, 336), (621, 370), (646, 453),
           (676, 520), (772, 540), (1300, 540)]
path3 = [(59, 750), (59, 698), (120, 618), (181, 628), (426, 416), (714, 426), (780, 333), (764, 279), (722, 270),
         (490, 280), (440, 322), (417, 387), (440, 420), (600, 420), (728, 420), (794, 338), (808, 206), (954, 73),
         (1043, 80), (1247, 284), (1300, 285)]

waves1 = [
    [15, 0, 0, 0],
    [20, 10, 0, 0],
    [25, 15, 5, 0],
    [40, 25, 15, 0],
    [50, 25, 25, 1]
]
waves2 = [
    [35, 15, 4, 0],
    [45, 20, 10, 0],
    [55, 25, 15, 0],
    [85, 40, 20, 1],
    [110, 50, 25, 2]
]
waves3 = [
    [5, 40, 1, 0],
    [30, 50, 10, 0],
    [50, 50, 20, 1],
    [50, 50, 50, 2],
    [0, 100, 75, 3]
]

mixer.music.load('music/yoitrax - Warrior.mp3')
mixer.music.play(-1)
build_sound = mixer.Sound('music/build.wav')
sell_sound = mixer.Sound('music/sell.wav')
upgrade_sound = mixer.Sound('music/upgrade.wav')
click_sound = mixer.Sound('music/click.wav')


class Game:

    def __init__(self):
        self.game_in_menu = True
        self.game_in_main = True
        self.width = 1250
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.monsters_beat = 0
        self.attack_towers = []
        self.support_towers = []
        self.lives = 10
        self.money = 2000
        self.start_money = self.money
        self.money_earn = 0
        self.start_lives = self.lives
        self.map1_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/backgrounds", "bg1.png")),
                                               (self.width, self.height))
        self.map2_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/backgrounds", "bg2.png")),
                                               (self.width, self.height))
        self.map3_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/backgrounds", "bg3.png")),
                                               (self.width, self.height))
        self.background = self.map1_img
        self.timer = time.time()
        self.timer1 = time.time()
        self.font1 = pygame.font.SysFont("comicsans", 50)
        self.font2 = pygame.font.SysFont("comicsans", 30)
        self.font3 = pygame.font.SysFont("comicsans", 16)
        self.selected_tower = None
        self.moving_object = None
        self.fail = False
        self.win = False

        self.main_menu = MainMenu(0, 0, pygame.transform.scale(main_menu_img, (self.width, self.height)))
        self.main_menu.add_button(play_button, "play")
        self.main_menu.add_button(music_button, "music")
        self.main_menu.add_button(sound_button, "sound")

        self.second_menu = MainMenu(0, 0, pygame.transform.scale(main_menu_img, (self.width, self.height)))
        self.second_menu.add_button(map1, "map1")
        self.second_menu.add_button(map2, "map2")
        self.second_menu.add_button(map3, "map3")
        self.second_menu.add_button(back_button, "back")

        self.vertical_menu = VerticalMenu(self.width - side_menu_img.get_width() + 80, 280, side_menu_img)
        self.vertical_menu.add_button(archer_tower_button_img1, "archer1", 1000)
        self.vertical_menu.add_button(archer_tower_button_img2, "archer2", 1500)
        self.vertical_menu.add_button(support_tower_button_img1, "support1", 500)
        self.vertical_menu.add_button(support_tower_button_img2, "support2", 750)
        self.vertical_menu.add_button(support_tower_button_img3, "support3", 2000)

        self.pause_menu = PauseMenu(self.width // 2 - pause_menu_img.get_width() // 2,
                                    self.height // 2 - pause_menu_img.get_height() // 2, pause_menu_img)
        self.pause_menu.add_button(settings_button, "pause")
        self.pause_menu.add_button(back_button, "back")
        self.pause_menu.add_button(music_button, "music")
        self.pause_menu.add_button(sound_button, "sound")
        self.pause_menu.add_button(home_button, "home")
        self.pause_button_clicked = False

        self.fail_menu = PauseMenu(self.width // 2 - fail_menu_img.get_width() // 2,
                                   self.height // 2 - fail_menu_img.get_height() // 2, fail_menu_img)
        self.fail_menu.add_button(home_button, "home1")
        self.fail_menu.add_button(restart_button, "restart")

        self.win_menu = PauseMenu(self.width // 2 - win_menu_img.get_width() // 2,
                                  self.height // 2 - win_menu_img.get_height() // 2, win_menu_img)
        self.win_menu.add_button(home_button, "home1")
        self.win_menu.add_button(next_button, "next")

        self.wave = 0
        self.waves = waves1
        self.current_wave = self.waves[self.wave][:]
        self.pause = True
        self.pause1 = self.pause
        self.faster = False
        self.path = path1
        self.fps = 30
        self.waveControlButton = WaveControlButton(wave_start_button, wave_pause_button, wave_faster_button, 10,
                                                   self.height - 85)
        self.music = True
        self.sound = True

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:

            if not self.faster:
                self.fps = 30
            else:
                self.fps = 300

            clock.tick(self.fps)

            pos = pygame.mouse.get_pos()

            if self.game_in_menu:
                if self.game_in_main:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            button_clicked = self.main_menu.get_clicked(pos[0], pos[1])
                            if button_clicked:
                                if self.sound:
                                    click_sound.play()
                                if button_clicked == "play":
                                    self.game_in_main = False
                                if button_clicked == "music":
                                    self.main_menu.music_off_on()
                                    if self.music:
                                        mixer.music.pause()
                                        self.music = False
                                    else:
                                        mixer.music.unpause()
                                        self.music = True
                                if button_clicked == "sound":
                                    self.main_menu.sound_off_on()
                                    if self.sound:
                                        self.sound = False
                                    else:
                                        self.sound = True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button_clicked = self.second_menu.get_clicked(pos[0], pos[1])
                        if button_clicked:
                            if self.sound:
                                click_sound.play()
                            if button_clicked == "back":
                                self.game_in_main = True
                            elif button_clicked == "map1":
                                self.background = self.map1_img
                                self.path = path1
                                self.waves = waves1
                                self.current_wave = self.waves[self.wave][:]
                                self.money = 3000
                                self.lives = 15
                                self.game_in_menu = False
                                if not self.sound:
                                    self.pause_menu.sound_off_on()
                                if not self.music:
                                    self.pause_menu.music_off_on()
                            elif button_clicked == "map2":
                                self.background = self.map2_img
                                self.waves = waves2
                                self.current_wave = self.waves[self.wave][:]
                                self.path = path2_2
                                self.money = 4000
                                self.lives = 10
                                self.game_in_menu = False
                                if not self.sound:
                                    self.pause_menu.sound_off_on()
                                if not self.music:
                                    self.pause_menu.music_off_on()
                            elif button_clicked == "map3":
                                self.background = self.map3_img
                                self.path = path3
                                self.waves = waves3
                                self.money = 4000
                                self.lives = 5
                                self.current_wave = self.waves[self.wave][:]
                                self.game_in_menu = False
                                if not self.sound:
                                    self.pause_menu.sound_off_on()
                                if not self.music:
                                    self.pause_menu.music_off_on()
            else:
                # generate monsters
                if not self.pause:
                    if time.time() - self.timer >= random.randrange(1, 5):
                        self.timer = time.time()
                        self.generate_enemies()

                # check for moving object
                if self.moving_object:
                    self.moving_object.move(pos[0], pos[1])

                # main event loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.moving_object:
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)
                            if self.sound:
                                build_sound.play()
                            self.moving_object.moving = False
                            self.moving_object = None
                        else:
                            # set button
                            set_button = self.pause_menu.get_clicked(pos[0], pos[1])
                            if set_button:
                                if set_button == "pause":
                                    self.pause1 = self.pause
                                    self.pause = True
                                    self.pause_button_clicked = True
                                elif set_button == "back" and self.pause_button_clicked:
                                    self.pause = self.pause1
                                    self.pause_button_clicked = False
                                elif set_button == "sound" and self.pause_button_clicked:
                                    self.pause_menu.sound_off_on()
                                    if self.sound:
                                        self.sound = False
                                    else:
                                        self.sound = True
                                elif set_button == "home" and self.pause_button_clicked:
                                    self.home_restart_next()
                                elif set_button == "music" and self.pause_button_clicked:
                                    self.pause_menu.music_off_on()
                                    if self.music:
                                        mixer.music.pause()
                                        self.music = False
                                    else:
                                        mixer.music.unpause()
                                        self.music = True

                            # check for play or pause
                            if self.waveControlButton.click(pos[0], pos[1]):
                                self.pause = not self.pause
                                self.waveControlButton.change_image()

                            # check for speed
                            if self.waveControlButton.click_speed_button(pos[0], pos[1]):
                                if not self.faster:
                                    self.faster = True
                                    self.waveControlButton.change_speed_image()
                                else:
                                    self.faster = False
                                    self.waveControlButton.change_speed_image()

                            # if you click on side menu
                            side_menu_button = self.vertical_menu.get_clicked(pos[0], pos[1])
                            if side_menu_button:
                                item_cost = self.vertical_menu.get_item_cost(side_menu_button)
                                if self.money >= item_cost:
                                    self.money -= item_cost
                                    self.add_tower(side_menu_button)

                            button_clicked = None

                            if self.selected_tower:
                                button_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                                if button_clicked:
                                    if button_clicked == "Upgrade":
                                        cost = self.selected_tower.get_item_cost()
                                        if cost != "MAX":
                                            if self.money >= cost:
                                                self.money -= cost
                                                if self.sound:
                                                    upgrade_sound.play()
                                                self.selected_tower.upgrade()
                                    elif button_clicked == "Sell":
                                        if self.sound:
                                            sell_sound.play()
                                        self.money += self.selected_tower.sell_price[self.selected_tower.level - 1]
                                        if self.support_towers.__contains__(self.selected_tower):
                                            for tower in self.selected_tower.effected:
                                                if isinstance(self.selected_tower, DamageTower):
                                                    tower.damage = tower.original_damage
                                                if isinstance(self.selected_tower, RangeTower):
                                                    tower.range = tower.original_range
                                                if isinstance(self.selected_tower, StarFarm):
                                                    tower.support_by_star_farm = False
                                                    tower.add_money = 0
                                            self.support_towers.remove(self.selected_tower)
                                            self.selected_tower = None
                                        else:
                                            self.attack_towers.remove(self.selected_tower)
                                            self.selected_tower = None

                                    elif button_clicked == "next":
                                        if self.selected_tower.menu.counter < 2:
                                            self.selected_tower.menu.counter += 1
                                        else:
                                            self.selected_tower.menu.counter = 0
                                    elif button_clicked == "back":
                                        if self.selected_tower.menu.counter > 0:
                                            self.selected_tower.menu.counter -= 1
                                        else:
                                            self.selected_tower.menu.counter = 2
                            else:
                                pass

                            fails_button = self.fail_menu.get_clicked(pos[0], pos[1])
                            win_button = self.win_menu.get_clicked(pos[0], pos[1])
                            if fails_button:
                                if fails_button == "home1":
                                    self.home_restart_next()
                                elif fails_button == "restart":
                                    self.home_restart_next(True, False)
                            if win_button:
                                if win_button == "home1":
                                    self.home_restart_next()
                                elif win_button == "next":
                                    self.home_restart_next(False, True)

                            if not button_clicked:
                                for tower in self.attack_towers:
                                    if tower.click(pos[0], pos[1]):
                                        tower.selected = True
                                        self.selected_tower = tower
                                    else:
                                        tower.selected = False

                                # support tower
                                for tower in self.support_towers:
                                    if tower.click(pos[0], pos[1]):
                                        tower.selected = True
                                        self.selected_tower = tower
                                    else:
                                        tower.selected = False

                if not self.pause:
                    # loop through enemies
                    to_del = []
                    for enemy in self.enemies:
                        enemy.move()
                        if enemy.x >= 1300:
                            to_del.append(enemy)

                    # delete all enemies off the screen
                    for d in to_del:
                        self.lives -= 1
                        self.enemies.remove(d)

                    # loop through attack towers
                    for tower in self.attack_towers:
                        money, monsters = tower.attack(self.enemies, self.sound)
                        self.money += money
                        self.money_earn += money
                        self.monsters_beat += monsters

                    # loop through support towers
                    for tower in self.support_towers:
                        tower.support(self.attack_towers)

                    # if you lose
                    if self.lives <= 0:
                        self.fail = True
                        self.pause = True

            self.draw()

        pygame.quit()

    def draw(self):

        if self.game_in_main:
            self.main_menu.draw(self.window)
        else:
            self.second_menu.draw(self.window)
        if not self.game_in_menu:
            self.window.blit(self.background, (0, 0))
            # draw attack towers
            for tower in self.attack_towers:
                tower.draw(self.window)

            # draw support towers
            for tower in self.support_towers:
                tower.draw(self.window)

            # draw enemies
            for enemy in self.enemies:
                if enemy.name == "boss" and time.time() - self.timer1 >= 10 and not self.pause:
                    self.timer1 = time.time()
                    enemy.ultra_on()
                if enemy.name == "boss" and enemy.reset_ult:
                    enemy.ultra_off()
                enemy.draw(self.window)

            # draw moving object
            if self.moving_object:
                self.moving_object.draw(self.window)

            # draw menu
            self.vertical_menu.draw(self.window)

            self.pause_menu.draw(self.window, self.pause_button_clicked)

            # draw button to wave control
            self.waveControlButton.draw(self.window)

            # draw lives
            text = self.font1.render(str(self.lives), 1, (255, 255, 255))
            life = pygame.transform.scale(lives_img, (50, 50))
            start_x = self.width - life.get_width() - 10

            self.window.blit(text, (start_x - text.get_width() - 10, 10))
            self.window.blit(life, (start_x, 20))

            # draw currency
            text = self.font1.render(str(self.money), 1, (255, 255, 255))
            star = pygame.transform.scale(star_img, (50, 50))
            start_x = self.width - star.get_width() - 10

            self.window.blit(text, (start_x - text.get_width() - 10, life.get_height() + 20))
            self.window.blit(star, (start_x, life.get_height() + 32))

            # draw wave number
            self.window.blit(waveBackground, (10, 10))
            text = self.font2.render("Wave #" + str(self.wave + 1), 1, (255, 255, 255))
            self.window.blit(text, (10 + waveBackground.get_width() // 2 - text.get_width() // 2, 18))

            if self.fail:
                self.fail_menu.draw(self.window, True)
            if self.win:
                self.win_menu.draw(self.window, True)
            if self.fail or self.win:
                text1 = self.font3.render("You beat: " + str(self.wave) + "/" + str(len(self.waves)) + " waves", 1,
                                          (255, 255, 255))
                text2 = self.font3.render("You beat: " + str(self.monsters_beat) + " monsters", 1, (255, 255, 255))
                text3 = self.font3.render("You earn: " + str(self.money_earn) + " stars", 1, (255, 255, 255))
                self.window.blit(summary, (
                    self.width // 2 - summary.get_width() // 2, self.height // 2 - summary.get_height() // 1.3))
                self.window.blit(text1, (
                    self.width // 2 - text1.get_width() // 2, self.height // 2 - text1.get_height() * 3 - 8))
                self.window.blit(text2, (
                    self.width // 2 - text2.get_width() // 2, self.height // 2 - text2.get_height() * 1.8))
                self.window.blit(text3,
                                 (self.width // 2 - text3.get_width() // 2, self.height // 2 - text3.get_height() + 18))

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["archer1", "archer2", "support2", "support1", "support3"]
        object_list = [ArcherTowerLong(x, y), ArcherTowerShort(x, y), DamageTower(x, y), RangeTower(x, y),
                       StarFarm(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

    def generate_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                if self.wave < len(self.waves):
                    self.current_wave = self.waves[self.wave]
                else:
                    self.win = True
                self.pause = True
                self.waveControlButton.image = self.waveControlButton.play
        else:
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    if self.background == self.map2_img:
                        self.path = random.choice([path2_2, path2_1])
                    wave_enemies = [Enemy1(self.path), Enemy2(self.path), Enemy3(self.path), Boss(self.path)]
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def home_restart_next(self, restart=False, next_round=False):
        if not restart:
            self.game_in_menu = True
            if not next_round:
                self.game_in_main = True
        self.pause = True
        self.faster = False
        self.wave = 0
        self.enemies = []
        self.support_towers = []
        self.attack_towers = []
        self.pause_button_clicked = False
        self.waveControlButton.image = self.waveControlButton.play
        self.waveControlButton.speed_image = self.waveControlButton.speed
        self.current_wave = self.waves[self.wave][:]
        self.money = self.start_money
        self.lives = self.start_lives
        self.fail = False
        self.win = False
        if not self.music:
            self.music = False
        if not self.sound:
            self.sound = False
