from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn

WHITE = True
BLACK = False


class Board:

    def __init__(self):
        self.figures = []
        self.current_side = WHITE
        self.checkmate = False
        self.size = 8
        # добавляем в массив фигур фигуры
        self.figures.extend([King(self, WHITE, (4, 7)),
                             King(self, BLACK, (4, 0)),
                             Queen(self, WHITE, (3, 7)),
                             Queen(self, BLACK, (3, 0)),
                             Rook(self, WHITE, (0, 7)),
                             Rook(self, WHITE, (7, 7)),
                             Rook(self, BLACK, (0, 0)),
                             Rook(self, BLACK, (7, 0)),
                             Knight(self, WHITE, (1, 7)),
                             Knight(self, WHITE, (6, 7)),
                             Knight(self, BLACK, (1, 0)),
                             Knight(self, BLACK, (6, 0)),
                             Bishop(self, WHITE, (2, 7)),
                             Bishop(self, WHITE, (5, 7)),
                             Bishop(self, BLACK, (2, 0)),
                             Bishop(self, BLACK, (5, 0)),
                             Pawn(self, WHITE, (0, 6)),
                             Pawn(self, WHITE, (1, 6)),
                             Pawn(self, WHITE, (2, 6)),
                             Pawn(self, WHITE, (3, 6)),
                             Pawn(self, WHITE, (4, 6)),
                             Pawn(self, WHITE, (5, 6)),
                             Pawn(self, WHITE, (6, 6)),
                             Pawn(self, WHITE, (7, 6)),
                             Pawn(self, BLACK, (0, 1)),
                             Pawn(self, BLACK, (1, 1)),
                             Pawn(self, BLACK, (2, 1)),
                             Pawn(self, BLACK, (3, 1)),
                             Pawn(self, BLACK, (4, 1)),
                             Pawn(self, BLACK, (5, 1)),
                             Pawn(self, BLACK, (6, 1)),
                             Pawn(self, BLACK, (7, 1))])

    def get_current_side(self):
        return self.current_side

    @staticmethod
    def move_figure_to_position(figure, position):
        figure.position = position

    @staticmethod
    def is_valid_position(self, position):
        if 0 <= position[0] < self.size and 0 <= position[1] < self.size:
            return True
        else:
            return False

    def find_figure(self, position):
        for figure in self.figures:
            if figure.position[0] == position[0] and figure.position[1] == position[1]:
                return figure
        return None

