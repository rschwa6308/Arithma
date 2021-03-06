# math puzzler

import pygame
from pygame import *
from random import *

from Classes import *
# from Funcs import *
from Check import *
from Levels import *
from Menu import *


# takes a list of pieces and grid coordinates and returns piece instance
def get_piece(pieces, coords):
    for piece in pieces:
        if piece.grid == coords:
            return piece
    return False


# takes a level number and returns a list of pieces
def load_level(level_num):
    pieces = []
    for p in Levels[level_num]:  # load in level
        if isinstance(p[0], str) and p[0][0] == "N":
            size = int(p[0][1:])
            pieces.append(NestedPiece(size, p[1], locked=p[1][0] < 10))
        else:
            pieces.append(Piece(p[0], p[1], locked=p[1][0] < 10))
    return pieces


def overlay(screen, buttons, level):
    # box
    box = pygame.Surface((300, 400))
    box.fill(white)

    # border
    pygame.draw.rect(box, grid_color, pygame.Rect(0, 0, 299, 399), 2)

    # heading
    head_img = piece_font.render("Correct!", True, grid_color)
    box.blit(head_img,
             (box.get_width() / 2 - head_img.get_width() / 2, box.get_height() / 2 - head_img.get_height() / 2 - 150))

    # message
    mess_img_0 = credits_font.render("You beat level " + str(level + 1) + ".", True, grid_color)
    mess_img_1 = credits_font.render("Great work!", True, grid_color)
    box.blit(mess_img_0, (
        box.get_width() / 2 - mess_img_0.get_width() / 2, box.get_height() / 2 - mess_img_0.get_height() / 2 - 75))
    box.blit(mess_img_1, (
        box.get_width() / 2 - mess_img_1.get_width() / 2, box.get_height() / 2 - mess_img_1.get_height() / 2 - 50))

    # buttons
    for button in buttons:
        box.blit(button.get_image(), (button.x, button.y))

    # blit box to screen
    screen.blit(box, (250, 100))

    # flip display
    pygame.display.update()


def pop_up(screen, buttons, level):
    ###pop up window###
    buttons = [
        Button(20, 190, 260, 50, grid_color, piece_color, button_font, "Next Level", "N"),
        Button(20, 260, 260, 50, grid_color, piece_color, button_font, "Replay", "R"),
        Button(20, 330, 260, 50, grid_color, piece_color, button_font, "Home", "H")

    ]
    overlay(screen, buttons, level)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # down button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(
                            (event.pos[0] - 250, event.pos[1] - 100)):  # compensate for offset origin
                        button.hover = 3
                        overlay(screen, buttons, level)

            # up button
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in buttons:
                    if button.hover == 3:  # include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        overlay(screen, buttons, level)
                        # programmatic control
                        if button.key == "N":
                            main(screen, level + 1)
                            return
                        elif button.key == "R":
                            # print("restart")
                            main(screen, level)
                            return
                        elif button.key == "H":
                            return

        # hover shading
        pos = (pygame.mouse.get_pos()[0] - 250,
               pygame.mouse.get_pos()[1] - 100)  # compensate for offset origin
        for button in buttons:
            if button.rect.collidepoint(pos) and button.hover == 0:
                button.hover = 1
                overlay(screen, buttons, level)
            elif not button.rect.collidepoint(
                    pos) and button.hover == 1:  # will only update screen when necessary
                button.hover = 0
                overlay(screen, buttons, level)


def reset_pieces(screen, pieces, selected, buttons, level):
    for piece in pieces:
        if isinstance(piece, NestedPiece):
            explode(pieces, piece)
            display(screen, pieces, selected, buttons)

    for piece in pieces:
        delta_x = piece.starting_pos[0] - piece.pos[0]
        delta_y = piece.starting_pos[1] - piece.pos[1]
        steps = int((delta_x ** 2 + delta_y ** 2) ** 0.5 / 10)
        for _ in range(steps):
            piece.pos = (piece.pos[0] + delta_x / steps, piece.pos[1] + delta_y / steps)
            display(screen, pieces, selected, buttons)
            pygame.time.wait(1)
        piece.grid = piece.starting_grid
        display(screen, pieces, selected, buttons)


