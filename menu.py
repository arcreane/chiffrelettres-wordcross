
import pygame
import pygame_menu
import board

pygame.init()
surface = pygame.display.set_mode((1200, 1200))


# Display of the levels difficulties options
def start_the_game(Name):
    player_input = f"Quelle est ton nom : f'{input(Name)}"
    Name = player_input
    pass


def set_difficulty():
    if ('Easy' == 1):
        board.board_easy()
    if ('Medium' == 2):
        board.board_medium()
    if ('Hard' == 3):
        board.board_hard()



def board_score():
    pass


menu = pygame_menu.Menu('Welcome on WordCross', 500, 500, theme=pygame_menu.themes.THEME_ORANGE)
menu.add.text_input('Name :', default=' ')
menu.add.button('Play', start_the_game)
menu.add.dropselect('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add.button('Score', board_score)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.center_content()

menu.mainloop(surface)
