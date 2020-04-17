import pygame
import time
import random

pygame.init()
width = 800
hight = 600
gamedisplay = pygame.display.set_mode((width, hight))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
block_size = 10
bullet_block_size = 10
fps = pygame.time.Clock()
score = 0


def snake(block_size, snakelist):
    for xny in snakelist:
        # xny[0] and xny[1] are x and y coordinates respectively of left top corner of rectangle.
        pygame.draw.rect(gamedisplay, green, [xny[0], xny[1], block_size, block_size])


def bullet(bullet_block_size, x, y):
    pygame.draw.rect(gamedisplay, black, [x, y, bullet_block_size, bullet_block_size])


font = pygame.font.SysFont(None, 25)


def message(msj, score, color):
    screen_text = font.render(msj, True, color)
    score_text = font.render(score, True, color)
    gamedisplay.blit(screen_text, [width / 2, hight / 2])
    gamedisplay.blit(score_text, [width / 2, hight / 1.7])


def game_score(score, color):
    screen_text = font.render(str(score), True, color)
    gamedisplay.blit(screen_text, [10, 10])
    pygame.display.flip()


def gameloop(score):
    gameexit = False
    gameover = False
    bullet_fire = False
    x = width / 2
    y = hight / 2
    x_change = 0
    y_change = 0
    bullet_x_change = 0
    bullet_y_change = 0
    snakelist = []
    snakelength = 1
    applex = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    appley = round(random.randrange(0, hight - block_size) / 10.0) * 10.0
    while not gameexit:
        while gameover == True:
            gamedisplay.fill(white)
            message("do you want to continue : C or Quit : Q", "Your Score: " + str(score), red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    elif event.key == pygame.K_c:
                        score = 0
                        gameloop(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = +block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = +block_size
                    x_change = 0
                elif event.key == pygame.K_SPACE:
                    bullet_fire = True
                    bullet_y_change = y_change
                    bullet_x_change = x_change

        if x < 0 or x >= width or y < 0 or y >= hight:
            gameover = True

        x += x_change
        y += y_change

        if not bullet_fire:
            bullet_x = x
            bullet_y = y

        bullet_x += 1 * bullet_x_change
        bullet_y += 1* bullet_y_change

        if bullet_x <= 0:
            bullet_x = width
        elif bullet_x >= width:
            bullet_x = 0
        elif bullet_y == 0:
            bullet_y = hight
        elif bullet_y >= hight:
            bullet_y = 0

        gamedisplay.fill(white)
        pygame.draw.rect(gamedisplay, red, [applex, appley, block_size, block_size])
        snakehead = []
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]

        """Below code is for snake don't bite himself"""
        # for eachsegment in snakelist[:-1]:
        #     if eachsegment == snakehead:
        #         gameover = True

        game_score(score, black)
        snake(block_size, snakelist)
        bullet(bullet_block_size, bullet_x, bullet_y)
        pygame.display.update()
        if bullet_x == applex and bullet_y == appley and bullet_fire == True:
            applex = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            appley = round(random.randrange(0, hight - block_size) / 10.0) * 10.0
            snakelength += 1
            score += 1
        fps.tick(25)

    pygame.quit()
    quit()


gameloop(score)
