from Figure import Figure
from Coordinate import Coordinate


class King(Figure):

    def __init__(self, side, position):
        super(King, self).__init__(side, position)
        self.name = "Король"
