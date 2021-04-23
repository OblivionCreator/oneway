import random

import pygame
from sprites import *
import pathgenerator

pygame.init()

# Colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Open Start Menu
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("One-Way ->")

# Stops loop when game closed
runGame = True

clock = pygame.time.Clock()

sprites_list = pygame.sprite.Group()

road_sprites = []


def newRoad(x, y, r_t, dir):
    n_rt = playerRoad.rotation
    print(x, y)

    if r_t == 0 and n_rt == 90:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(0)
    elif r_t == 90 and n_rt == 180:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(270)
    elif r_t == 180 and n_rt == 270:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(180)
    elif r_t == 0 and n_rt == 270:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(270)
    elif r_t == 90 and n_rt == 0:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(180)
    elif r_t == 180 and n_rt == 90:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(90)
    elif r_t == 270 and n_rt == 180:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(0)
    elif r_t == 270 and n_rt == 0:
        newRoad = CornerRoad(RED, 32, 32)
        newRoad.rotate(90)
    else:
        newRoad = Road(RED, 32, 32)
        newRoad.rotate(r_t)

    newRoad.rect.x = x
    newRoad.rect.y = y

    blocked_squares.append((x, y))
    road_sprites.append(newRoad)
    return newRoad


runMenu = True
menu = Logo()
start = Start()
endless = Endless()
puzzle = Puzzle()
start.rect.left = 45
start.rect.top = 174
sel1 = Selector()
sel2 = Selector()

sel1.rect.x = 45
sel1.rect.y = 238
sel2.rect.x = 45
sel2.rect.y = 276
puzzle.rect.x = 85
puzzle.rect.y = 238
endless.rect.x = 85
endless.rect.y = 276

sprites_list.add(menu, start, endless, puzzle, sel1, sel2)

menuSel = 1
pMenuSel = 0
playMenu = False
start.select(1)


# Menu Game Loop

def optSel(opt_sel):
    print(opt_sel)
    if opt_sel == 0:
        puzzle.select(False)
        endless.select(False)
        sel1.select(False)
        sel2.select(False)
    elif opt_sel == 1:
        puzzle.select(True)
        endless.select(False)
        sel1.select(True)
        sel2.select(False)
        pMenuSel = 1
    elif opt_sel == 2:
        puzzle.select(False)
        endless.select(True)
        sel1.select(False)
        sel2.select(True)
        pMenuSel = 2

# Main Game Loop


def init_game():
    global sprites_list, playerHighlight, playerRoad, background, restart, blocked_squares, b1, b2, building_sprites, building_squares, num1, num2, lvlDisplay, level
    sprites_list = pygame.sprite.Group()

    playerHighlight = Highlight()
    playerRoad = Road(RED, 32, 32)
    background = Background()
    restart = Restart()
    blocked_squares = []
    b1 = (200, 0)
    b2 = (776, 576)
    building_sprites = []
    building_squares = []
    num1 = PX_Number()
    num2 = PX_Number()
    num1.rect.x, num1.rect.y = 33, 54
    num2.rect.x, num2.rect.y = 97, 54
    lvlDisplay = LevelDisplay()
    lvlDisplay.rect.x, lvlDisplay.rect.y = 17, 22

def clearBoard(level: int):
    global playerHighlight, playerRoad, background, restart, blocked_squares, b1, b2, building_squares, points, lvlpoints, num1, num2, lvlDisplay

    lvlpoints = 0

    points = 0

    blocked_squares = []

    playerHighlight.rect.x = 136
    playerHighlight.rect.y = 256
    playerHighlight.rotate(270)
    sprites_list.add(playerHighlight)

    playerRoad.rect.x = 168
    playerRoad.rect.y = 288
    playerRoad.rotate(270)
    sprites_list.add(playerRoad)

    background.rect.x = -1
    sprites_list.add(background)
    sprites_list.add(num1, num2, lvlDisplay)

    restart.rect.x = 32
    restart.rect.y = 529
    sprites_list.add(restart)

    gen = Generate()
    gen.rect.x = 50
    gen.rect.y = 50
    sprites_list.add(gen)

    numStr = str(level)
    if level >= 99:
        num1.char(9)
        num2.char(9)
    elif level >= 10:
        num1.char(int(numStr[0]))
        num2.char(int(numStr[1]))
    else:
        num1.char(0)
        num2.char(int(numStr))

    pygame.display.flip

    for i in road_sprites:
        i.kill()

    for b, r in building_sprites:
        r.kill()

    building_squares = []

    path = pathgenerator.main()


    buildingCount = (level*level)+level
    if buildingCount > 30:
        buildingCount = 30

    for i in range(buildingCount):
        validPlacement = False
        while not validPlacement:
            pos = random.choice(path)
            building = Building()
            x, y = pos
            y=y-1
            if((x, y)) not in path:
                x = 200+(32*x)
                y = 32*(y)
                newPos = (x, y)
                building.rect.x, building.rect.y = x, y
                sprites_list.add(building)
                building_squares.append(newPos)
                building_sprites.append((newPos, building))
                validPlacement = True

    gen.kill()
    print(building_squares)


