""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig
from player import *
from move import Move
from background import BG
from plateformes import plateform 
from cle import Cle
#Dessiner qd est ce qu'on s'arrête 
#Centralise la gestion
class Gamestate: 
    def __init__(self):
        self.game = Gameconfig()
        self.player = Player(60)
        self.cle = Cle()
        self.seuil = 0
        self.bg = BG()
        self.platforms = plateform()

    def advance_state(self, next_move):
        self.player.advance_state(next_move)
        self.seuil = max(self.seuil+Gameconfig.D_SEUIL, Gameconfig.seuil_max)
    
    def draw(self, window):
        self.bg.draw(window, self.seuil)
        self.player.draw(window, self.seuil)
        self.cle.draw(window, self.seuil)
        pygame.draw.rect(window, (0, 255, 0), (self.bg.rectcle.x, self.bg.rectcle.y, self.bg.rectcle.width, self.bg.rectcle.height), 2) #debogage interface
        pygame.draw.rect(window, (0, 0, 255), (self.bg.rectporte.x + self.seuil, self.bg.rectporte.y, self.bg.rectporte.width, self.bg.rectporte.height), 2) #debogage interface
        
        print("window", self.seuil)
        print("position x", self.player.rect.x)
        for platform in self.platforms.platforms:
            pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 0)
        
        for key in self.cle.cles:
            pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
        
    
    def collision(self):
        for platform in self.platforms.platforms:
            if platform.colliderect(self.player.rect):
                self.player.vx = 0
                self.player.vy = 0
    
    def collision_cle(self):
        for cle in self.cle.cles:
            if cle.colliderect(self.player.rect):
                self.cle.cles.remove(cle)
                self.bg.counter+=1
                
        if self.bg.rectporte.colliderect(self.player.rect) and self.bg.counter == 3:
                self.bg.counter_niveau+=1
                self.bg.counter = 0
                self.seuil = 0
                print("Jeu fini")
        
    def fin_jeu(self):
        if -self.seuil == self.player.rect.x:
            return True
    
    def ecran_fin_jeu(self):
        pass