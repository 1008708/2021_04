import pygame
from pygame.draw import *
from random import randint
#from math import

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
        return (round(self.x), round(self.y))

    def distance(self, other):
        return (pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def __add__(self, other):
        return Vector (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector (self.x - other.x, self.y - other.y)

    def __mul__(self, i):
        return Vector (self.x*i, self.y*i)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __neg__(self):
        return Vector (-self.x, -self.y)

class Ball:
    '''
    Класс шарика обладает:
    -координатами x,y типа Vector
    -скоростью vx, vy типа Vector
    -радиусом r
    -цветом color
    '''
    def __init__(self, pos, vel, r=10, color=(0, 0, 0)):
        self.color = color
        self.r = r
        self.pos = pos
        self.vel = vel
        self.alive = True
        self.elastity = 0.95
        self.m = 1

    def show(self):
        '''
        Перерисовать шарик
        :return: пусто
        '''
        circle(screen, self.color, self.pos.pair(), self.r)
        circle(screen, (10, 10, 10), self.pos.pair(), self.r, 1)

    def check_corners(self):
        if (self.pos.x - self.r) < 0:
            self.pos.x = self.r
            self.vel.x = -self.vel.x * self.elastity
            self.vel.y *= self.elastity

        if (self.pos.y - self.r) < 0:
            self.pos.y = self.r
            self.vel.y = -self.vel.y * self.elastity
            self.vel.x *= self.elastity

        if (self.pos.x + self.r) > screen_width:
            self.pos.x = screen_width - self.r
            self.vel.x = -self.vel.x * self.elastity
            self.vel.y *= self.elastity

        if (self.pos.y + self.r) > screen_height:
            self.pos.y = screen_height - self.r
            self.vel.y = -self.vel.y * self.elastity
            self.vel.x *= self.elastity

    def move(self, time=1):
        '''
        Движение шарика со своей скоростью
        :return:пусто
        '''
        self.check_corners()
        if 0 < abs(self.vel.x) < 0.1:
            self.vel.x = 0
        if 0 < abs(self.vel.y) < 0.1:
            self.vel.y = 0
        self.pos += self.vel * time

class Ballgrav(Ball):
    def __init__(self, pos, vel, r = 10, color = (0, 0, 0)):
        super().__init__(pos, vel, r, color)
        self.gravity = Vector(0, 2)

    def move(self, time=1):
        self.check_corners()
        if 0 < abs(self.vel.x) < 0.1:
            self.vel.x = 0
        if 0 < abs(self.vel.y) < 0.1:
            self.vel.y = 0

        self.vel += self.gravity
        self.pos += self.vel * time


class Game_obj:
    def __init__(self, number):
        self.number_of_balls = number
        self.finish_game = False
        self.mouse_pos = Vector()
        self.Balls = []
        self.score_table = Score()
        self.generate_balls(self.number_of_balls)

    def run(self):
        handle_code = self.handle()
        if handle_code == 1:
            index = self.mouse_push1()
            if index != -1:
                self.alive = False
                self.Balls.pop(index)
            else:
                self.generate_ballgrav()

        if handle_code == 3:
            number = self.number_of_balls
            self.Balls.clear()
            self.__init__(number)

        for i, ball in enumerate(self.Balls):
            ball.move()
            ball.show()

            for j in range(i, len(self.Balls)):
                if self.check_collision(i, j):
                    self.collade(i, j)
                    ball.move()

            #score_table.math()
    #    score_table.show()

    def generate_pos(self):
        return Vector(randint(60, screen_width-60), randint(60, screen_height-60))

    def generate_balls(self, number: int):
        for i in range(number):
            ball_speed = Vector(randint(-10, 10), randint(-10, 10))
            startpos = self.generate_pos()
            ball_color = (randint(0, 240), randint(0, 240), randint(0, 240))
            radius = randint(20, 50)
            ball = Ball(startpos, ball_speed, radius, ball_color)
            self.Balls.append(ball)

            for j in range(0, i):
                while self.check_collision(i, j) == True:
                    self.Balls[i].pos = self.generate_pos()
                    j = 0

    def generate_ballgrav(self):
            ball_speed = Vector(randint(-10, 10), randint(-10, 10))
            startpos = self.mouse_pos
            ball_color = (randint(0, 240), randint(0, 240), randint(0, 240))
            radius = randint(20, 50)
            ballgrav = Ballgrav(startpos, ball_speed, radius, ball_color)
            self.Balls.append(ballgrav)

            j = len(self.Balls) - 1
            for i in range(0, j):
                while self.check_collision(i, j) == True:
                    self.Balls[i].pos += self.Balls[i].vel * 2
                    i = 0

    def handle(self):
        '''
        обработчик событий
        0 - нет событий
        1 - кнопка левая мыши - попасть по шарику
        3 - кнопка правая мыши - начать новую игру
        выход - True in .finish_game
        :return: код события
        '''
        handle_code = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finish_game = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_code = 1
                m_pos = pygame.mouse.get_pos()
                self.mouse_pos = Vector(m_pos[0], m_pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                handle_code = 3
                m_pos = pygame.mouse.get_pos()
                self.mouse_pos = Vector(m_pos[0], m_pos[1])
        return handle_code

    def mouse_push1(self):
        index = -1
        for i, ball in enumerate(self.Balls):
            if ball.pos.distance(self.mouse_pos) < ball.r**2:
               index = i
        return index

    def check_collision(self, index1, index2):
        check = False

        min_lenght = (self.Balls[index1].r + self.Balls[index2].r)**2
        real_length = self.Balls[index1].pos.distance(self.Balls[index2].pos)

        if real_length != 0 and real_length*1.035 <= min_lenght:
            check = True
            self.Balls[index1].pos -= self.Balls[index1].vel
            self.Balls[index2].pos -= self.Balls[index2].vel
            rl = self.Balls[index1].pos.distance(self.Balls[index2].pos)

        return check

    def collade(self, index1, index2):
        vel1_new, vel2_new = Vector(), Vector()
        k_massa1 = (self.Balls[index1].m-self.Balls[index2].m * self.Balls[index2].elastity) / (self.Balls[index1].m+self.Balls[index2].m)
        k_massa2 = (1+self.Balls[index2].elastity)*self.Balls[index2].m / (self.Balls[index1].m+self.Balls[index2].m)
        vel1_new = self.Balls[index1].vel*k_massa1 + self.Balls[index2].vel*k_massa2

        k_massa1 = (self.Balls[index2].m-self.Balls[index1].m * self.Balls[index1].elastity) / (self.Balls[index1].m+self.Balls[index2].m)
        k_massa2 = (1+self.Balls[index1].elastity)*self.Balls[index1].m / (self.Balls[index1].m + self.Balls[index2].m)
        vel2_new = self.Balls[index2].vel*k_massa1 + self.Balls[index1].vel*k_massa2

        self.Balls[index1].vel = vel1_new
        self.Balls[index2].vel = vel2_new


if __name__ == '__main__':
    FPS = 30
    number_balls = 5

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.update()
    clock = pygame.time.Clock()

    game1 = Game_obj(number_balls)

    while not game1.finish_game:
        clock.tick(FPS)
        screen.fill('GRAY')
        game1.run()
        pygame.display.flip()
    pygame.quit()
