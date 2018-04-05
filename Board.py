from King import King


WHITE = True
BLACK = False


class Board:

    def __init__(self):
        self.figures = []
        self.current_side = WHITE
        self.checkmate = False
        self.size = 8
        # добавляем в массив фигур фигуры
        self.figures.extend([King(self, WHITE, (0, 2)),
                             King(self, BLACK, (0, 0))])

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

