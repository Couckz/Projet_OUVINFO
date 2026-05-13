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

def countdown(window):
    font = pygame.font.SysFont("Arial", 80, bold=True)
    for i in range(3, 0, -1):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 1000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            window.fill((0, 0, 0))
            texte = font.render(str(i), True, (255, 255, 255))
            ombre = font.render(str(i), True, (80,80,80))
            x = Gameconfig.LONGUEUR_LEVEL1 // 2 - texte.get_width() // 2
            y = Gameconfig.LARGEUR_LEVEL1 // 2 - texte.get_height() // 2
            window.blit(ombre, (x+4, y+4))
            window.blit(texte, (x,y))
            pygame.display.update()
            pygame.time.delay(20)

def gameloop(window):
    quitting = False
    game_state = Gamestate()
    game_state.bg.counter_niveau = 5
    countdown_done = False
    game_state.collision_cle()


    #game_state.bg.counter_niveau = 3
    
    while not quitting : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

        niveau_avant = game_state.bg.counter_niveau

        if game_state.bg.counter_niveau == 5:
            game_state.debut_jeu(window)
            if game_state.bg.counter_niveau == 2 and not countdown_done:
                countdown(window)
                countdown_done = True

        elif game_state.bg.counter_niveau == 3  and game_state.fin_atteinte :
            game_state.dessiner_fin(window)
            if game_state.player.rect.colliderect(game_state.prince.rect) :
                game_state.fin_atteinte = True
                game_state.bg.counter_niveau = 4
        
        elif game_state.bg.counter_niveau == 4  :
            game_state.dessiner_fin(window)
            
        else :
            next_move = get_next_move()
            game_state.advance_state(next_move)
            game_state.draw(window)
            game_state.collision()
            game_state.collision_cle()
            if game_state.fin_jeu():
                game_state.ecran_fin_jeu(window)
                #quitting = True
            if game_state.bg.counter_niveau != niveau_avant:
                countdown(window)
        if game_state.recommencer_niveau:
            game_state.recommencer_niveau = False
            countdown(window)

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