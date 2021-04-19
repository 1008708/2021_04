#!/usr/bin/python
# -*- coding: cp1251 -*-

import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

def eye(x, y, color, size):
    circle(screen, color, (x, y), size, 0)
    circle(screen, "black", (x, y), size // 3, 0)


def elad(cenx, ceny, size_head):
    # здесь будут рисоваться фигуры
    # ...
    color = (200, 150, 150)
    circle(screen, color, (cenx, ceny), size_head, 0)
    
    x_eye1 = cenx - size_head // 2; y_eye1 = ceny - size_head  // 2
    x_eye2 = cenx + size_head // 2; y_eye2 = ceny - size_head  // 2
    
    color = (30, 150, 150)
    eye(x_eye1, y_eye1, color, size_head // 10)
    eye(x_eye2, y_eye2, color, size_head // 10)
        
    color = (230, 100, 150)
    x_mouth = cenx - size_head // 2
    y_mouth = ceny + size_head // 2.5
    rect(screen, color, (x_mouth, y_mouth, size_head, size_head // 10))

    color = (230, 200, 250)
    nouse = [(cenx, ceny - size_head // 10), (cenx - size_head // 10, ceny), 
             (cenx + size_head // 10, ceny), (cenx, ceny - size_head // 10)]
    polygon(screen, (0, 0, 255), nouse, 0)
    
# И создать окно:
screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()
finished = False
FPS = 50
scale = 150

screen.fill('WHITE')
elad(200, 200, scale)
pygame.display.update()

while not finished:
    for event in pygame.event.get():
        clock.tick(FPS) 
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            finished = True
        if key[pygame.K_LEFT]:
            scale -= 5
            screen.fill('WHITE')
            elad(200, 200, scale)
            pygame.display.flip()
        if key[pygame.K_RIGHT]:
            scale += 5
            screen.fill('WHITE')
            elad(200, 200, scale)
            pygame.display.flip()
            
pygame.quit()