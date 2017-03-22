from Game import *
from Colors import *
from Classes import *
from Levels import *

import pygame
import os






def display(screen,buttons):

    #background
    screen.fill(background_color)

    #title
    title_img = title_font.render("Arithma", True, grid_color)
    screen.blit(title_img, (800/2-title_img.get_width()/2,600/2-title_img.get_height()/2-200))    #auto center text

    #outline
    pygame.draw.rect(screen, grid_color, pygame.Rect(0,0,800-1,600-1), 4)  #'-1' fixes bottom and right edge alignment

##    #button box - MAYBE?
##    pygame.draw.rect(screen,grid_color, Rect(240, 190, 320, 340), 2)

    #buttons
    for button in buttons:
        screen.blit(button.get_image(),(button.x,button.y))

    pygame.display.update()

    
    


def home_screen():

    #set up screen
    pygame.init()
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Arithma")

    #define buttons
    buttons = [
        Button(250, 200, 300, 100, grid_color, piece_color,  piece_font, "Levels", "L"),
        Button(250, 310, 300, 100, grid_color, piece_color, piece_font, "Settings", "S"),
        Button(250, 420, 145, 100, grid_color, piece_color, piece_font, "Credits", "C"),
        Button(405, 420, 145, 100, grid_color, piece_color, piece_font, "Quit", "Q")
    ]
    
##    #hover scale demo
##    buttons[0].hover = 0
##    buttons[1].hover = 1
##    buttons[2].hover = 2
##    buttons[3].hover = 3

    #display screen initially
    display(screen,buttons)

    #control loop
    done = False
    while not done:

        #user input
        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return

            #down button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                   if button.rect.collidepoint(event.pos):
                       button.hover = 3
                       display(screen, buttons)

            #up button
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in buttons:
                    if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        display(screen, buttons)
                        #programmatic control
                        if button.key == "L":
                            print "levels"
                            level_screen(screen)
                            pygame.display.quit()
                            return
                        elif button.key == "S":
                            print "settings"
                            settings_screen(screen)
                            pygame.display.quit()
                        elif button.key == "C":
                            print "credits"
                            credits_screen(screen)
                            pygame.display.quit()
                            return
                        elif button.key == "Q":
                            pygame.display.quit()
                            return
                            
        #hover shading
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos) and button.hover == 0:
                button.hover = 1
                display(screen, buttons)
            elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                button.hover = 0
                display(screen, buttons)
                    






def level_screen(screen):
    screen.fill(white)

    buttons = [Button(350, 500, 100, 75, grid_color, piece_color,  piece_font, "Back", "B")]
    for n in range(len(Levels)):
        buttons.append(Button(75+(n%6)*110, 100+int(n/6.0)*110, 100, 100, grid_color, piece_color, piece_font, str(n+1), n))

    def display(screen):
        screen.fill(white)

        #outline
        pygame.draw.rect(screen, grid_color, pygame.Rect(0,0,800-1,600-1), 4)  #'-1' fixes bottom and right edge alignment

        #title
        title_img = title_font.render("Levels", True, grid_color)
        screen.blit(title_img, (800/2-title_img.get_width()/2,600/2-title_img.get_height()/2-250))    #auto center text

        for button in buttons:
            screen.blit(button.get_image(), (button.x,button.y))

        pygame.display.update()



    display(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                   if button.rect.collidepoint(event.pos):
                       button.hover = 3
                       display(screen)

            elif event.type == pygame.MOUSEBUTTONUP:
                for button in buttons:
                    if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        display(screen)
                        if button.key == "B":
                            home_screen()
                        else:
                            main(screen, button.key)
                            display(screen)
                


        #hover shading
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos) and button.hover == 0:
                button.hover = 1
                display(screen)
            elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                button.hover = 0
                display(screen)

        



def settings_screen(screen):
    screen.fill(white)

    buttons = [
        Button(20, 505, 100, 75, grid_color, piece_color,  piece_font, "Back", "B")
    ]

    selected = False
    
    sliders = [
        Slider((200,200), 200, 100, grid_color, background_color)
    ]

    def display(screen, buttons, sliders):
        screen.fill(white)

        #title
        title_img = title_font.render("Settings", True, grid_color)
        screen.blit(title_img, (800/2-title_img.get_width()/2,600/2-title_img.get_height()/2-250))    #auto center text

        #buttons
        for button in buttons:
            screen.blit(button.get_image(), (button.x,button.y))

        #sliders
        for slider in sliders:
            screen.blit(slider.get_image(), slider.start)
            pygame.draw.rect(screen, black, slider.get_rect(), 2)      #draw bounding rect

        pygame.display.update()


    display(screen, buttons, sliders)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            elif event.type == MOUSEBUTTONDOWN:
                    for button in buttons:
                       if button.rect.collidepoint(event.pos):
                           button.hover = 3
                           display(screen, buttons, sliders)
                    for slider in sliders:
                        if slider.get_rect().collidepoint(event.pos):
                            selected = slider

            elif event.type == MOUSEBUTTONUP:
                for button in buttons:
                    if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        display(screen, buttons, sliders)
                        if button.key == "B":
                            home_screen()
                if selected != False:
                    selected = False
                


        #hover shading
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos) and button.hover == 0:
                button.hover = 1
                display(screen, buttons, sliders)
            elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                button.hover = 0
                display(screen, buttons, sliders)


        #move slider
        if selected != False:
            pos = pygame.mouse.get_pos()
            if pos[0] > selected.start[0] and pos[0] < selected.end[0]:
                selected.x = pos[0] - selected.start[0]
                display(screen, buttons, sliders)

        



def credits_screen(screen):
    screen.fill(white)
    
    text_img_0 = credits_font.render("Howard High School Coding Club", True, black)
    text_img_1 = credits_font.render("By Russell Schwartz and Micah Johnson", True, black)
    text_img_2 = credits_font.render("December 2015", True, black)

    buttons = [
        Button(350, 300, 100, 75, grid_color, piece_color,  credits_font, "Back", "B")
    ]

    def display(screen):
        screen.fill(white)
        
        screen.blit(text_img_0,(800/2-text_img_0.get_width()/2,100))
        screen.blit(text_img_1,(800/2-text_img_1.get_width()/2,150))
        screen.blit(text_img_2,(800/2-text_img_2.get_width()/2,200))

        for button in buttons:
            screen.blit(button.get_image(), (button.x,button.y))
        
        pygame.display.update()

    
    display(screen)
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            elif event.type == MOUSEBUTTONDOWN:
                for button in buttons:
                   if button.rect.collidepoint(event.pos):
                       button.hover = 3
                       display(screen)

            elif event.type == MOUSEBUTTONUP:
                for button in buttons:
                    if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        display(screen)
                        if button.key == "B":
                            home_screen()
                


        #hover shading
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos) and button.hover == 0:
                button.hover = 1
                display(screen)
            elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                button.hover = 0
                display(screen)
    












#home_screen()

