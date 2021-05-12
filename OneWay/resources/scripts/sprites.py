import random
import pygame

WHITE = (255, 255, 255)
road_img = pygame.image.load("OneWay/resources/img/road.png")
road_turn_img = pygame.image.load("OneWay/resources/img/roadc.png")
highlight = pygame.image.load("OneWay/resources/img/highlight_2.png")
start_des = pygame.image.load("OneWay/resources/img/start_des.png")
start = pygame.image.load("OneWay/resources/img/start.png")

class Road(pygame.sprite.Sprite):
    # Creates the roads that a player builds.
    def __init__(self, color, width, height):
        super().__init__()
        # Draws picture of road
        self.image = road_img
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [32, 32, width, height])
        self.rotation = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def rotate(self, degrees):
        self.rotation = degrees
        self.image = pygame.transform.rotate(road_img, degrees)

class CornerRoad(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = road_turn_img
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [32, 32, width, height])

    def rotate(self, degrees):
        self.rotation = degrees
        self.image = pygame.transform.rotate(road_turn_img, degrees)

class Highlight(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = highlight
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [32, 32, 32, 32])

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def rotate(self, degree):
        self.image = pygame.transform.rotate(highlight, degree)

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/oneway.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])

class Start(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = start_des
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [314, 59, 0, 0])

    def select(self, sel):
        if sel == 1:
            self.image = start
        else:
            self.image = start_des


class Misc(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/misc_des.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [251, 59, 0, 0])

    def select(self, sel):
        if sel == 1:
            self.image = pygame.image.load("OneWay/resources/img/misc.png")
        else:
            self.image = pygame.image.load("OneWay/resources/img/misc_des.png")


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/background.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])

class Restart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        restart_img = pygame.image.load("OneWay/resources/img/restart.png")
        self.image = restart_img
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [125, 49, 0, 0])

class Generate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        restart_img = pygame.image.load("OneWay/resources/img/generating.png")
        self.image = restart_img
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])

class Building(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_img = pygame.image.load("OneWay/resources/img/buildings.png")
        self.glow_img = pygame.image.load("OneWay/resources/img/buildings_lit.png")
        self.image = self.base_img
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [125, 49, 0, 0])
        self.glowing = False
        self.special = False

        sp_ch = random.randint(1, 15)
        if sp_ch == 15:
            self.specialBuilding()

    def glow(self):
        self.base_img = self.glow_img
        self.image = self.base_img
        self.glowing = True

    def specialBuilding(self):
        self.special = True
        images = [('OneWay/resources/img/building_alt_1.png', 'OneWay/resources/img/building_alt_1_lit.png'), ('OneWay/resources/img/building_alt_2.png', 'OneWay/resources/img/building_alt_2_lit.png')]
        tmp_base_img, tmp_glow_img = random.choice(images)
        self.base_img, self.glow_img = pygame.image.load(tmp_base_img), pygame.image.load(tmp_glow_img)
        self.image = self.base_img

class Endless(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/mode_end.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])
        self.selected = False

    def select(self, select:bool):
        if select and not self.selected:
            self.selected = True
            self.rect.x += 14
            self.image = pygame.image.load("OneWay/resources/img/mode_end_sel.png")
        elif not select:
            if self.selected:
                self.rect.x -= 14
            self.image = pygame.image.load("OneWay/resources/img/mode_end.png")
            self.selected = False

class Puzzle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/mode_puzzle.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])
        self.selected = False

    def select(self, select:bool):
        if select and not self.selected:
            self.selected = True
            self.image = pygame.image.load("OneWay/resources/img/mode_puzzle_sel.png")
            self.rect.x += 14
        elif not select:
            if self.selected:
                self.rect.x -= 14
            self.image = pygame.image.load("OneWay/resources/img/mode_puzzle.png")
            self.selected = False

class Selector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/pointer.png").convert()
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])
        self.selected = False

    def select(self, select:bool):
        if select and not self.selected:
            self.selected = True
            self.image = pygame.image.load("OneWay/resources/img/pointer_sel.png")
        elif not select:
            self.image = pygame.image.load("OneWay/resources/img/pointer.png")
            self.selected = False

class PX_Number(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/char/0.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [56, 56, 0, 0])

    def char(self, no):
        charDict = {
            0:"OneWay/resources/img/char/0.png",
            1:"OneWay/resources/img/char/1.png",
            2:"OneWay/resources/img/char/2.png",
            3:"OneWay/resources/img/char/3.png",
            4:"OneWay/resources/img/char/4.png",
            5:"OneWay/resources/img/char/5.png",
            6:"OneWay/resources/img/char/6.png",
            7:"OneWay/resources/img/char/7.png",
            8:"OneWay/resources/img/char/8.png",
            9:"OneWay/resources/img/char/9.png"
        }
        self.image = pygame.image.load(charDict[no])

class LevelDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/level.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [56, 56, 0, 0])

class Par(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/par.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [92, 28, 0, 0])

class Count(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/resources/img/count.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [156, 28, 0, 0])