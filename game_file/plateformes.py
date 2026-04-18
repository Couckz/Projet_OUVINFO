import pygame

"""Gère les plateformes"""
class plateform(pygame.sprite.Sprite):
    def __init__(self):
        self.platforms_niv1 = [
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
        self.platforms_niv2 = [
            pygame.Rect(10, 305, 2475, 50), #sol
            pygame.Rect(0, 220, 500, 60),
            pygame.Rect(200, 75, 160, 30),
            pygame.Rect(445, 160, 160, 30),
            pygame.Rect(615, 100, 160, 30),
            pygame.Rect(795, 280, 60, 40),
            pygame.Rect(930, 280, 60, 40),
            pygame.Rect(1090, 280, 100, 40),
            pygame.Rect(900, 160, 330, 30),
            pygame.Rect(1190, 180, 30, 110),
            pygame.Rect(1000, 30, 160, 30),
            pygame.Rect(1210, 45, 160, 30),
            pygame.Rect(1250, 280, 160, 30),
            pygame.Rect(1375, 130, 160, 30),
            pygame.Rect(1500, 280, 160, 30),
            pygame.Rect(1670, 150, 160, 30),
            pygame.Rect(1910, 220, 160, 30),
            
]       
        self.platforms_niv3 = [
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