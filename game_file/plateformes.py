import pygame

"""Gère les plateformes"""
class plateform(pygame.sprite.Sprite):
    def __init__(self):
        self.platforms_niv1 = [
            pygame.Rect(10, 285, 2475, 60), #sol
            pygame.Rect(840, 180, 90, 25),   #plat2
            pygame.Rect(340, 180, 250, 25), #plat 1
            pygame.Rect(930, 260, 70, 25), #plat3
            pygame.Rect(987, 230, 80, 25), #plat4
            pygame.Rect(1420, 260, 140, 25), #plat5
            pygame.Rect(1550, 190, 130, 30), #plat6
            pygame.Rect(1690, 160, 130, 25),
            pygame.Rect(2020, 170, 130, 25),
            pygame.Rect(2170, 260, 130, 25),
]       
        self.platforms_niv2 = [
            pygame.Rect(0, 305, 2420, 150), #sol
            pygame.Rect(0, 220, 480, 50), #plateforme 1
            pygame.Rect(220, 75, 160, 30),
            pygame.Rect(450, 145, 160, 30),
            pygame.Rect(645, 75, 160, 30),
            pygame.Rect(755, 200, 60, 25),
            pygame.Rect(825, 280, 70, 30),
            pygame.Rect(960, 280, 60, 40),
            pygame.Rect(1090, 280, 100, 40),
            pygame.Rect(905, 130, 330, 30),
            pygame.Rect(1185, 160, 30, 130),
            pygame.Rect(1250, 280, 160, 30),
            pygame.Rect(1360, 148, 160, 30),
            pygame.Rect(1500, 280, 160, 30),
            pygame.Rect(1650, 200, 160, 30),
            pygame.Rect(1910, 220, 160, 30),
            
]       
        self.platforms_niv3 = [
            pygame.Rect(10, 320, 2475, 40), #sol
            pygame.Rect(280, 190, 120, 20), 
            pygame.Rect(520, 80, 110, 25),
            pygame.Rect(650, 130, 100, 25),
            pygame.Rect(750, 170, 110, 25),
            pygame.Rect(960, 190, 30, 110),
            pygame.Rect(990, 160, 70, 35),
            pygame.Rect(1055, 150, 70, 35),
            pygame.Rect(1095, 130, 70, 35),
            pygame.Rect(1270, 120, 110, 35),
            pygame.Rect(1500, 155, 110, 30),
            pygame.Rect(1730, 155, 10, 90),
            pygame.Rect(1820, 95, 110, 20),
            pygame.Rect(1920, 95, 20, 200),
            pygame.Rect(2200, 260, 20, 100),
            pygame.Rect(2225, 250, 110, 20),
            
            
]
        
        self.plateforms_niv4 =  [
            pygame.Rect(0,300,675, 44),
            pygame.Rect(400, 220, 150, 20),
            pygame.Rect(100, 220, 150, 20), 
            pygame.Rect(250, 150, 150, 20)
        ]