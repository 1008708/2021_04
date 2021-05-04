import pygame
from pygame.draw import *
from random import randint
pygame.init()

class Vector:
    '''Класс вектор:
     для работы с координатой шарика или скоростью'''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def pair(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector (self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)


class Ball:
    '''
    Класс шарика обладает:
    -координатами x,y типа Vector
    -скоростью vx, vy типа Vector
    -радиусом r
    -цветом color
    '''
    def __init__(self, pos, vel, r = 10,  color = (0, 0, 0)):
        self.color = color
        self.r = r
        self.pos = pos
        self.vel = vel

    def show(self):
        circle(screen, self.color, self.pos.pair(), self.r)

    def move(self):
        if (self.pos.x + self.r) > screen.get_width() or (self.pos.x - self.r) < 0:
            self.vel.x = -self.vel.x
        if (self.pos.y + self.r) > screen.get_height() or (self.pos.y - self.r) < 0:
            self.vel.y = -self.vel.y
        self.pos = self.pos + self.vel

    def collision(self):
        print('coll')

FPS = 30
global screen

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

screen = pygame.display.set_mode((1200, 900))
screen.fill('WHITE')
pygame.display.update()
clock = pygame.time.Clock()
finished = False
number_balls = 10
startpos = Vector(300, 200)


Startvel = [Vector(randint(-5, 5), randint(-10, 10)) for i in range(number_balls)]
Balls = [Ball(startpos, Startvel[i], 10*(10-i), COLORS[randint(0, 5)]) for i in range(number_balls)]

while not finished:
    clock.tick(FPS)
    for ball in Balls:
        ball.show()
        ball.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print('Click!')
    pygame.display.update()
    screen.fill('WHITE')

pygame.quit()