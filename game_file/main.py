""" 
fichier principale du jeu """

import pygame
from gameconfig import Gameconfig
from gamestate import Gamestate

def gameloop(window):
    quitting = False
    game_state = Gamestate()
    while not quitting : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            game_state.draw(window)
            pygame.display.update()

    
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((Gameconfig.LONGUEUR_LEVEL1, Gameconfig.LARGEUR_LEVEL1))
    pygame.display.set_caption("Avoid Bats")
    Gameconfig.init()
    gameloop(window)
    pygame.quit()
    quit()