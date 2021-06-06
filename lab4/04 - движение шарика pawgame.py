import pygame
from pygame.draw import *
from random import randint

global screen, screen_width, screen_height
screen_width = 1200
screen_height = 900

class Score:
    '''
    Score Table
    '''
    def __init__(self):
        self.b_col_score = 0
        self.font = pygame.font.SysFont("dejavusansmono", 25)

    def math(self, score=1):
        self.b_col_score +=score

    def show(self):
        score_surf = []
        score_surf.append(self.font.render("Collide: {}".format(self.b_col_score), True, 'WHITE'))
        #score_surf.append(self.font.render("Balls used: {}".format(self.b_used), True, WHITE))
        #score_surf.append(self.font.render("Total: {}".format(self.score()), True, RED))
        screen.blit(score_surf[0], [10, 10])


class Vector:
    '''Класс вектор:
     для работы с координатой шарика или скоростью'''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def pair(self):
        return (self.x, self.y)

    def distance(self, other):
        return (pow(self.x - other.x, 2) + pow(self.y - other.y, 2))**0.5

    def __add__(self, other):
        return Vector (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector (self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __neg__(self):
        return Vector (-self.x , -self.y)

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
        self.in_start_pos = True

    def show(self):
        '''
        Перерисовать шарик
        :return: пусто
        '''
        circle(screen, self.color, self.pos.pair(), self.r)

    def move(self):
        '''
        Движение шарика со своей скоростью
        :return:пусто
        '''
        if (self.pos.x + self.r/1.3 ) >= screen_width or (self.pos.x - self.r/1.3 ) <= 0:
            self.vel.x = -self.vel.x

        if (self.pos.y + self.r/1.3) >= screen_height or (self.pos.y - self.r/1.3) <= 0:
            self.vel.y = -self.vel.y

        self.pos += self.vel

    def check_collision(self, other):
        min_lenght = (self.r+other.r)*1.05
        check = False
        if min_lenght != 0 and self.pos.distance(other.pos) < min_lenght:
            check = True
        return check

    def collade(self, other):
        self.vel = -self.vel
        other.vel = -other.vel

def gerenerate_color():
    return (randint(0, 240), randint(0, 240), randint(0, 240))

def generate_pos():
    startpos = Vector(randint(60, screen_width-60), randint(60, screen_height-60))
    return startpos

def generate_balls(number: int):
    balls = []
    for i in range(0, number):
        ball_speed = Vector(randint(-10, 10), randint(-10, 10))
        radius = randint(10, 50)
        startpos = generate_pos()
        ball = Ball(startpos, ball_speed, radius, gerenerate_color())
        balls.append(ball)

        if i > 0:
            for j in range(0, i-1):
                while balls[i].check_collision(balls[j]) == True:
                    balls[i].pos = generate_pos()
                    j = 0

    return balls

def my_main():
    finish = False
    FPS = 40
    clock = pygame.time.Clock()
    number_balls = 10

    score_table = Score()
    Balls = generate_balls(number_balls)

    while not finish:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print('Click!')

        for i, ball in enumerate(Balls):
            ball.move()
            ball.show()

            for j in range(0, i):
                if ball.check_collision(Balls[j]):
                    ball.collade(Balls[j])
                    score_table.math()

        pygame.display.flip()
        screen.fill('GRAY')
        score_table.show()

    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill('WHITE')
    pygame.display.update()

    my_main()