import sys
import random

import pygame

pygame.init()

size = width, height = 320, 288
screen = pygame.display.set_mode(size)

maze = [
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 2, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

squares = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0)
]
block = pygame.Rect(0, 0, 32, 32)

player_pos = (2, 0)
player_color = (0, 0, 255)


def draw_maze():
    for x in range(0, 10):
        for y in range(0, 9):
            square = maze[y][x]
            block.right = (x+1) * block.width
            block.top = y * block.height
            pygame.draw.rect(screen, squares[square], block)


def draw_player():
    pos = (
        int(player_pos[0] * block.width + block.width/2),
        int(player_pos[1] * block.height + block.height/2)
    )
    pygame.draw.circle(screen, player_color, pos, 16, 0)


def move_player():
    global player_pos
    nx = player_pos[0]
    ny = player_pos[1]
    if pygame.key.get_pressed()[pygame.K_UP]:
        ny -= 1
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        ny += 1
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        nx -= 1
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        nx += 1
    if nx >= 0 and ny >= 0 and nx < 10 and ny < 9:
        if maze[ny][nx] != 1:
            player_pos = (nx, ny)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    move_player()
    if maze[player_pos[1]][player_pos[0]] == 2:
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            screen.fill(color)
            pygame.time.wait(100)
            pygame.display.flip()

    screen.fill((0, 0, 0))
    draw_maze()
    draw_player()
    pygame.display.flip()
    pygame.time.wait(120)
