""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig
from player import *
from move import Move
from background import BG

class Gamestate: 
    

    def __init__(self):
        self.player = Player(12)
        self.seuil = 0 
        self.bg = BG()
    
     
    def draw(self, window):
        # window.blit(Gameconfig.BACKGROUND_LEVEL1, (0,0))
        self.bg.draw(window,self.seuil)
        self.player.draw(window)

     
    def advance_state(self, next_move):
        self.player.advance_state(next_move)
        self.seuil = max(self.seuil+Gameconfig.D_SEUIL, Gameconfig.seuil_max)
    