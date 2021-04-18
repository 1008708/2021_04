#!/usr/bin/python
# -*- coding: cp1251 -*-

import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

# И создать окно:
screen = pygame.display.set_mode((300, 200))

# здесь будут рисоваться фигуры
# ...


# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        clock.tick(30)
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()