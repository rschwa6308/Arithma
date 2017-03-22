#math puzzler

import pygame
from pygame import *
from random import *

from Classes import *
from Funcs import *
from Check import *
from Levels import *
from Menu import *



#takes a list of pieces and grid coordinates and returns piece instance
def get_piece(pieces, coords):
    for piece in pieces:
        if piece.grid == coords:
            return piece 
    return False



def overlay(screen, buttons, level):
    #box
    box = pygame.Surface((300,400))
    box.fill(white)

    #border
    pygame.draw.rect(box, grid_color, pygame.Rect(0,0,299,399),2)

    #heading
    head_img = piece_font.render("Correct!",True,grid_color)
    box.blit(head_img, (box.get_width()/2-head_img.get_width()/2,box.get_height()/2-head_img.get_height()/2-150))

    #message
    mess_img_0 = credits_font.render("You beat level " + str(level+1) + ".", True, grid_color)
    mess_img_1 = credits_font.render("Great work!",True,grid_color)
    box.blit(mess_img_0, (box.get_width()/2-mess_img_0.get_width()/2,box.get_height()/2-mess_img_0.get_height()/2-75))
    box.blit(mess_img_1, (box.get_width()/2-mess_img_1.get_width()/2,box.get_height()/2-mess_img_1.get_height()/2-50))

    #buttons
    for button in buttons:
        box.blit(button.get_image(), (button.x,button.y))
        
    #blit box to screen
    screen.blit(box,(250,100))
    
    #flip display
    pygame.display.update()







#main() takes screen and a level index
def main(screen, level):

    #set up screen
    s_w = 800
    s_h = 600
    
    #set window caption
    pygame.display.set_caption("Level " + str(level+1))


    #init pieces (build from level)
    pieces = []
    for l in Levels[level]:   #load in level
        pieces.append(Piece(l[0],l[1]))
        

    #init buttons
    buttons = [
        Button(610,495,180,40, grid_color, piece_color, button_font, "Check","C"),
        Button(610,545,180,40, grid_color, piece_color, button_font, "Home","H")
    ]


    #show board 
    display(screen, pieces, buttons)
    
    
    #init selected var
    selected = False


    #set up clock
    clock = pygame.time.Clock()
    clock.tick(60)


    #game loop
    done = False
    
    while not done:
        
        #user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                done = True

            #run check algorithm
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if check(pieces) or True:
                        print "success!!!"
                        overlay(screen)
                    else:
                        print "failure!!!"

            #select (pick up) piece
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = mouse.get_pos()
                    pos = (int(pos[0]/60),int(pos[1]/60))
                    selected = get_piece(pieces, pos)
                for button in buttons:
                   if button.rect.collidepoint(event.pos):
                       button.hover = 3
                       display(screen, pieces, buttons)

            #deselect (place) piece       
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    pos = mouse.get_pos()
                    pos = (int(pos[0]/60),int(pos[1]/60))
                    if selected != False:
                        if pos[0] > 12 or pos[1] > 9 or (pos[0] >= 10 and pos[1] >= 8):   #check if outside acceptable range
                            pass
                        elif get_piece(pieces, pos) == False or get_piece(pieces, pos) == selected:         #center
                            selected.grid = pos
                        else:
                            delta_x = 1
                            delta_y = 0
                            tries = 0
                            while get_piece(pieces, (pos[0]+delta_x,pos[1]+delta_y)) != False and tries <= 100 or (pos[0]+delta_x > 12 or pos[1]+delta_y > 9 or (pos[0]+delta_x >= 10 and pos[1]+delta_y >= 8)):
                                delta_x = randint(-1,1)
                                delta_y = randint(-1,1)
                                tries += 1
                                print (pos[0]+delta_x,pos[1]+delta_y)
                            if tries < 100:
                                selected.grid = (pos[0]+delta_x,pos[1]+delta_y)
                    
                        selected.pos = selected.get_pos()
                        display(screen, pieces, buttons)
                        selected = False
                        
                #button execution
                for button in buttons:
                    if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        display(screen, pieces, buttons)
                        if button.key == "H":
                            return
                        elif button.key == "C":
                            if check(pieces):
                                print "success!!!"

                                ###pop up window###
                                buttons = [
                                    Button(20,190,260,50, grid_color, piece_color, button_font, "Next Level","N"),
                                    Button(20,260,260,50, grid_color, piece_color, button_font, "Replay","R"),
                                    Button(20,330,260,50, grid_color, piece_color, button_font, "Home","H")
                                    
                                ]
                                overlay(screen, buttons, level)
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            return
                                        
                                        #down button
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            for button in buttons:
                                               if button.rect.collidepoint((event.pos[0]-250,event.pos[1]-100)):   #compensate for offset origin
                                                   button.hover = 3
                                                   overlay(screen, buttons, level)

                                        #up button
                                        elif event.type == pygame.MOUSEBUTTONUP:
                                            for button in buttons:
                                                if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                                                    button.hover = 0
                                                    overlay(screen, buttons, level)
                                                    #programmatic control
                                                    if button.key == "N":
                                                        main(screen, level+1)
                                                        return
                                                    elif button.key == "R":
                                                        print "restart"
                                                        main(screen, level)    #does not work!?!?!
                                                        return
                                                    elif button.key == "H":
                                                        return
                                                        
                                    #hover shading
                                    pos = (pygame.mouse.get_pos()[0]-250,pygame.mouse.get_pos()[1]-100)  #compensate for offset origin
                                    for button in buttons:
                                        if button.rect.collidepoint(pos) and button.hover == 0:
                                            button.hover = 1
                                            overlay(screen, buttons, level)
                                        elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                                            button.hover = 0
                                            overlay(screen, buttons, level)

                                        
                                        
                            else:
                                print "failure!!!"
                                #flash red
                                for i in range(2):
                                    button.color = red
                                    button.txt_color = red
                                    button.bg = background_color
                                    display(screen, pieces, buttons)
                                    pygame.time.wait(100)
                                    button.color = grid_color
                                    button.txt_color = piece_color
                                    button.bg = red
                                    display(screen, pieces, buttons)
                                    pygame.time.wait(100)
                                button.bg = white
                                button.color = grid_color
                                button.txt_color = piece_color
                                display(screen, pieces, buttons)


                       

            #update pos of selected piece         
            if selected != False:
                selected.pos = (mouse.get_pos()[0]-25,mouse.get_pos()[1]-25)
                display(screen, pieces, buttons)

            

            #hover shading
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos) and button.hover == 0:
                    button.hover = 1
                    display(screen, pieces, buttons)
                elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                    button.hover = 0
                    display(screen, pieces, buttons)
  






#main(L1)
