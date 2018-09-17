# -*- coding: utf-8 -*-

# Levels
# from Classes import *

# board: 0-9   container: 10-12

# + - × ÷ ^
# u"\u00F7"

m = u"×"
d = u"÷"
# print d


L1 = [
    (1, (10, 0)),
    (1, (11, 0)),
    (2, (10, 1)),
    ("+", (10, 4)),
    ("=", (10, 5))
]

L2 = [
    (2, (10, 0)),
    (5, (10, 1)),
    (10, (10, 2)),
    (m, (10, 4)),
    ("=", (10, 5)),
]

L3 = [
    (1, (10, 0)),
    (1, (11, 0)),
    (2, (10, 1)),
    (3, (10, 2)),
    ("+", (10, 4)),
    (m, (10, 5)),
    ("=", (10, 7))
]

L4 = [
    (1, (10, 0)),
    (5, (10, 1)),
    (6, (10, 2)),
    ("-", (10, 4)),
    ("=", (10, 7))
]

L5 = [
    (3, (10, 0)),
    (3, (11, 0)),
    (9, (10, 2)),
    (d, (10, 4)),
    ("=", (10, 7))
]

L6 = [
    (2, (10, 0)),
    (3, (10, 1)),
    (8, (10, 2)),
    ("^", (10, 4)),
    ("=", (10, 7))
]

L7 = [
    (2, (10, 0)),
    (2, (11, 0)),
    (3, (10, 1)),
    (36, (10, 2)),
    (m, (10, 4)),
    ("^", (11, 4)),
    ("=", (10, 7))
]

L8 = [
    (1, (10, 0)),
    (1, (11, 0)),
    (3, (10, 1)),
    (4, (10, 2)),
    (12, (10, 3)),
    (m, (10, 5)),
    ("=", (10, 7))
]

L9 = [
    (3, (10, 0)),
    (4, (11, 0)),
    (2, (10, 1)),
    (12, (10, 2)),
    (24, (10, 3)),
    (m, (10, 5)),
    (d, (11, 5)),
    ("=", (10, 7)),
    ("=", (11, 7))
]

L10 = [
    (2, (10, 0)),
    (3, (11, 0)),
    (5, (10, 1)),
    (10, (11, 1)),
    (15, (10, 2)),
    (20, (11, 2)),
    (m, (10, 4)),
    ("=", (10, 7)),
    ("=", (11, 7))
]

L11 = [
    (1, (10, 0)),
    (2, (11, 0)),
    (2, (11, 0)),
    (2, (11, 0)),
    (3, (12, 0)),
    (5, (10, 1)),
    (6, (11, 1)),
    (7, (12, 1)),
    (7, (12, 1)),
    (19, (10, 2)),
    ("-", (10, 4)),
    ("-", (10, 4)),
    ("-", (10, 4)),
    (m, (11, 4)),
    ("^", (12, 4)),
    ("^", (12, 4)),
    ("=", (10, 7)),
    ("=", (10, 7)),
    ("=", (10, 7))
]

L12 = [
    (1, (10, 0)),
    (2, (10, 1)),
    (3, (10, 2)),
    ("+", (3, 4)),
    ("=", (5, 4))
]

L13 = [
    (4, (0, 4)),
    (4, (2, 4)),
    (4, (4, 4)),
    (4, (6, 4)),
    (0, (8, 4)),
    ("=", (7, 4)),
    (d, (10, 0)),
    ("-", (11, 0)),
    (m, (10, 1)),
]

L14 = [
    (0, (10, 0)),
    (0, (10, 0)),
    (1, (11, 0)),
    (1, (11, 0)),
    (2, (12, 0)),
    (2, (12, 0)),
    (3, (10, 1)),
    (3, (10, 1)),
    (3, (10, 1)),
    (4, (11, 1)),
    (4, (11, 1)),
    (6, (12, 1)),
    (6, (12, 1)),
    (6, (12, 1)),
    (9, (10, 2)),
    (12, (11, 2)),
    ("+", (10, 4)),
    ("+", (10, 4)),
    ("+", (10, 4)),
    ("+", (10, 4)),
    ("+", (10, 4)),
    ("-", (11, 4)),
    ("-", (11, 4)),
    (d, (12, 4)),
    (m, (10, 5)),
    (m, (10, 5)),
    (m, (10, 5)),
    ("^", (11, 5)),
    ("^", (11, 5)),
    ("=", (10, 7)),
    ("=", (10, 7)),
    ("=", (10, 7)),
    ("=", (10, 7)),
    ("=", (11, 7)),
    ("=", (11, 7)),
    ("=", (11, 7)),
    ("=", (11, 7))
]

L15 = [
    (3, (10, 0)),
    (5, (11, 0)),
    (6, (10, 1)),
    (36, (11, 1)),
    ("N3", (10, 3)),
    ("-", (10, 5)),
    ("^", (11, 5)),
    ("=", (10, 7))
]

L16 = [
    (2, (10, 0)),
    (4, (11, 0)),
    (6, (12, 0)),
    (18, (10, 1)),
    (36, (11, 1)),
    ("N3", (10, 3)),
    ("N3", (10, 3)),
    ("-", (10, 5)),
    ("^", (11, 5)),
    ("^", (11, 5)),
    ("=", (10, 7))
]

L17 = [
    (2, (11, 0)),
    (3, (10, 1)),
    (4, (11, 1)),
    (6, (10, 2)),
    (12, (11, 2)),
    (m, (10, 5)),
    (m, (10, 5)),
    ("=", (10, 7)),
    ("=", (10, 7))
]

L18 = [
    (2, (10, 0)),
    (3, (11, 0)),
    (13, (10, 1)),
    (13, (10, 1)),
    (30, (11, 1)),
    (70, (10, 2)),
    ("N3", (10, 4)),
    ("-", (10, 6)),
    ("-", (10, 6)),
    ("^", (11, 6)),
    ("^", (11, 6)),
    ("=", (10, 8))
]

Levels = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15, L16, L17, L18]
