'''
текущие цели:
ввести перемещение фигур
ввести сокращенные имена для шахматных координат (мб еще фигур)
ввести спрайты для фигур
'''
from math import floor

import pygame
import os
import sys

from Move import Move
from FigureSprite import FigureSprite
from pygame.locals import *

from Board import Board


class PyChessGUI:
    # вызываем инициализацию экрана, координат
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((850, 500))
        self.boardStart_x = 50
        self.boardStart_y = 50
        pygame.display.set_caption('Python Chess')

        self.square_size = 50
        self.white_square = pygame.image.load(os.path.join("images", "white_square.png")).convert()
        self.black_square = pygame.image.load(os.path.join("images", "black_square.png")).convert()

        # self.white_king = pygame.image.load(os.path.join("images", "White_King.png")).convert()
        # self.white_king = pygame.transform.scale(self.white_king, (self.square_size, self.square_size))
        self.figures = pygame.sprite.Group()
        self.fontDefault = pygame.font.Font(None, 20)

    # конвертер координат мыши в координаты доски
    def convert_to_chess_coords(self, screen_position):
        (x, y) = screen_position
        row = floor((y - self.boardStart_y) / self.square_size)
        col = floor((x - self.boardStart_x) / self.square_size)
        return tuple([col, row])

    # и обратно
    def convert_to_screen_coords(self, position):
        (row, col) = position
        screen_x = self.boardStart_x + col * self.square_size
        screen_y = self.boardStart_y + row * self.square_size
        return tuple([screen_x, screen_y])

    def create_sprites(self, board):
        figures = []
        for figure in board.figures:
            figures.append(FigureSprite(pygame.transform.scale(figure.image, (self.square_size, self.square_size)),
                                        self.convert_to_screen_coords(figure.position)))
        self.figures.add(figures)


    def draw(self, board):
        for i in range(board.size):
            for j in range(board.size):
                (screen_x, screen_y) = self.convert_to_screen_coords((i, j))
                if (i + j) % 2 == 0:
                    self.screen.blit(self.white_square, (screen_x, screen_y))
                else:
                    self.screen.blit(self.black_square, (screen_x, screen_y))
        '''будет цикл на отрисовку фигур, как с клетками. пока пусть так висит.
           ДЛЯ ФИГУР - СПРАЙТЫ!'''

        self.create_sprites(board)
        self.figures.draw(self.screen)
        # self.screen.blit(self.white_king, (50, 50))
        pygame.display.update()

    def get_clicked_square(self, board, position):
        (row, col) = self.convert_to_chess_coords((position[0], position[1]))
        if board.is_valid_position(board, (row, col)):
            return tuple([row, col])
        else:
            return False


'''______________________MAIN_____________________-'''

if __name__ == "__main__":
    # инициализация
    game = PyChessGUI()
    board = Board()
    clock = pygame.time.Clock()
    using_figure = False

    # отрисовка доски (клеточек), фигур
    game.draw(board)

    while 1:
        # clock.tick(30)
        for event in pygame.event.get():
            # if для выхода на крестик
            if event.type is QUIT:
                pygame.quit()
                sys.exit(0)
            # список возможных рекций на клавиши
            if hasattr(event, 'key'):
                # выход на q
                if event.key is K_q:
                    pygame.quit()
                    sys.exit(0)

            if (event.type is MOUSEBUTTONDOWN) and (event.button is 1):
                if using_figure is False:
                    square = game.get_clicked_square(board, event.pos)
                    if square is not False:
                        using_figure = True

                    '''вызывается проверка координаты под мышкой
                       переход в шахматные координаты
                       проверяется наличие корректной фигуры по этим координатам
                       недоступная -> continue
                       иначе - берем фигуру
                       отрисовываем доступные для хода клетки
                       флаг = Тру'''
                else:
                    using_figure = False
                    '''-когда флаг == Тру
                       мышкой выбираем клетку
                       проверка на совпадение с доступной
                       недоступная -> continue
                       иначе - ставим фигуру
                       при надобности - вызываем функцию для удаления фигуры противника
                       флаг = Ф'''
