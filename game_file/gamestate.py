""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig
from player import *
from move import Move

class Gamestate: 
    def __init__(self):
        self.player = Player(12)
    
    def draw(self, window):
        window.blit(Gameconfig.BACKGROUND_LEVEL1, (0,0))
        self.player.draw(window)
        
    def advance_state(self, next_move):
        self.player.advance_state(next_move)
    