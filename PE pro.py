import pygame
import math
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 700))
background = pygame.image.load('backgroundblack.png')
mixer.music.load('music.wav')
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders (1).png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('space-invaders (1).png')
playerX = 380
playerY = 600
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

enemy2img = pygame.image.load('space-ship.png')
enemy2X = random.randint(0, 735)
enemy2Y = random.randint(20, 150)
enemy2X_change = 2.5
enemy2Y_change = 0

bossimg = pygame.image.load('Boss.png')
bossX = 250
bossY = 30

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy2.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(20, 150))
    enemyX_change.append(3)
    enemyY_change.append(60)

bullet1Img = pygame.image.load('bullet.png')
bullet1X = 0
bullet1Y = 606
bullet1X_change = 0
bullet1Y_change = 10
bullet1_state = "ready"

bullet2Img = pygame.image.load('bullet.png')
bullet2X = 0
bullet2Y = 606
bullet2X_change = 0
bullet2Y_change = 10
bullet2_state = "ready"

laser = pygame.image.load('laser.png')
laserX = enemy2X
laserY = enemy2Y
laserX_change = 0
laserY_change = -6
laser_state = "ready"

laser2img = pygame.image.load('laser2.png')
laser2X = bossX
laser2Y = bossY
laser2X_change = 0
laser2Y_change = -4
laser2_state = "ready"

rocketimg = pygame.image.load('missile.png')
rocketX = playerX
rocketY = bossY
rocketX_change = 0
rocketY_change = -3
rocket_state = "ready"

laser2_2img = pygame.image.load('laser2.png')
laser2_2X = bossX
laser2_2Y = bossY
laser2_2X_change = 3
laser2_2Y_change = -4
laser2_2_state = "ready"

laser2_3img = pygame.image.load('laser2.png')
laser2_3X = bossX
laser2_3Y = bossY
laser2_3X_change = 5
laser2_3Y_change = -4
laser2_3_state = "ready"

laser2_4img = pygame.image.load('laser2.png')
laser2_4X = bossX
laser2_4Y = bossY
laser2_4X_change = -3
laser2_4Y_change = -4
laser2_4_state = "ready"

laser2_5img = pygame.image.load('laser2.png')
laser2_5X = bossX
laser2_5Y = bossY
laser2_5X_change = -5
laser2_5Y_change = -4
laser2_5_state = "ready"

score_value = 0
font = pygame.font.Font('Pixeltype.ttf', 60)

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 100)


def score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(score_value):
    if 0 <= score_value <= 300:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (300, 350))


def win(score_value):
    if score_value >= 120:
        win1 = font.render("YOU WIN", True, (127, 0, 255))
        screen.blit(win1, (300, 350))
        for j in range(num_of_enemies):
            enemyY[j] = 2000


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def enemy2(x, y):
    screen.blit(enemy2img, (x, y))


def fire_bullet1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1Img, (x - 12, y))


def fire_bullet2(x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (x + 49, y))


def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laser, (x - 20, y))


def Boss(x, y):
    if score_value >= 64:
        screen.blit(bossimg, (x, y))


def laser2(x, y):
    if score_value >= 64:
        global laser2_state
        laser2_state = "fire"
        screen.blit(laser2img, (x + 140, y + 272))


def laser2_2(x, y):
    if score_value >= 64:
        global laser2_2_state
        laser2_2_state = "fire"
        screen.blit(laser2_2img, (x + 140, y + 272))


def laser2_3(x, y):
    if score_value >= 64:
        global laser2_3_state
        laser2_3_state = "fire"
        screen.blit(laser2_3img, (x + 140, y + 272))


def laser2_4(x, y):
    if score_value >= 64:
        global laser2_4_state
        laser2_4_state = "fire"
        screen.blit(laser2_4img, (x + 140, y + 272))


def laser2_5(x, y):
    if score_value >= 64:
        global laser2_5_state
        laser2_5_state = "fire"
        screen.blit(laser2_5img, (x + 140, y + 272))


def rocket(x, y):
    if score_value >= 64:
        global rocket_state
        rocket_state = "fire"
        screen.blit(rocketimg, (x, y + 272))


def remove(enemyX, enemyX_change, enemyY_change):
    for j in range(num_of_enemies):
        enemyX[j] = 2000
        enemyX_change[j] = 0
        enemyY_change[j] = 0


def iscollision1(enemyX, enemyY, bullet1X, bullet1Y):
    distance1 = math.sqrt((math.pow(enemyX - bullet1X, 2)) + (math.pow(enemyY - bullet1Y, 2)))
    if distance1 < 60:
        return True
    else:
        return False


def iscollision3(enemyX, enemyY, playerX, playerY):
    distance3 = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance3 < 80:
        return True
    else:
        return False


