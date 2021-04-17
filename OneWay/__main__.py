import pygame
from sprites import Road, CornerRoad, Highlight, Logo, Start, Background

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

def newRoad(x, y, r_t, dir):

    n_rt = playerRoad.rotation
    print(r_t, n_rt)

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

    roadpieces.append((x, y))

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

playerRoad = Road(RED, 32, 32)
playerRoad.rect.x = 168
playerRoad.rect.y = 288
playerRoad.rotate(270)
sprites_list.add(playerRoad)


playerHighlight = Highlight()
playerHighlight.rect.x = 168
playerHighlight.rect.y = 288
playerHighlight.rotate(270)
sprites_list.add(playerHighlight)

background = Background()
background.rect.x = -1
sprites_list.add(background)

roadpieces = []
b1 = (200, 0)
b2 = (776, 576)

def boundChecker(tl, br, xchange=0, ychange=0):
    x, y = tl
    x_, y_ = br
    b1_x, b1_y = b1
    b2_x, b2_y = b2
    xy = (x+xchange, y+ychange)
    if xy in roadpieces:
        return False
    elif x+xchange < b1_x or y+ychange < b1_y or x_+xchange > b2_x or y_+ychange > b2_y:
        return False
    else:
        return True

while runGame:

    menu.kill()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runGame = False
        elif event.type == pygame.KEYDOWN:

            c_rt = playerRoad.rotation

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

    screen.fill(BLACK)

    # Listens for keyboard inputs

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
