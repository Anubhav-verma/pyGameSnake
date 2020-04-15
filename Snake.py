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
fps = pygame.time.Clock()
score = 0

def snake(block_size, snakelist):
    for xny in snakelist:
        pygame.draw.rect(gamedisplay, green, [xny[0], xny[1], block_size, block_size])


font = pygame.font.SysFont(None, 25)


def message(msj, color):
    screen_text = font.render(msj, True, color)
    gamedisplay.blit(screen_text, [width / 2, hight / 2])

def game_score(score, color):
    screen_text = font.render(str(score), True, color)
    gamedisplay.blit(screen_text, [10, 10])
    pygame.display.flip()

def gameloop(score):
    gameexit = False
    gameover = False
    x = width / 2
    y = hight / 2
    x_change = 0
    y_change = 0
    snakelist = []
    snakelength = 1
    applex = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    appley = round(random.randrange(0, hight - block_size) / 10.0) * 10.0
    while not gameexit:
        while gameover == True:
            gamedisplay.fill(white)
            message("do you want to continue : C or Quit : Q", red)
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
                gsmeexit = True
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
        if x < 0 or x >= width or y < 0 or y >= hight:
            gameover = True

        x += x_change
        y += y_change
        gamedisplay.fill(white)
        pygame.draw.rect(gamedisplay, red, [applex, appley, block_size, block_size])
        snakehead = []
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameover = True
        game_score(score, black)
        snake(block_size, snakelist)
        pygame.display.update()
        if x == applex and y == appley:
            applex = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            appley = round(random.randrange(0, hight - block_size) / 10.0) * 10.0
            snakelength += 1
            score += 1
        fps.tick(25)

    pygame.quit()
    quit()


gameloop(score)

