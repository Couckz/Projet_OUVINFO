""" 
Ce fichier définit l'état actuel du jeu"""
from gameconfig import Gameconfig
from player import *
from move import Move
from background import BG
from plateformes import plateform 
from cle import Cle

class Gamestate: 
    def __init__(self):
        self.just_changed_level = False
        self.state = "playing" 
        self.game = Gameconfig()
        self.player = Player(80)
        self.cle = Cle()
        self.seuil = 0
        self.bg = BG()
        self.platforms = plateform()
        self.fin_atteinte = False 
        

    def advance_state(self, next_move):
        if self.just_changed_level:
            self.just_changed_level = False
            return
        self.player.advance_state(next_move)
        if self.bg.counter_niveau < 3:
            self.seuil = max(self.seuil+Gameconfig.D_SEUIL, Gameconfig.seuil_max)
        else:
            self.seuil = 0
    
    def draw(self, window):
        self.bg.draw(window, self.seuil)
        self.player.draw(window, self.seuil)
        self.cle.draw(window, self.seuil)
        
        pygame.draw.rect(window, (0, 255, 0), (self.bg.rectcle.x, self.bg.rectcle.y, self.bg.rectcle.width, self.bg.rectcle.height), 2) #debogage interface
        pygame.draw.rect(window, (0, 0, 255), (self.bg.rectporte[self.bg.counter_niveau].x + self.seuil, self.bg.rectporte[self.bg.counter_niveau].y, self.bg.rectporte[self.bg.counter_niveau].width, self.bg.rectporte[self.bg.counter_niveau].height), 2) #debogage interface
        
        
        #Debogage, niveau 1
        if self.bg.counter_niveau == 0:
            for platform in self.platforms.platforms_niv1:
                pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
            for key in self.cle.cles_niv1:
                pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
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
                
        #Debogage, niveau4
        if self.bg.counter_niveau == 3:
            for platform in self.platforms.platforms_niv4:
                pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
            
            

    def collision(self):
        if self.bg.counter_niveau == 0:
                platforms = self.platforms.platforms_niv1
                self.player.rect.x += self.player.vx * Gameconfig.DT
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:
                            self.player.rect.right = platforme.left
                        elif self.player.vx < 0:
                            self.player.rect.left = platforme.right

                self.player.rect.y += self.player.vy * Gameconfig.DT
                self.player.on_ground = False
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vy > 0:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        elif self.player.vy < 0:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0
            
        if self.bg.counter_niveau == 1:
                platforms = self.platforms.platforms_niv2
                self.player.rect.x += self.player.vx * Gameconfig.DT
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:
                            self.player.rect.right = platforme.left
                        elif self.player.vx < 0:
                            self.player.rect.left = platforme.right

                self.player.rect.y += self.player.vy * Gameconfig.DT
                self.player.on_ground = False
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vy > 0:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        elif self.player.vy < 0:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0
                            
        if self.bg.counter_niveau == 2:
                platforms = self.platforms.platforms_niv3
                self.player.rect.x += self.player.vx * Gameconfig.DT
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:
                            self.player.rect.right = platforme.left
                        elif self.player.vx < 0:
                            self.player.rect.left = platforme.right

                self.player.rect.y += self.player.vy * Gameconfig.DT
                self.player.on_ground = False
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vy > 0:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        elif self.player.vy < 0:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0     
        
        if self.bg.counter_niveau == 3:
                platforms = self.platforms.platforms_niv4
                self.player.rect.x += self.player.vx * Gameconfig.DT
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vx > 0:
                            self.player.rect.right = platforme.left
                        elif self.player.vx < 0:
                            self.player.rect.left = platforme.right

                self.player.rect.y += self.player.vy * Gameconfig.DT
                self.player.on_ground = False
                for platforme in platforms:
                    if self.player.rect.colliderect(platforme):
                        if self.player.vy > 0:
                            self.player.rect.bottom = platforme.top
                            self.player.vy = 0
                            self.player.on_ground = True
                        elif self.player.vy < 0:
                            self.player.rect.top = platforme.bottom
                            self.player.vy = 0
                

        
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
                self.just_changed_level = True
                self.bg.counter_niveau += 1
                self.cle.counter_clelevel += 1
                self.bg.counter = 0
    
    def changement_niveau(self):
        self.state = "transition"
        time.sleep(0.001)
        Gameconfig.GRAVITY = 0
        self.player = Player(80)
        self.player.rect.y = 170
        self.seuil = 0
        self.player.vx = 0
        self.player.vy = 0
        
        
    def fin_jeu(self):
        if self.state != "playing":
            return False
        if self.bg.counter_niveau < 3:
                if self.player.rect.x + self.seuil < 0:
                    return True
            
            
    
    def ecran_fin_jeu(self, window):
        self.bg.draw_end(window)
        #Debug NE PAS TOUCHER
        pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[0].x, self.bg.rectbutton[0].y, self.bg.rectbutton[0].width, self.bg.rectbutton[0].height), 2)
        if self.bg.click >= 1:
            self.state = "playing" 
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
                self.bg.counter_niveau = 0 ##A mettre à 3 pour se rendre directement à la scène du prince
                self.bg.counter = 0
                self.bg.start = 0
                self.cle.counter_clelevel = 0
                self.seuil = 0
                self.bg.click = 0
                self.bg.start_click = 0
            pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[1].x, self.bg.rectbutton[1].y, self.bg.rectbutton[1].width, self.bg.rectbutton[1].height), 2)
    
    def ending(self):
        if self.bg.counter_niveau == 3:
            rect_prince = self.bg.rectporte[3]
            if self.player.rect.colliderect(rect_prince):
                return True
    
    def message_fin(self, window):
        self.souris = pygame.mouse.get_pos()
        window.blit(self.bg.image[9], (0,0))
        window.blit(self.bg.image[10], (self.bg.rectbutton[1].x, self.bg.rectbutton[1].y))
        pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[1].x, self.bg.rectbutton[1].y, self.bg.rectbutton[1].width, self.bg.rectbutton[1].height), 2)
        if pygame.mouse.get_pressed()[0]:  
                if self.bg.rectbutton[1].collidepoint(pygame.mouse.get_pos()):
                    self.player = Player(80)
                    self.cle = Cle() 
                    self.bg.counter_niveau = 0 ##A mettre à 3 pour se rendre directement à la scène du prince
                    self.bg.counter = 0
                    self.bg.start = 0
                    self.cle.counter_clelevel = 0
                    self.seuil = 0
                    self.bg.click = 0
                    self.bg.start_click = 0
                    
    

