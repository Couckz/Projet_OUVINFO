""" 
contient la classe qui gère le joueur"""
import pygame
import math
from gameconfig import Gameconfig

class BG (pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("../img_file/niv.png").convert()

    def draw(self,window,seuil) :
        window.blit(self.image,(seuil,0))
