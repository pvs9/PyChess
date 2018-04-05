'''
текущие цели:
ввести перемещение фигур
ввести сокращенные имена для шахматных координат (мб еще фигур)
ввести спрайты для фигур
'''
from math import floor
from typing import Optional

import pygame
import os
import sys

from Move import Move
# from FigureSprite import FigureSprite
from pygame.locals import *

from Board import Board

WHITE = True
BLACK = False


class PyChessGUI:
    # вызываем инициализацию экрана, координат
    def __init__(self, board=None, side=WHITE):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((850, 500))
        self.board_start_x = 50
        self.board_start_y = 50
        pygame.display.set_caption('Python Chess')

        self.square_size = 50
        self.white_square = pygame.image.load(os.path.join("images", "white_square.png")).convert()
        self.black_square = pygame.image.load(os.path.join("images", "black_square.png")).convert()
        self.board = board
        self.player_side = side

        # self.figures = pygame.sprite.Group()
        self.fontDefault = pygame.font.Font(None, 20)

    # конвертер координат мыши в координаты доски
    def convert_to_chess_coords(self, screen_position):
        (x, y) = screen_position
        row = floor((y - self.board_start_y) / self.square_size)
        col = floor((x - self.board_start_x) / self.square_size)
        return tuple([col, row])

    # и обратно
    def convert_to_screen_coords(self, position):
        (col, row) = position
        screen_x = self.board_start_x + col * self.square_size
        screen_y = self.board_start_y + row * self.square_size
        return tuple([screen_x, screen_y])

    def transform_figure_images(self):
        for figure in self.board.figures:
            figure.image = pygame.transform.scale(figure.image, (self.square_size, self.square_size))

    '''def create_sprites(self, board):
        figures = []
        for figure in board.figures:
            figures.append(FigureSprite(pygame.transform.scale(figure.image, (self.square_size, self.square_size)),
                                        self.convert_to_screen_coords(figure.position)))
        self.figures.add(figures)'''

    def init_draw(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                (screen_x, screen_y) = self.convert_to_screen_coords((i, j))
                if (i + j) % 2 == 0:
                    self.screen.blit(self.white_square, (screen_x, screen_y))
                else:
                    self.screen.blit(self.black_square, (screen_x, screen_y))
        '''будет цикл на отрисовку фигур, как с клетками. пока пусть так висит.
           ДЛЯ ФИГУР - СПРАЙТЫ!'''
        self.transform_figure_images()
        # self.create_sprites(board)
        # self.figures.draw(self.screen)
        self.screen.blit(self.board.figures[0].image, self.convert_to_screen_coords(self.board.figures[0].position))
        self.screen.blit(self.board.figures[1].image, self.convert_to_screen_coords(self.board.figures[1].position))
        pygame.display.update()

    def get_clicked_square(self, position):
        (col, row) = self.convert_to_chess_coords((position[0], position[1]))
        if self.board.is_valid_position(self.board, (row, col)):
            return tuple([col, row])
        else:
            return None

    def pick_figure(self, position):
        figure = self.board.find_figure(position)
        if figure is not None and figure.side is self.player_side:
            move = Move(figure, None)
            return move
        else:
            return None

    def move_draw(self, move):
        if(move.old_pos[0] + move.old_pos[1]) % 2 == 0:
            self.screen.blit(self.white_square, self.convert_to_screen_coords(move.old_pos))
        else:
            self.screen.blit(self.black_square, self.convert_to_screen_coords(move.old_pos))
        game.screen.blit(move.piece.image, game.convert_to_screen_coords(move.piece.position))
        pygame.display.update()





'''______________________MAIN_____________________-'''

if __name__ == "__main__":
    # инициализация
    game = PyChessGUI()
    game.board = Board()
    clock = pygame.time.Clock()
    using_figure = False

    # отрисовка доски (клеточек), фигур
    game.init_draw()

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
                    square = game.get_clicked_square(event.pos)
                    if square is not None:
                        # вызов функции на проверку наличия валидной фигуры
                        move = game.pick_figure(square)
                        if move is not None:
                            using_figure = True
                        else:
                            continue
                    else:
                        continue
                    '''
                       ...проверяется наличие корректной фигуры по этим координатам
                       иначе - берем фигуру
                       отрисовываем доступные для хода клетки
                       флаг = Тру'''
                else:
                    square = game.get_clicked_square(event.pos)
                    if square is not None:
                        move.new_pos = square
                        if move.piece.is_valid_move(square):
                            game.board.move_figure_to_position(move.piece, move.new_pos)
                            using_figure = False
                            game.move_draw(move)
                        else:
                            using_figure = False
                            continue
                    else:
                        continue
                    '''-когда флаг == Тру
                       мышкой выбираем клетку
                       проверка на совпадение с доступной
                       недоступная -> continue
                       иначе - ставим фигуру
                       при надобности - вызываем функцию для удаления фигуры противника
                       флаг = Ф'''
