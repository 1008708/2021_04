#!/usr/bin/python
# -*- coding: cp1251 -*-

import pygame
from pygame.draw import *

# ����� ������� ����������, ���������� � ����������������:
pygame.init()

# � ������� ����:
screen = pygame.display.set_mode((300, 200))

# ����� ����� ���������� ������
# ...


# ����� ����, ����� ��� ������������ �� ������, ����� ����� ��������:
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        clock.tick(30)
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()