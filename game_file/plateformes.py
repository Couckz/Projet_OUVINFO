import pygame

"""Gère les plateformes"""
class plateform(pygame.sprite.Sprite):
    def __init__(self):
        self.platforms = [
            pygame.Rect(10, 285, 2475, 60), #sol
            pygame.Rect(830, 180, 90, 20), 
            pygame.Rect(350, 170, 240, 25),
            pygame.Rect(940, 260, 70, 25),
            pygame.Rect(987, 230, 100, 25),
            pygame.Rect(1420, 260, 130, 25),
            pygame.Rect(1550, 190, 130, 25),
            pygame.Rect(1690, 160, 130, 25),
            pygame.Rect(2020, 160, 130, 25),
            pygame.Rect(2170, 260, 130, 25),
]