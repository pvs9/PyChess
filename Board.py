from King import King
from Coordinate import Coordinate as Position
from Move import Move

WHITE = True
BLACK = False


class Board:

    def __init__(self):
        self.figures = []
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False

        self.figures.extend([King(self, WHITE, Position(0, 0))])

    def get_current_side(self):
        return self.currentSide

    @staticmethod
    def move_figure_to_position(self, figure, position):
        figure.position = position

    @staticmethod
    def is_valid_position(self, position):
        if 0 <= position[0] <= 7 and 0 <= position[1] <= 7:
            return True
        else:
            return False
