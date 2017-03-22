import pygame


#fonts
pygame.init()
piece_font = pygame.font.SysFont("verdana", 25)
title_font = pygame.font.SysFont("Dotum", 80)
title_font.set_underline(True)
credits_font = pygame.font.SysFont("Lucida Console", 20)
button_font = pygame.font.SysFont("verdana", 20)




#colors

black = (0,0,0)
white = (255,255,255)

blue = (84,155,255)
green =(128,255,0)
purple = (102,0,204)
red = (255,0,0)
yellow = (255,219,88)
brown = (139,69,19)


###worlds worst color scheme
##background_color = (255,0,0)
##grid_color = purple
##piece_color = brown            
##text_color = (0,255,255)

A = white
B = black


background_color = A         #A
grid_color = B              #B
piece_color = B             #B
text_color = A               #A
