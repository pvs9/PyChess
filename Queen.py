import pygame
import os

from Figure import Figure

WHITE = True
BLACK = False

class Queen(Figure):

    value = 100

    def __init__(self, board, side, position):
        super(Queen, self).__init__(board, side, position)
        if side is WHITE:
            self.image = pygame.image.load(os.path.join("images", "white_queen.png")).convert()
        else:
            self.image = pygame.image.load(os.path.join("images", "black_queen.png")).convert()
        self.name = "Queen"
        
    def valid_moves(self):
        valid_moves = []
        return valid_moves
        
    def attacks_positions(self):
        attacks=[]
        return attacks
                
    def is_valid_move(self, position):
        return False