def iscollision4(laserX, laserY, playerX, playerY):
    distance4 = math.sqrt((math.pow(laserX - playerX, 2)) + (math.pow(laserY - playerY, 2)))
    if distance4 < 40:
        return True
    else:
        return False


def iscollision5(enemy2X, enemy2Y, bullet1X, bullet1Y):
    distance5 = math.sqrt((math.pow(enemy2X - bullet1X, 2)) + (math.pow(enemy2Y - bullet1Y, 2)))
    if distance5 < 60:
        return True
    else:
        return False



def iscollision7(playerX, playerY, laser2X, laser2Y):
    distance7 = math.sqrt((math.pow(playerX - (laser2X + 126), 2)) + (math.pow(playerY - (laser2Y + 268), 2)))
    if distance7 < 30:
        return True
    else:
        return False


def iscollision12(bossX, bossY, bullet1X, bullet1Y):
    distance12 = math.sqrt((math.pow((bossX + 120) - bullet1X, 2)) + (math.pow(bossY - (bullet1Y - 200), 2)))
    if distance12 < 110:
        return True
    else:
        return False

def iscollision14(playerX, playerY, rocketX, rocketY):
    distance14 = math.sqrt((math.pow((playerX) - (rocketX), 2)) + (math.pow((playerY) - (rocketY + 300), 2)))
    if distance14 < 40:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = +4
            if event.key == pygame.K_SPACE:
                if bullet1_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bullet1X = playerX
                    fire_bullet1(bullet1X, bullet1Y)
            if event.key == pygame.K_SPACE:
                if bullet2_state == "ready":
                    bullet2X = playerX
                    fire_bullet2(bullet2X, bullet2Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    laserX = enemy2X
                    fire_laser(laserX, laserY)
                if laser2_state == "ready":
                    laser2X = bossX
                    laser2(laser2X, laser2Y)
                if laser2_2_state == "ready":
                    laser2_2X = bossX
                    laser2_2(laser2_2X, laser2_2Y)
                if laser2_3_state == "ready":
                    laser2_3X = bossX
                    laser2_3(laser2_3X, laser2_3Y)
                if laser2_4_state == "ready":
                    laser2_4X = bossX
                    laser2_4(laser2_4X, laser2_4Y)
                if laser2_5_state == "ready":
                    laser2_5X = bossX
                    laser2_5(laser2_5X, laser2_5Y)
                if rocket_state == "ready":
                    rocketX = playerX
                    rocket(rocketX, rocketY)

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        if enemyY[i] > 650:
            for j in range(num_of_enemies):
                enemyX[j] = 2000
            playerX = 3000
            enemy2X = 2000
            laserX = 4000
            game_over_text(score_value)
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2.5
            enemyY[i] += enemyY_change[i]

        collision1 = iscollision1(enemyX[i], enemyY[i], bullet1X, bullet1Y)
        collision2 = iscollision1(enemyX[i], enemyY[i], bullet2X, bullet2Y)

        if collision1:
            bullet1Y = 606
            bullet1_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(20, 150)
        if collision2:
            bullet2Y = 606
            bullet2_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(20, 150)

        collision3 = iscollision3(enemyX[i], enemyY[i], playerX, playerY)
        if collision3:
            for j in range(num_of_enemies):
                enemyX[j] = 2000
            enemy2X = 2000
            playerX = 3000
            laserX = 4000
            game_over_text(score_value)
            break

        enemy(enemyX[i], enemyY[i], i)

    collision4 = iscollision4(laserX, laserY, playerX, playerY)
    if collision4:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        game_over_text(score_value)

    collision5 = iscollision5(enemy2X, enemy2Y, bullet1X, bullet1Y)
    if collision5:
        bullet1Y = 606
        bullet1_state = "ready"
        score_value += 1
        enemy2X = random.randint(0, 735)
        enemy2Y = random.randint(20, 150)

    collision6 = iscollision5(enemy2X, enemy2Y, bullet2X, bullet2Y)
    if collision6:
        bullet2Y = 606
        bullet2_state = "ready"
        score_value += 1
        enemy2X = random.randint(0, 735)
        enemy2Y = random.randint(20, 150)

    collision7 = iscollision7(playerX, playerY, laser2X, laser2Y)
    if collision7:
        game_over_text(score_value)
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        bossX = 4000
        laser2X = 4000
        laser2_2X = 4000
        laser2_3X = 4000
        laser2_4X = 4000
        laser2_5X = 4000
        rocketX = 4000

    collision8 = iscollision7(playerX, playerY, laser2_2X, laser2_2Y)
    if collision8:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        bossX = 4000
        laser2X = 4000
        laser2_2X = 4000
        laser2_3X = 4000
        laser2_4X = 4000
        laser2_5X = 4000
        rocketX = 4000
        game_over_text(score_value)

    collision9 = iscollision7(playerX, playerY, laser2_3X, laser2_3Y)
    if collision9:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        bossX = 4000
        laser2X = 4000
        laser2_2X = 4000
        laser2_3X = 4000
        laser2_4X = 4000
        laser2_5X = 4000
        rocketX = 4000
        game_over_text(score_value)

    collision10 = iscollision7(playerX, playerY, laser2_4X, laser2_4Y)
    if collision10:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        bossX = 4000
        laser2X = 4000
        laser2_2X = 4000
        laser2_3X = 4000
        laser2_4X = 4000
        laser2_5X = 4000
        rocketX = 4000
        game_over_text(score_value)

    collision11 = iscollision7(playerX, playerY, laser2_5X, laser2_5Y)
    if collision11:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        bossX = 4000
        laser2X = 4000
        laser2_2X = 4000
        laser2_3X = 4000
        laser2_4X = 4000
        laser2_5X = 4000
        rocketX = 4000
        game_over_text(score_value)

    collision12 = iscollision12(bossX, bossY, bullet1X, bullet1Y)
    if score_value >= 64:
        if collision12:
            bullet1Y = 606
            bullet1_state = "ready"
            score_value += 2

    collision13 = iscollision12(bossX, bossY, bullet2X, bullet2Y)
    if score_value >= 64:
        if collision13:
            bullet2Y = 606
            bullet2_state = "ready"
            score_value += 2

    collision14 = iscollision14(playerX, playerY, rocketX, rocketY)
    if collision14:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        laserX = 4000
        playerX = 3000
        enemy2X = 2000
        bossX = 4000
        laser2X = 4000
        laser2_2X = 4000
        laser2_3X = 4000
        laser2_4X = 4000
        laser2_5X = 4000
        rocketX = 4000
        game_over_text(score_value)

    if score_value >= 10:
        enemy2(enemy2X, enemy2Y)
        enemy2X += enemy2X_change
        if laser_state == "fire":
            fire_laser(laserX, laserY)
            laserY -= laserY_change

        if laserY >= 800:
            laserY = enemy2Y
            laserX = enemy2X

        if enemy2X <= 0:
            enemy2X_change = 3
            enemy2Y += enemy2Y_change
        elif enemy2X >= 736:
            enemy2X_change = -3
            enemy2Y += enemy2Y_change

    Boss(bossX, bossY)
    if score_value >= 64:
        remove(enemyX, enemyX_change, enemyY_change)
        enemy2X = 2000
        enemy2X_change = 0

    if laser2_state == "fire":
        laser2(laser2X, laser2Y)
        laser2X += laser2X_change
        laser2Y -= laser2Y_change
    if laser2Y >= 600:
        laser2Y = bossY
        laser2X = bossX

    if laser2_2_state == "fire":
        laser2_2(laser2_2X, laser2_2Y)
        laser2_2X += laser2_2X_change
        laser2_2Y -= laser2_2Y_change
    if laser2_2Y >= 600:
        laser2_2Y = bossY
        laser2_2X = bossX

    if laser2_3_state == "fire":
        laser2_3(laser2_3X, laser2_3Y)
        laser2_3X += laser2_3X_change
        laser2_3Y -= laser2_3Y_change
    if laser2_3Y >= 600:
        laser2_3Y = bossY
        laser2_3X = bossX

    if laser2_4_state == "fire":
        laser2_4(laser2_4X, laser2_4Y)
        laser2_4X += laser2_4X_change
        laser2_4Y -= laser2_4Y_change
    if laser2_4Y >= 600:
        laser2_4Y = bossY
        laser2_4X = bossX

    if laser2_5_state == "fire":
        laser2_5(laser2_5X, laser2_5Y)
        laser2_5X += laser2_5X_change
        laser2_5Y -= laser2_5Y_change
    if laser2_5Y >= 600:
        laser2_5Y = bossY
        laser2_5X = bossX

    if rocket_state == "fire":
        if rocketY <= 200:
            rocketX += playerX_change
            rocketY -= rocketY_change
            rocket(rocketX, rocketY)
        elif rocketY > 200:
            rocketX += rocketX_change
            rocketY -= rocketY_change
            rocket(rocketX, rocketY)

    if rocketY >= 600:
        rocketY = bossY
        rocketX = playerX

    if bullet1Y <= 0:
        bullet1Y = 606
        bullet1_state = "ready"

    if bullet1_state == "fire":
        fire_bullet1(bullet1X, bullet1Y)
        bullet1Y -= bullet1Y_change

    if bullet2Y <= 0:
        bullet2Y = 606
        bullet2_state = "ready"

    if bullet2_state == "fire":
        fire_bullet2(bullet2X, bullet2Y)
        bullet2Y -= bullet2Y_change

    WW = win(score_value)
    if score_value >= 120:
        bossX = 4000
        rocketX = 4000

    player(playerX, playerY)
    score(textX, textY)
    pygame.display.update()
