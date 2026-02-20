""" 
Ce fichier définit les constantes du jeu qui ne sont pas
modifiés"""
import pygame

class Gameconfig:
    BACKGROUND_LEVEL1 = None
    LARGEUR_LEVEL1 = 885
    LONGUEUR_LEVEL1 = 1595
    BACKGROUND_LEVEL2 = None
    BACKGROUND_LEVEL3 = None
    STANDING_IMG = None
    
    def init():
            Gameconfig.BACKGROUND_LEVEL1 = pygame.image.load("/Users/bensemmanecamelia/Desktop/OUVINFO/projet/Projet_OUVINFO/img_file/level1.jpeg")
            # Gameconfig.BACKGROUND_LEVEL2 = pygame.image.load("img_file/level2.jpeg")
            # Gameconfig.BACKGROUND_LEVEL3 = pygame.image.load("img_file/level3.jpeg")
            # Gameconfig.STANDING_IMG = pygame.image.load('ressources/standing.png')