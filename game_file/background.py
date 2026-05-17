""" 
contient la classe qui gère le joueur"""
import pygame
import math
from gameconfig import Gameconfig

class BG (pygame.sprite.Sprite):
    def __init__(self):
        self.counter_niveau = 5 #Variable qui sert à compter les niveaux et pour l'affichage
        self.image = [pygame.image.load("../img_file/niv.png").convert(),
                    pygame.image.load("../img_file/l.png").convert(),
                    pygame.image.load("../img_file/level.png").convert(),
                    pygame.image.load("../img_file/perdu.png").convert(),
                    pygame.image.load("../img_file/ee.png").convert(),
                    pygame.image.load("../img_file/skin2.png").convert(),
                    pygame.image.load("../img_file/jeu.png").convert(), 
                    pygame.image.load("../img_file/final.png").convert_alpha(),
                    pygame.image.load("../img_file/level_findejeu.png").convert(),
                    pygame.image.load("../img_file/image_fin.png").convert(),
                    pygame.image.load("../img_file/bouton_fin.png").convert()]
        self.click = 0
        self.start_click = 0
        self.rectbutton = [
            pygame.Rect(200, 180, 250, 70),
            pygame.Rect(225, 160, 220, 80),
            pygame.Rect(215,160,240,100)
        ]
        self.counter = 0 #Variable qui sert pour l'affichage du compteur des clés
        
        self.rectcle = pygame.Rect(20, 10, 130, 70)
        self.rectporte = [pygame.Rect(2350, 185, 85, 100), #level 1
                          pygame.Rect(2190, 185, 85, 100), #level 2
                          pygame.Rect(2350, 185, 85, 100), #level 3
                          pygame.Rect(310,220,40,64), #Pour le prince
                          #pygame.Rect(2350, 185, 85, 100),
                          #pygame.Rect(2350, 185, 85, 100),
                          #pygame.Rect(2350, 185, 85, 100)
                          ]
        self.imgcle = [
            pygame.image.load("../img_file/cle0.png"),
            pygame.image.load("../img_file/cle1.png"),
            pygame.image.load("../img_file/cle2.png"),
            pygame.image.load("../img_file/cle3.png")
        ]
        self.start = 0
        self.vie = 3
        self.rectvie = pygame.Rect(240, 10, 250, 60)
        self.imgvie = [
            pygame.image.load("../img_file/full.png"),
            pygame.image.load("../img_file/demi.png"),
            pygame.image.load("../img_file/low.png")
        ]
        
        self.image_prince = pygame.image.load("../img_file/prince2.png")
        
        

    def draw(self,window,seuil) :
        #Dessiner l'arrière plan
        
        #Niveau 1
        if self.counter_niveau == 0:
            window.blit(self.image[0],(seuil,0))
        #Niveau 2
        if self.counter_niveau == 1:
            window.blit(self.image[1],(seuil,0))
        #Niveau 3
        if self.counter_niveau == 2:
            window.blit(self.image[2],(seuil,0))
            
        #Niveau avec le prince
        if self.counter_niveau == 3:
            window.blit(self.image[8], (seuil, 0))
        
        if self.counter_niveau == 4 :
            window.blit(self.image[9], (seuil, 0))
        
        #Dessiner le compteur des clés
        if self.counter_niveau < 3:
            if self.counter == 0:
                window.blit(self.imgcle[0], (self.rectcle.x , self.rectcle.y))
            if self.counter == 1:
                window.blit(self.imgcle[1], (self.rectcle.x , self.rectcle.y))
            if self.counter == 2:
                window.blit(self.imgcle[2], (self.rectcle.x , self.rectcle.y))
            if self.counter == 3:
                window.blit(self.imgcle[3], (self.rectcle.x , self.rectcle.y))
        else:
            window.blit(self.image_prince, (self.rectporte[3].x, self.rectporte[3].y))
    

    def draw_end(self, window):
        self.souris = pygame.mouse.get_pos()
        window.blit(self.image[3], (0,0))
        window.blit(self.image[4], (self.rectbutton[0].x, self.rectbutton[0].y))
        if self.rectbutton[0].collidepoint(self.souris):
                window.blit(self.image[5], (self.rectbutton[0].x, self.rectbutton[0].y))
                if pygame.mouse.get_pressed()[0]:  
                    if self.rectbutton[0].collidepoint(pygame.mouse.get_pos()):
                        self.click+=1
    
    def draw_start(self, window):
        self.souris = pygame.mouse.get_pos()
        window.blit(self.image[6], (0,0))
        window.blit(self.image[7], (self.rectbutton[1].x, self.rectbutton[1].y))
        if self.rectbutton[0].collidepoint(self.souris):
                window.blit(self.image[7], (self.rectbutton[1].x, self.rectbutton[1].y))
                if pygame.mouse.get_pressed()[0]:  
                    print(self.image[7].get_size())
                    if self.rectbutton[0].collidepoint(pygame.mouse.get_pos()):
                        self.start_click +=1