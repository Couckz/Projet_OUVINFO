""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig
from player import *
from move import Move
from background import BG
from plateformes import plateform 
#Dessiner qd est ce qu'on s'arrête 
#Centralise la gestion
class Gamestate: 
    def __init__(self):
        self.player = Player(20)
        self.seuil = 0
        self.bg = BG()
        self.platforms = plateform()

    def advance_state(self, next_move):
        self.player.advance_state(next_move)
        self.seuil = max(self.seuil+Gameconfig.D_SEUIL, Gameconfig.seuil_max)
    
    def draw(self, window):
        self.bg.draw(window, self.seuil)
        self.player.draw(window, self.seuil)
        for platform in self.platforms.platforms:
            pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 0)
            self.player.draw(window, self.seuil)