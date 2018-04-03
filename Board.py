from King import King
from Coordinate import Coordinate as Position
from Move import Move

WHITE = True
BLACK = False


class Board:

    def __init__(self):
        self.figures = []
        self.currentSide = WHITE
        self.checkmate = False
        #добавляем в массив фигур фигуры
        self.figures.extend([King(self, WHITE, (0, 0))])

    def get_current_side(self):
        return self.currentSide
''' '''
    @staticmethod
    def move_figure_to_position(self, figure, position):
        figure.position = position

    @staticmethod
    def is_valid_position(self, position):
        if 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
            return True
        else:
            return False
