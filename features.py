import pygame
import random

pygame.init()
running = True
screen = pygame.display.set_mode([500, 500])
# font = pygame.font.Font('freesansbold.ttf', 32)
# textX = 10
# textY = 10


def import_library():
    # Get liste_francais.txt and pass it througt a Python list named library

    extract = open("liste_francais.txt")
    library = extract.readlines()

    library = list(map(lambda st: str.replace(st, "?", "é"), library))

    random_words_library(library)


def random_words_library(extracted_list):
    i = 0
    word_list = []
    while i < 4:  # difficulté select

        i += 1

        word = random.choice(extracted_list).split()
        word_list.extend([word])

        print(word)

    # print(word_list)
    print(len(word_list))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()


# def showWords(x, y):
#     text = font.render("Hello", True, (0, 0, 0))
#     screen.blit(text, (x, y))


pygame.quit()




# to draw a line on board
def draw_line():
    pass


# to cross a words of the list word
def cross_words():
    pass