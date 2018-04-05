import pygame
import os

from Figure import Figure


class King(Figure):

    value = 100

    def __init__(self, board, side, position):
        super(King, self).__init__(board, side, position)
        self.image = pygame.image.load(os.path.join("images", "White_King.png")).convert()
        self.name = "King"

    def is_valid_move(self, position):
        if abs(position[0] - self.position[0]) <= 1 and abs(position[1] - self.position[1]) <= 1:
            return True
        else:
            return False
