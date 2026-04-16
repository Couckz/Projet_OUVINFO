import pygame

"""Gère les plateformes"""
class plateform(pygame.sprite.Sprite):
    def __init__(self):
        self.platforms = [
            pygame.Rect(830, 180, 90, 20),
            pygame.Rect(340, 180, 240, 25),
            pygame.Rect(920, 260, 70, 25),
            pygame.Rect(987, 230, 100, 25),
            pygame.Rect(1420, 260, 130, 25),
            pygame.Rect(1550, 200, 130, 25),
            pygame.Rect(1690, 160, 130, 25),
            pygame.Rect(2020, 160, 130, 25),
            pygame.Rect(2170, 260, 130, 25),
]