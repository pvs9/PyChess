from King import King


WHITE = True
BLACK = False


class Board:

    def __init__(self):
        self.figures = []
        self.currentSide = WHITE
        self.checkmate = False
        self.size = 8
        # добавляем в массив фигур фигуры
        self.figures.extend([King(self, WHITE, (0, 0))])

    def get_current_side(self):
        return self.currentSide

    @staticmethod
    def move_figure_to_position(self, figure, position):
        figure.position = position

    @staticmethod
    def is_valid_position(self, position):
        if 0 <= position[0] < self.size and 0 <= position[1] < self.size:
            return True
        else:
            return False
