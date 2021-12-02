# import pygame
#
# import time
#
#
# clock = pygame.time.Clock()
#
#
#
# blue_color = (0,75,255)
# red_color = (255,0,0)
# res = (400,400)
#
# pygame.init()
#
# window_surface = pygame.display.set_mode(res)
# window_surface.fill(blue_color)
# pygame.display.set_caption("Timer")
# pygame.display.update()
#
#  #timer
#
#
#
#
#
# launched = True
#
# while launched :
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             launched = False
#
#

import pygame
import pygame.freetype

def main():
    pygame.init()
    screen=pygame.display.set_mode((400, 300))
    clock=pygame.time.Clock()
    font=pygame.freetype.SysFont(None, 34)
    font.origin=True
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return
        screen.fill(pygame.Color('white'))
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes,seconds=seconds, millis=millis )
        font.render_to(screen, (100, 100), out, pygame.Color('red'))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__': main()