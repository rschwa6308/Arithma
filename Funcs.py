#game funcs
import pygame

from Colors import *


def display(screen, pieces, buttons):
    width = screen.get_width()
    height = screen.get_height()

    g_width = (width-200)/10
    g_height = height/10

    #clear screen
    screen.fill(background_color)
    
    #draw grid
    for y in range(10):
        pygame.draw.line(screen, grid_color, (0,y*g_height), (width-200,y*g_height))
    for x in range(10):
        pygame.draw.line(screen, grid_color, (x*g_width,0), (x*g_width,height))

    #draw border and partitions
    pygame.draw.rect(screen, grid_color, pygame.Rect(0,0,width-1,height-1), 4)
    pygame.draw.line(screen, grid_color, (width-200,0), (width-200,height), 2)
    #pygame.draw.line(screen, grid_color, (600,480), (800,480), 2)
    
    #draw pieces
    for piece in pieces:
        #print piece.get_pos()
        screen.blit(piece.image, piece.pos)

    #draw buttons
    for button in buttons:
        screen.blit(button.get_image(), (button.x,button.y))

    #flip display
    pygame.display.update()

    
