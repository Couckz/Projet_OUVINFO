import pygame

"""Gère les plateformes"""
class plateform(pygame.sprite.Sprite):
    def __init__(self):
        self.platforms = [
            pygame.Rect(200, 200, 150, 20),
            pygame.Rect(500, 180, 150, 20),
]