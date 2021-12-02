import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
calc_board_width = screen_width / 2 * 3
calc_board_height = screen_height / 3 * 2
board = pygame.display.set_mode((calc_board_width, calc_board_height))
pygame.display.set_caption('WordCross')

# define variable
line_width = 4
markers = []
clicked = False
pos = []


# 7*7
def board_easy():
    bg = (255, 255, 255)
    grid = (60, 0, 60)
    board.fill(bg)
    for x in range(1, 7):
        pygame.draw.line(board, grid, (0, x * 142), (screen_width, x * 142), line_width)
        pygame.draw.line(board, grid, (x * 142, 0), (x * 142, screen_width), line_width)


for x in range(7):
    row = [0] * 7
    markers.append(row)

run = True
while run:
    board_easy()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False

# 10*10
def board_medium():
    bg = (255, 255, 255)
    grid = (60, 0, 60)
    board.fill(bg)
    for x in range(1, 10):
        pygame.draw.line(board, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(board, grid, (x * 100, 0), (x * 100, screen_width), line_width)


for x in range(10):
    row = [0] * 10
    markers.append(row)

run = True
while run:
    board_medium()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False

# 15*15
def board_hard():
    bg = (255, 255, 255)
    grid = (60, 0, 60)
    board.fill(bg)
    for x in range(1, 15):
        pygame.draw.line(board, grid, (0, x * 66), (screen_width, x * 66), line_width)
        pygame.draw.line(board, grid, (x * 66, 0), (x * 66, screen_width), line_width)


for x in range(15):
    row = [0] * 15
    markers.append(row)

run = True
while run:
    board_hard()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False

# add words by random
def word():
    pass


def list_word_right():
    pass

pygame.quit()
