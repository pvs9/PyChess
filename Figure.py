class Figure:

    def __init__(self, board, side, position):
        self.board = board
        self.side = side
        self.position = position
        self.if_moved = False

    def __eq__(self, other):
        if self.board == other.board and \
           self.side == other.side and \
           self.position == other.position and \
           self.__class__ == other.__class__:
            return True
        return False

