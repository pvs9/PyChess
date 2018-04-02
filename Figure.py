from Coordinate import Coordinate as Position


class Figure:

    def __init__(self, side, position):
        self.side = side
        self.position = position

    def __eq__(self, other):
        if self.side == other.side and \
           self.position == other.position and \
           self.__class__ == other.__class__:
            return True
        return False

