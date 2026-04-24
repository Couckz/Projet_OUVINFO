""" 
fichier principale du jeu """
import pygame
from gameconfig import Gameconfig
from gamestate import Gamestate
from move import Move
from player import Player
from background import BG

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
        if game_state.bg.counter_niveau == 5:
            game_state.debut_jeu(window)
        else :
            next_move = get_next_move()
            game_state.advance_state(next_move)
            game_state.draw(window)
            game_state.move_ennemi()
            game_state.collision()
            game_state.collision_cle()
            if game_state.fin_jeu():
                game_state.ecran_fin_jeu(window)
                #quitting = True
        pygame.display.update()
        pygame.time.delay(20)
    
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((Gameconfig.LONGUEUR_LEVEL1, Gameconfig.LARGEUR_LEVEL1))
    pygame.display.set_caption("monjeu")
    Gameconfig.init()
    Player.init_sprites()
    gameloop(window)
    pygame.quit()
    quit()