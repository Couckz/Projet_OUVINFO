""" 
Ce fichier définit les constantes du jeu qui ne sont pas
modifiés"""
import pygame

class Gameconfig:
    BACKGROUND_LEVEL1 = None
    LARGEUR_LEVEL1 = 885
    LONGUEUR_LEVEL1 = 1595
    WINDOW_H = 640
    WINDOW_W = 960
    BACKGROUND_LEVEL2 = None
    BACKGROUND_LEVEL3 = None
    STANDING_IMG = None
    Y_PLATEFORM = 415
    PLAYER_W = 64
    PLAYER_H = 64
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 9.81
    FORCE_JUMP = -100
    
    def init():
        Gameconfig.BACKGROUND_LEVEL1 = pygame.image.load("/Users/bensemmanecamelia/Desktop/OUVINFO/Projet_OUVINFO/img_file/level1.jpeg")
        Gameconfig.STANDING_IMG = pygame.image.load("/Users/bensemmanecamelia/Desktop/OUVINFO/Projet_OUVINFO/img_file/princesse_stand.png")
            # Gameconfig.BACKGROUND_LEVEL2 = pygame.image.load("img_file/level2.jpeg")
            # Gameconfig.BACKGROUND_LEVEL3 = pygame.image.load("img_file/level3.jpeg")
            # Gameconfig.STANDING_IMG = pygame.image.load('ressources/standing.png')