def flash_red(screen, pieces, selected, buttons, button):
    # flash red
    for i in range(2):
        button.color = red
        button.txt_color = red
        button.bg = background_color
        display(screen, pieces, selected, buttons)
        pygame.time.wait(100)
        button.color = grid_color
        button.txt_color = piece_color
        button.bg = red
        display(screen, pieces, selected, buttons)
        pygame.time.wait(100)
    button.bg = white
    button.color = grid_color
    button.txt_color = piece_color
    display(screen, pieces, selected, buttons)


def explode(pieces, nested):
    for piece in nested.contents:
        if piece is not None:
            nested.remove(piece)
            pieces.append(piece)
            attempt_place(pieces, nested.grid, piece)
    nested.contents = [None for _ in range(nested.size)]


def attempt_place(pieces, pos, piece):
    # print(pos, piece)
    delta_x = 1
    delta_y = 0
    tries = 0
    while get_piece(pieces, (pos[0] + delta_x, pos[1] + delta_y)) != False or (
                            pos[0] + delta_x > 12 or pos[1] + delta_y > 9 or (
                                pos[0] + delta_x >= 10 and pos[1] + delta_y >= 8)):
        delta_x = randint(-1, 1)
        delta_y = randint(-1, 1)
        tries += 1
        if tries > 100:
            print("could not find a spot!")
            break
    if tries < 100:
        piece.grid = (pos[0] + delta_x, pos[1] + delta_y)
    piece.pos = piece.get_pos()


def display(screen, pieces, selected, buttons):
    width = screen.get_width()
    height = screen.get_height()

    g_width = (width - 200) / 10
    g_height = height / 10

    # clear screen
    screen.fill(background_color)

    grid_colors_hor = [
        (175, 175, 175),
        (175, 175, 175),
        (50, 50, 50)
    ]

    grid_colors_vert = [
        (125, 125, 125),
        (150, 150, 150),
        (0, 0, 0)
    ]

    # draw grid
    for y in range(10):
        pygame.draw.line(screen, grid_colors_hor[0], (0, y * g_height - 1), (width - 200, y * g_height - 1))
        pygame.draw.line(screen, grid_colors_hor[2], (0, y * g_height + 1), (width - 200, y * g_height + 1))
    for x in range(10):
        pygame.draw.line(screen, grid_colors_vert[0], (x * g_width - 1, 0), (x * g_width - 1, height))
        pygame.draw.line(screen, grid_colors_vert[2], (x * g_width + 1, 0), (x * g_width + 1, height))
    for y in range(10):
        pygame.draw.line(screen, grid_colors_hor[1], (0, y * g_height), (width - 200, y * g_height))
    for x in range(10):
        pygame.draw.line(screen, grid_colors_vert[1], (x * g_width, 0), (x * g_width, height))

    # draw border and partitions
    pygame.draw.rect(screen, grid_color, pygame.Rect(0, 0, width - 1, height - 1), 4)
    pygame.draw.line(screen, grid_color, (width - 200, 0), (width - 200, height), 2)
    # pygame.draw.line(screen, grid_color, (600,480), (800,480), 2)

    # sort pieces for proper rendering order
    pieces.sort(key=lambda p: 10 * p.grid[1] + p.grid[0])
    if selected:
        pieces.remove(selected)  # move selected to end of pieces list so it is rendered last (on top)
        pieces.append(selected)

    positions_used = []

    # draw pieces
    for piece in pieces:
        # print piece.get_pos()
        n = positions_used.count(piece.grid)
        if n == 0:
            screen.blit(piece.image, piece.pos)
        else:
            offset_x = 5  # the ratio of these two values determines the slope at which the stack renders
            offset_y = 5  # slope should match that of tile source image
            draw_x, draw_y = piece.pos[0] - offset_x * n, piece.pos[1] - offset_y * n
            screen.blit(piece.image, (draw_x, draw_y))
            # # draw lines to separate pieces (only *necessary* if offset < tile height)
            pygame.draw.line(screen, (220, 220, 220), (draw_x + offset_x, draw_y + 50), (draw_x + 50, draw_y + 50), 1)
            pygame.draw.line(screen, (140, 140, 140), (draw_x + 50, draw_y + 50), (draw_x + 50, draw_y + offset_y), 1)
        positions_used.append(piece.grid)

    # draw buttons
    for button in buttons:
        screen.blit(button.get_image(), (button.x, button.y))

    # flip display
    pygame.display.update()