def boundChecker(tl, br, xchange=0, ychange=0):
    x, y = tl
    x_, y_ = br
    b1_x, b1_y = b1
    b2_x, b2_y = b2
    xy = (x + xchange, y + ychange)
    if xy in blocked_squares or xy in building_squares:
        return False
    elif x + xchange < b1_x or y + ychange < b1_y or x_ + xchange > b2_x or y_ + ychange > b2_y:
        if (y + ychange) == 288 and x + xchange == 776:
            return True
        return False
    else:
        return True

def endlessGame():

    global runGame

    init_game()

    clearBoard(1)
    points = 0
    lvlpoints = 0

    while runGame:

        menu.kill()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                runGame = False
            elif event.type == pygame.KEYDOWN:

                c_rt = playerRoad.rotation
                # Listens for keyboard inputs
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if boundChecker(playerRoad.rect.topleft, playerRoad.rect.bottomright, xchange=-32, ychange=0):
                        playerRoad.rotate(270)
                        playerHighlight.rotate(90)
                        sprites_list.add(newRoad(playerRoad.rect.left, playerRoad.rect.top, c_rt, 'left'))
                        playerRoad.moveLeft(32)
                        playerHighlight.moveLeft(32)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if boundChecker(playerRoad.rect.topleft, playerRoad.rect.bottomright, xchange=32, ychange=0):
                        playerRoad.rotate(90)
                        playerHighlight.rotate(270)
                        sprites_list.add(newRoad(playerRoad.rect.left, playerRoad.rect.top, c_rt, 'right'))
                        playerRoad.moveRight(32)
                        playerHighlight.moveRight(32)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if boundChecker(playerRoad.rect.topleft, playerRoad.rect.bottomright, xchange=0, ychange=-32):
                        playerRoad.rotate(0)
                        playerHighlight.rotate(0)
                        sprites_list.add(newRoad(playerRoad.rect.left, playerRoad.rect.top, c_rt, 'up'))
                        playerRoad.moveUp(32)
                        playerHighlight.moveUp(32)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if boundChecker(playerRoad.rect.topleft, playerRoad.rect.bottomright, xchange=0, ychange=+32):
                        playerRoad.rotate(180)
                        playerHighlight.rotate(180)
                        sprites_list.add(newRoad(playerRoad.rect.left, playerRoad.rect.top, c_rt, 'down'))
                        playerRoad.moveDown(32)
                        playerHighlight.moveDown(32)
                elif event.key == pygame.K_r or event.key == pygame.K_c:
                    clearBoard(level=level)

                if (playerRoad.rect.x, playerRoad.rect.y - 32) in building_squares:
                    points += 100
                    lvlpoints += 100
                    print(building_sprites)
                    for bs in building_sprites:
                        p, b = bs
                        if (p == (playerRoad.rect.x, playerRoad.rect.y - 32)):
                            b.glow()
                    print(points)

                if playerRoad.rect.y == 288 and playerRoad.rect.x == 776:
                    bonus = (level / 10) * lvlpoints
                    points += int(bonus)
                    print(f"Level Complete! Gained {points} points ({int(bonus)} Bonus)! (Level {level})")
                    level += 1
                    clearBoard(level)

        screen.fill(BLACK)

        sprites_list.update()
        sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # Sets FPS. Set at 60.

while runMenu:

    screen.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runMenu = False
            runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                menuSel -= 1
                if menuSel < 1:
                    menuSel = 1
                if menuSel == 1:
                    start.select(1)
                    pMenuSel = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                menuSel += 1
                if menuSel > 2:
                    menuSel = 2
                if menuSel == 2:
                    start.select(0)
                optSel(0)
            elif (event.key == pygame.K_UP or event.key == pygame.K_w) and menuSel == 1:
                pMenuSel -= 1
                if pMenuSel < 0:
                    pMenuSel = 0
                optSel(pMenuSel)
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and menuSel == 1:
                pMenuSel += 1
                if pMenuSel > 2:
                    pMenuSel = 2
                optSel(pMenuSel)
            elif event.key == pygame.K_z or event.key == pygame.K_RETURN:
                if pMenuSel == 1:
                    runMenu = False
                    runGame = True
                    endlessGame()

    sprites_list.update()
    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # Sets FPS. Set at 60.


# TO DO

# - Buildings
# Pickups
# Exit
# Levels

pygame.quit()
