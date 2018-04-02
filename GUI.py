import pygame
import os

from Coordinate import Coordinate as Position


class PyChessGUI:

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((850, 500))
        self.boardStart_x = 50
        self.boardStart_y = 50
        pygame.display.set_caption('Python Chess')
        self.square_size = 50
        self.white_square = pygame.image.load(os.path.join("images", "white_square.png")).convert()
        self.black_square = pygame.image.load(os.path.join("images", "black_square.png")).convert()

        self.white_king = pygame.image.load(os.path.join("images", "White_King.png")).convert()
        self.white_king = pygame.transform.scale(self.white_king, (self.square_size, self.square_size))

        self.fontDefault = pygame.font.Font(None, 20)

    def convert_to_chess_coords(self, screen_position):
        (x, y) = screen_position
        row = (y - self.boardStart_y) / self.square_size
        col = (x - self.boardStart_x) / self.square_size
        return Position(row, col)

    def convert_to_screen_coords(self, position):
        (row, col) = position
        screen_x = self.boardStart_x + col * self.square_size
        screen_y = self.boardStart_y + row * self.square_size
        return (screen_x, screen_y)
