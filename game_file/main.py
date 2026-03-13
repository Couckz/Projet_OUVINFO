""" 
fichier principale du jeu """
import pygame
from gameconfig import Gameconfig
from gamestate import Gamestate
from move import Move

def get_next_move():
    nextmove = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] : 
        nextmove.right = True
    if keys[pygame.K_LEFT] : 
        nextmove.left = True
    if keys[pygame.K_UP] :
        nextmove.jump = True
    return nextmove

def gameloop(window):
    quitting = False
    game_state = Gamestate()
    while not quitting : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        next_move = get_next_move()
        game_state.advance_state(next_move)
        game_state.draw(window)
        pygame.display.update()
        pygame.time.delay(20)
    
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((Gameconfig.LONGUEUR_LEVEL1, Gameconfig.LARGEUR_LEVEL1))
    pygame.display.set_caption("monjeu")
    Gameconfig.init()
    gameloop(window)
    pygame.quit()
    quit()