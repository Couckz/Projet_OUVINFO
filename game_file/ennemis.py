"""contient la classe gérant les caractéristiques des ennemis"""
import pygame
from gameconfig import Gameconfig

class Ennemis(pygame.sprite.Sprite):
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vx = 0
        self.vy = 0
        self.position_level1 = [
            pygame.Rect(500, 225, 50, 60) #Monstre 1
        ]
        
        
        self.position_level2 = [
            
        ]
        self.position_level3 = [
            
        ]
        
        
