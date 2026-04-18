""" 
contient la classe qui gère le joueur"""
import pygame
import math
from gameconfig import Gameconfig

class BG (pygame.sprite.Sprite):
    def __init__(self):
        self.counter_niveau = 0
        self.image = [pygame.image.load("../img_file/niv.png").convert(),
                    pygame.image.load("../img_file/niv2.png").convert(),
                    pygame.image.load("../img_file/level3.jpeg").convert(),]
        self.counter = 0
        self.rectcle = pygame.Rect(20, 10, 130, 70)
        self.rectporte = [pygame.Rect(2350, 185, 85, 100),
                          pygame.Rect(2230, 185, 85, 100),
                          pygame.Rect(2350, 185, 85, 100)]
        self.imgcle = [
            pygame.image.load("../img_file/cle0.png"),
            pygame.image.load("../img_file/cle1.png"),
            pygame.image.load("../img_file/cle2.png"),
            pygame.image.load("../img_file/cle3.png")
        ]

    def draw(self,window,seuil) :
        #Dessiner l'arrière plan
        if self.counter_niveau == 0:
            window.blit(self.image[0],(seuil,0))
        if self.counter_niveau == 1:
            window.blit(self.image[1],(seuil,0))
        if self.counter_niveau == 2:
            window.blit(self.image[2],(seuil,0))
        
        
        #Dessiner le compteur des clés
        if self.counter == 0:
            window.blit(self.imgcle[0], (self.rectcle.x , self.rectcle.y))
        if self.counter == 1:
            window.blit(self.imgcle[1], (self.rectcle.x , self.rectcle.y))
        if self.counter == 2:
            window.blit(self.imgcle[2], (self.rectcle.x , self.rectcle.y))
        if self.counter == 3:
            window.blit(self.imgcle[3], (self.rectcle.x , self.rectcle.y))
    