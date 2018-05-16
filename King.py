import pygame
import os

from Figure import Figure

WHITE = True
BLACK = False

class King(Figure):

    value = 100

    def __init__(self, board, side, position):
        super(King, self).__init__(board, side, position)
        if side is WHITE:
            self.image = pygame.image.load(os.path.join("images", "white_king.png")).convert()
        else:
            self.image = pygame.image.load(os.path.join("images", "black_king.png")).convert()
        self.name = "King"
        
    def valid_moves(self):
        valid_moves = []
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.is_valid_move(tuple([i, j])) == True:
                    valid_moves.append((i, j))
        return valid_moves
        
    def attacks_positions(self):
        attacks=[]
        for i in range(self.position[0]-1, self.position[0]+2):
            for j in range(self.position[1]-1, self.position[1]+2):
                if self.board.is_valid_position(self.board, (i, j)):
                    attacks.append((i, j))
        return attacks
                
    def is_valid_move(self, position):
        if abs(position[0] - self.position[0]) <= 1 and abs(position[1] - self.position[1]) <= 1:
            figure = self.board.find_figure(position)
            if (figure and figure.side is not self.side and figure.name != "King") or (not figure):
                return True
            else:
                return False
        else:
            return False
