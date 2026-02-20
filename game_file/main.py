""" 
fichier principale du jeu """

import pygame
from gameconfig import Gameconfig

def gameloop():
    quitting = False
    while not quitting : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

    
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((Gameconfig.LONGUEUR_LEVEL1, Gameconfig.LARGEUR_LEVEL1))
    Gameconfig.init()
    gameloop()
    pygame.quit()
    quit()