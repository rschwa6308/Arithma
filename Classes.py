# -*- coding: utf-8 -*-

# game classes
import pygame
from pygame import gfxdraw

from Colors import *
from Images import *
from Check import *


class Button:
    def __init__(self, x, y, width, height, color, txt_color, font, text, key):
        self.hover = 0
        self.bg = (255, 255, 255)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

        self.color = color

        self.txt_color = color
        self.font = font
        self.text = text

        self.key = key

    def get_image(self):
        img = pygame.Surface((self.width, self.height))
        img.fill((self.bg[0] - 50 * self.hover, self.bg[1] - 50 * self.hover, self.bg[2] - 50 * self.hover))
        bwidth = 2
        buff = bwidth - 1
        pygame.draw.rect(img, self.color, pygame.Rect(buff, buff, self.width - 2 * buff, self.height - 2 * buff),
                         bwidth)

        text_img = self.font.render(self.text, 1, self.txt_color)
        img.blit(text_img, (
            self.width / 2 - text_img.get_width() / 2, self.height / 2 - text_img.get_height() / 2))  # auto center text
        return img


class Slider:
    def __init__(self, start, length, x, color, bg_color):
        self.start = start
        self.length = length
        self.end = (start[0] + length, start[1])
        self.x = x
        self.color = color
        self.bg_color = bg_color

    def get_rect(self):
        return pygame.Rect(self.x - 5 + self.start[0], self.start[1], 10, 40)

    def get_image(self):
        # print self.start
        # print self.end
        image = pygame.Surface((self.length + 10, 40))
        image.fill(self.bg_color)
        # draw line
        pygame.draw.line(image, self.color, (5, 20), (self.length, 20), 4)
        # draw rect(s)
        pygame.draw.rect(image, self.color, pygame.Rect(self.x - 5, 0, 10, 40))
        return image


class Piece:
    def __init__(self, data, grid, locked=False):
        self.data = data
        self.grid = grid
        self.locked = locked
        self.pos = self.get_pos()

        # # Minimalistic - white text on black piece
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(piece_color)
        # text_img = piece_font.render(str(data), 1, text_color)
        # self.image.blit(text_img, (50 / 2 - text_img.get_width() / 2, 50 / 2 - text_img.get_height() / 2))

        # 3D - black text on white piece with black shadow
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image.blit(piece_image, (0, 0))
        text_img = piece_font.render(str(data), 1, piece_color)

        n = 1  # shadow width offset correction
        self.image.blit(text_img, (50 / 2 - text_img.get_width() / 2 - n, 50 / 2 - text_img.get_height() / 2 - n))
        if self.locked:
            # TODO: Make up my mind already!
            # # corner lines (straps)
            # n = 8
            # w = 2
            # pygame.draw.line(self.image, white, (0, n), (n, 0), w)
            # pygame.draw.line(self.image, white, (50 - n, 0), (50, n), w)
            # pygame.draw.line(self.image, white, (50, 50 - n), (50 - n, 50), w)
            # pygame.draw.line(self.image, white, (n, 50), (0, 50 - n), w)

            # # corner circles (bolts)
            # n = 6
            # r = 2
            # pygame.draw.circle(self.image, white, (n, n), r, 0)
            # pygame.draw.circle(self.image, white, (50 - n, n), r, 0)
            # pygame.draw.circle(self.image, white, (50 - n, 50 - n), r, 0)
            # pygame.draw.circle(self.image, white, (n, 50 - n), r, 0)

            # bold black lettering on white background # with black border
            self.image.fill(background_color)
            # n = 2
            # pygame.draw.rect(self.image, background_color, pygame.Rect(n, n, 50 - 2 * n, 50 - 2 * n), 0)
            text_img = piece_font.render(str(data), 1, piece_color)
            self.image.blit(text_img, (50 / 2 - text_img.get_width() / 2, 50 / 2 - text_img.get_height() / 2))

    def get_pos(self):
        return (self.grid[0] * 60 + 5, self.grid[1] * 60 + 5)

    def get_image(self):
        return self.image


class NestedPiece(Piece):
    def __init__(self, size, grid, locked=False):
        self.size = size
        self.grid = grid
        self.locked = locked
        self.pos = self.get_pos()

        self.contents = [None for _ in range(self.size)]
        self.contents = [Piece(1, (0, 0)), Piece("+", (0, 0)), None] # Piece(2, (0, 0))]  # test dummy data

    def get_image(self):
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image.blit(piece_image, (0, 0))

        # # split rectangle (grid look)
        # n = 42 / size
        # pygame.draw.rect(self.image, piece_color, pygame.Rect(4, 4, n, 42), 1)
        # for i in range(size):
        #     pygame.draw.line(self.image, piece_color, (4, 4 + i * n), (4 + n, 4 + i * n), 1)

        # distinct squares
        n = 42 / self.size
        dim = 8
        for i in range(self.size):
            p = self.contents[i]
            # if spot is filled, draw filled square
            if p:
                pygame.draw.rect(self.image, piece_color, pygame.Rect(6, 6 + i * n, dim, dim), 0)
            else:
                pygame.draw.rect(self.image, piece_color, pygame.Rect(6, 6 + i * n, dim, dim), 1)

        if all(self.contents):
            self.data = get_value([p.data for p in self.contents])
            print(self.data)
            text_img = piece_font.render(str(self.data), 1, piece_color)
            n = 1  # shadow width offset correction
            self.image.blit(text_img,
                            (6 + 50 / 2 - text_img.get_width() / 2 - n, 50 / 2 - text_img.get_height() / 2 - n))

        return self.image
