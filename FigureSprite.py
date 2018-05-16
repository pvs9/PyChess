'''не используется'''s
import pygame


class FigureSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.old = (0, 0, 0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self, position):
        self.old = self.rect
        self.rect = self.rect.move([position[0] - self.rect.x, position[1] - self.rect.y])

