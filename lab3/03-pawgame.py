#!/usr/bin/python
# -*- coding: cp1251 -*-

import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

def eye(screen, color, x, y, size):
    '''
    x, y - центр глаз
    цвет, радиус
    '''
    circle(screen, color, (x, y), size, 0)
    circle(screen, "black", (x, y), size // 3, 0)

def mouth(screen, color, x, y, width, height):
    '''
    x, y - левый верх рта
    цвет
    '''
    rect(screen, color, (x, y, width, height), 0)
    rect(screen, 'WHITE', (x, y + height // 2, width, height // 2), 1)
    

def elad(screen, cenx, ceny, size_head):
    # здесь будут рисоваться фигуры
    # ...
    color = (200, 150, 150)
    circle(screen, color, (cenx, ceny), size_head, 0)
    
    y_eye = ceny - size_head  // 2
    color = (30, 150, 150)
    for x_eye1 in (cenx - size_head // 2, cenx + size_head // 2):
        eye(screen, color, x_eye1, y_eye, size_head // 10)
            
    color = (230, 100, 150)
    x_mouth = cenx - size_head // 2
    y_mouth = ceny + size_head // 2.5
    mouth(screen, color, x_mouth, y_mouth, size_head, size_head // 10)
    
    color = (20, 200, 250)
    nouse = [(cenx, ceny - size_head // 10), (cenx - size_head // 10, ceny), 
             (cenx + size_head // 10, ceny), (cenx, ceny - size_head // 10)]
    polygon(screen, color, nouse, 0)
    
# И создать окно:
screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()
finished = False
FPS = 50
scale = 150

while not finished:
    clock.tick(FPS) 
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            finished = True
        if key[pygame.K_LEFT]:
            scale -= 5
        elif key[pygame.K_RIGHT]:
            scale += 5
    screen.fill('WHITE')
    elad(screen, 400, 200, scale)
    elad(screen, 100, 200, scale // 2)
    elad(screen, 700, 200, scale // 2)
    pygame.display.update()
            
pygame.quit()