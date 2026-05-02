import pygame
from gameconfig import Gameconfig

class Prince(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        super().__init__()
        self.image = Gameconfig.PRINCE_IMG
        self.rect = pygame.Rect(x, 200, Gameconfig.PRINCE_W, Gameconfig.PRINCE_H)
        self.rect.x = x
        self.rect.y = y

    def draw(self, window, seuil) :
        window.blit(self.image, (self.rect.x + seuil, self.rect.y))