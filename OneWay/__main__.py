import random

import pygame
from sprites import Road, CornerRoad, Highlight, Logo, Start, Background, Restart, Building

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

    global points
    points += -5
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
start.rect.left = 67
start.rect.top = 369

sprites_list.add(menu)
sprites_list.add(start)

menuSel = 1

# Menu Game Loop
while runMenu:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runMenu = False
            runGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                menuSel = 1
                start.select(1)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pass
            elif event.key == pygame.K_RETURN or event.key == pygame.K_z:
                if menuSel == 1:
                    runMenu = False


    sprites_list.update()
    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # Sets FPS. Set at 60.

# Main Game Loop

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

def clearBoard(level:int):
    global playerHighlight, playerRoad, background, restart, blocked_squares, b1, b2, building_squares, points, lvlpoints
    lvlpoints = 0
    if level > 8:
        level = 8

    level=level*10

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

    restart.rect.x = 32
    restart.rect.y = 529
    sprites_list.add(restart)

    for i in road_sprites:
        i.kill()

    for b, r in building_sprites:
        r.kill()

    building_squares = []

    for l in range(level):
        validPos = False
        building = Building()
        x1, y1 = b1
        x2, y2 = b2
        attempts = 0
        while not validPos:
            pos1_pre = random.randint(0, 16)
            pos2_pre = random.randint(0, 16)
            pos = (x1 + (pos1_pre*32), y1 + (pos2_pre*32))
            x, y = pos
            pos2 = (x, y+32)
            pos3 = (x, y-32)
            if pos not in blocked_squares or pos not in building_squares:
                if pos2 in building_squares or pos3 in building_squares or pos == (200, 288):
                    pass
                else:
                    building.rect.x, building.rect.y = pos
                    sprites_list.add(building)
                    validPos = True
                    building_squares.append(pos)
                    building_sprites.append((pos, building))
            elif attempts > 10:
                validPos == True
                print("Failed placing a building!")
            else:
                attempts+=1

    print(building_squares)



def boundChecker(tl, br, xchange=0, ychange=0):
    x, y = tl
    x_, y_ = br
    b1_x, b1_y = b1
    b2_x, b2_y = b2
    xy = (x+xchange, y+ychange)
    if xy in blocked_squares or xy in building_squares:
        return False
    elif x+xchange < b1_x or y+ychange < b1_y or x_+xchange > b2_x or y_+ychange > b2_y:
        if(y+ychange) == 288 and x+xchange == 776:
            return True
        return False
    else:
        return True

clearBoard(1)
level = 1
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
                lvlpoints +=100
                print(building_sprites)
                for bs in building_sprites:
                    p, b = bs
                    if(p == (playerRoad.rect.x, playerRoad.rect.y - 32)):
                        b.glow()
                print(points)

            if playerRoad.rect.y == 288 and playerRoad.rect.x == 776:
                bonus = (level / 10)*lvlpoints
                points += int(bonus)
                print(f"Level Complete! Gained {points} points ({int(bonus)} Bonus)! (Level {level})")
                level +=1
                clearBoard(level)


    screen.fill(BLACK)

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
