""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig
from player import *
from move import Move
from background import BG
from plateformes import plateform 
from cle import Cle
from ennemis import Ennemis
#Dessiner qd est ce qu'on s'arrête 
#Centralise la gestion
class Gamestate: 
    def __init__(self):
        self.game = Gameconfig()
        self.player = Player(80)
        self.cle = Cle()
        self.ennemi = Ennemis()
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
        pygame.draw.rect(window, (0, 0, 255), (self.bg.rectporte[self.bg.counter_niveau].x + self.seuil, self.bg.rectporte[self.bg.counter_niveau].y, self.bg.rectporte[self.bg.counter_niveau].width, self.bg.rectporte[self.bg.counter_niveau].height), 2) #debogage interface
        pygame.draw.rect(window, (0, 255, 0), (self.bg.rectvie.x, self.bg.rectvie.y,  self.bg.rectvie.width, self.bg.rectvie.height), 2)
        #print("window", self.seuil)
        #print("position x", self.player.rect.x)
        
        #Debogage, niveau 1
        if self.bg.counter_niveau == 0:
            for platform in self.platforms.platforms_niv1:
                pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
            for key in self.cle.cles_niv1:
                pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
            for position in self.ennemi.position_level1:
                pygame.draw.rect(window, (255, 255, 0), (position.x + self.seuil, position.y, position.width, position.height), 0)
        #Debogage, niveau 2
        if self.bg.counter_niveau == 1:
            for platform in self.platforms.platforms_niv2:
                pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
            for key in self.cle.cles_niv2:
                pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
        
        #Debogage, niveau3
        if self.bg.counter_niveau == 2:
            for platform in self.platforms.platforms_niv3:
                pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
            for key in self.cle.cles_niv3:
                pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
                
        
    def move_ennemi(self):
        if self.bg.counter_niveau == 0:
            print(self.bg.counter_niveau)
            seuil_bas = 450
            seuil_haut = 600
            seuil_b = seuil_bas
            seuil_h = seuil_haut
            for positions in self.ennemi.position_level1:
                seuil_bas = positions.x - 20
                seuil_haut = positions.x + 20
                if positions.x <= seuil_h:
                    positions.x = positions.x+5
                elif min(positions.x, seuil_bas) != positions.x :
                        positions.x = positions.x-5
        
            
    def collision(self):
        #self.player.on_ground = False
        if self.bg.counter_niveau == 0:
            for platforme in self.platforms.platforms_niv1:
                if platforme.colliderect(self.player.rect):
                    if self.player.vy > 0:  # le joueur tombe
                        if self.player.rect.bottom >= platforme.top:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        
                    elif self.player.vy < 0:  # le joueur monte
                        if self.player.rect.top <= platforme.bottom:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0
                        
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:  # vers la droite
                            self.player.rect.right = platforme.left
                            self.player.vx = 0
                        elif self.player.vx < 0:  # vers la gauche
                            self.player.rect.left = platforme.right
                            self.player.vx = 0
        
        if self.bg.counter_niveau == 1:
            for platforme in self.platforms.platforms_niv2:
                if platforme.colliderect(self.player.rect):
                    if self.player.vy > 0:  # le joueur tombe
                        if self.player.rect.bottom >= platforme.top:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        
                    elif self.player.vy < 0:  # le joueur monte
                        if self.player.rect.top <= platforme.bottom:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0
                        
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:  # vers la droite
                            self.player.rect.right = platforme.left
                        elif self.player.vx < 0:  # vers la gauche
                            self.player.rect.left = platforme.right
                            self.player.vx = 0
        
        if self.bg.counter_niveau == 2:
            for platforme in self.platforms.platforms_niv3:
                if platforme.colliderect(self.player.rect):
                    if self.player.vy > 0:  # le joueur tombe
                        if self.player.rect.bottom >= platforme.top:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        
                    elif self.player.vy < 0:  # le joueur monte
                        if self.player.rect.top <= platforme.bottom:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0
                        
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:  # vers la droite
                            self.player.rect.right = platforme.left
                        elif self.player.vx < 0:  # vers la gauche
                            self.player.rect.left = platforme.right
                            self.player.vx = 0
        
    def collision_cle(self):
        if self.cle.counter_clelevel == 0:
            for cle in self.cle.cles_niv1:
                if cle.colliderect(self.player.rect):
                    self.cle.cles_niv1.remove(cle)
                    self.bg.counter+=1
        
        if self.cle.counter_clelevel == 1:
            for cle in self.cle.cles_niv2:
                if cle.colliderect(self.player.rect):
                    self.cle.cles_niv2.remove(cle)
                    self.bg.counter+=1
        
        if self.cle.counter_clelevel == 2:
            for cle in self.cle.cles_niv3:
                if cle.colliderect(self.player.rect):
                    self.cle.cles_niv3.remove(cle)
                    self.bg.counter+=1
                    
        if self.bg.rectporte[self.bg.counter_niveau].colliderect(self.player.rect) and self.bg.counter == 3:
                self.bg.counter_niveau+=1
                self.cle.counter_clelevel+=1
                self.bg.counter = 0
                self.seuil = 0
                self.player = Player(50)
                #print("Jeu fini")
        
    def fin_jeu(self):
        if -self.seuil >= self.player.rect.x:
            return True
    
    def ecran_fin_jeu(self, window):
        self.bg.draw_end(window)
        #Debug
        pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[0].x, self.bg.rectbutton[0].y, self.bg.rectbutton[0].width, self.bg.rectbutton[0].height), 2)
        if self.bg.click >= 1:
            self.player = Player(80)
            self.cle = Cle() 
            self.bg.counter_niveau = 0
            self.bg.counter = 0
            self.bg.start = 0
            self.cle.counter_clelevel = 0
            self.seuil = 0
            self.bg.click = 0
    
    def debut_jeu(self,window):
        if self.bg.counter_niveau == 5:
            self.bg.draw_start(window)
            if self.bg.start_click >= 1:
                self.player = Player(80)
                self.cle = Cle() 
                self.bg.counter_niveau = 0
                self.bg.counter = 0
                self.bg.start = 0
                self.cle.counter_clelevel = 0
                self.seuil = 0
                self.bg.click = 0
            pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[1].x, self.bg.rectbutton[1].y, self.bg.rectbutton[1].width, self.bg.rectbutton[1].height), 2)
        