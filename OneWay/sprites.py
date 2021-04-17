import pygame

WHITE = (255, 255, 255)
road_img = pygame.image.load("OneWay/img/road.png")
road_turn_img = pygame.image.load("OneWay/img/roadc.png")
highlight = pygame.image.load("OneWay/img/highlight.png")
start_des = pygame.image.load("OneWay/img/start_des.png")
start = pygame.image.load("OneWay/img/start.png")

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
        self.image = pygame.image.load("OneWay/img/oneway.png")
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


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OneWay/img/background.png")
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (0, 0, 0), [800, 600, 0, 0])