# main() takes screen and a level index
def main(screen, level):
    # set up screen
    s_w = 800
    s_h = 600

    # set window caption
    pygame.display.set_caption("Level " + str(level + 1))

    # init pieces (build from level)

    # init buttons
    buttons = [
        Button(615, 545, 50, 50, grid_color, piece_color, button_font, "", "C", check_image),
        Button(675, 545, 50, 50, grid_color, piece_color, button_font, "", "R", reset_image),
        Button(735, 545, 50, 50, grid_color, piece_color, button_font, "", "H", home_image)
    ]

    pieces = load_level(level)

    # init selected var
    selected = False

    # show board
    display(screen, pieces, selected, buttons)

    # set up clock
    clock = pygame.time.Clock()

    # game loop
    done = False

    while not done:
        clock.tick(60)

        # user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                done = True

            # run check algorithm
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if check_scrabble(pieces):
                        # print("success!!!")
                        pop_up(screen, buttons, level)
                        return
                    else:
                        # print("failure!!!")
                        pass

            # select (pick up) piece
            if event.type == MOUSEBUTTONDOWN:
                pos = mouse.get_pos()
                # decide grid location based on whether on board or rack
                if pos[0] > 600:
                    pos = (int((pos[0] - 10) / 60), int(pos[1] / 60))
                else:
                    pos = (int(pos[0] / 60), int(pos[1] / 60))
                clicked = get_piece(pieces, pos)

                if event.button == 1:
                    if clicked and not clicked.locked:  # if clicked is not None and piece is not locked
                        selected = clicked
                    # detect button press
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):
                            button.hover = 3
                            display(screen, pieces, selected, buttons)

                elif event.button == 3:
                    if clicked and not clicked.locked:
                        if isinstance(clicked, NestedPiece):
                            explode(pieces, clicked)
                            display(screen, pieces, selected, buttons)
                        else:
                            pass

            # deselect (place) piece
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    pos = mouse.get_pos()
                    pos = (int(pos[0] / 60), int(pos[1] / 60))
                    if selected:
                        if pos[0] > 12 or pos[1] > 9 or (
                                        pos[0] >= 10 and pos[1] >= 9):  # check if outside acceptable range
                            pass
                        elif get_piece(pieces, pos) == False or get_piece(pieces, pos) == selected:
                            selected.grid = pos
                        elif get_piece(pieces, pos).data == selected.data and pos[0] >= 10:  # tile stacking in tray
                            selected.grid = pos
                        # insert into nested piece
                        elif isinstance(get_piece(pieces, pos), NestedPiece) and \
                                        None in get_piece(pieces, pos).contents:
                            # print("nesting yay!")
                            get_piece(pieces, pos).insert(selected)
                            pieces.remove(selected)  # temporary
                        else:
                            attempt_place(pieces, pos, selected)

                        selected.pos = selected.get_pos()
                        selected = False
                        display(screen, pieces, selected, buttons)

                # button execution
                for button in buttons:
                    if button.hover == 3:  # include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                        button.hover = 0
                        display(screen, pieces, selected, buttons)
                        if button.key == "C":
                            if check_scrabble(pieces):
                                # print("success!!!")
                                pop_up(screen, buttons, level)
                                return
                            else:
                                # print("failure!!!")
                                flash_red(screen, pieces, selected, buttons, button)
                        elif button.key == "R":
                            reset_pieces(screen, pieces, selected, buttons, level)
                            pygame.time.wait(100)       # allow for reset animation to finish (asynchronous?)
                            pieces = load_level(level)
                        elif button.key == "H":
                            return

            # update pos of selected piece
            if selected != False:
                selected.pos = (mouse.get_pos()[0] - 25, mouse.get_pos()[1] - 25)
                display(screen, pieces, selected, buttons)

            # hover shading
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos) and button.hover == 0:
                    button.hover = 1
                    display(screen, pieces, selected, buttons)
                elif not button.rect.collidepoint(pos) and button.hover == 1:  # will only update screen when necessary
                    button.hover = 0
                    display(screen, pieces, selected, buttons)
