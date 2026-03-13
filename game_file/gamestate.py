""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig

class Gamestate: 
    def __init__(self):
        pass
    
    def draw(self, window):
        window.blit(Gameconfig.BACKGROUND_LEVEL1, (0,0))