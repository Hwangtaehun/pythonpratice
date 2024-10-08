import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMES = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()

def num_of_bomb(field, x_pos, y_pos):
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    
    return count

def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return
    
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)

def main():
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!", True, (0, 255, 255))
    message_over = largefont.render("!!GAME OVER!!", True, (0, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)
    game_over = False

    field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

    count = 0
    while count < NUM_OF_BOMES:
        xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1
        
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE)

                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field, xpos, ypos)
            
            SURFACE.fill((0, 0, 0))
            for ypos in range(HEIGHT):
                for xpos in range(WIDTH):
                    tile = field[ypos][xpos]
                    rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                    if tile == EMPTY or tile == BOMB:
                        pygame.draw.rect(SURFACE, (192, 192, 192), rect)
                        if game_over and tile == BOMB:
                            pygame.draw.ellipse(SURFACE, (255, 255, 0), rect)
                    elif tile == OPENED:
                        count = num_of_bomb(field, xpos, ypos)
                        if count > 0:
                            num_image = smallfont.render("{}".format(count), True, (255, 255, 0))
                            SURFACE.blit(num_image, (xpos * SIZE + 10, ypos * SIZE + 10))
                
                for index in range(0, WIDTH * SIZE, SIZE):
                    pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT * SIZE))

                for index in range(0, HEIGHT * SIZE, SIZE):
                    pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH * SIZE, index))

                if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMES:
                    SURFACE.blit(message_clear, message_rect.topleft)
                elif game_over:
                    SURFACE.blit(message_over, message_rect.topleft)
                
                pygame.display.update()
    
if __name__ == '__main__':
    main()