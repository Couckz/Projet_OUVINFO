# """ 
# Ce fichier définit l'état actuel du jeu"""
# from gameconfig import Gameconfig
# from player import *
# from move import Move
# from background import BG
# from plateformes import plateform 
# from cle import Cle
# from prince import Prince
# from ennemis import Ennemis

# class Gamestate: 
#     def __init__(self):
#         self.game = Gameconfig()
#         self.player = Player(80)
#         self.cle = Cle()
#         self.ennemi = Ennemis()
#         self.seuil = 0
#         self.bg = BG()
#         self.platforms = plateform()
#         self.fin_atteinte = False 
#         self.prince = Prince(300, Gameconfig.Y_PLATEFORM - Gameconfig.PRINCE_H)

#     def advance_state(self, next_move):
#         # 1. Sélectionner la liste des plateformes du niveau en cours
#         if self.bg.counter_niveau == 0:
#             current_platforms = self.platforms.platforms_niv1
#         elif self.bg.counter_niveau == 1:
#             current_platforms = self.platforms.platforms_niv2
#         elif self.bg.counter_niveau == 2:
#             current_platforms = self.platforms.platforms_niv3
#         elif self.bg.counter_niveau == 3:
#             current_platforms = self.platforms.plateforms_niv4
#         else:
#             current_platforms = []

#         # 2. On passe cette liste au joueur pour qu'il gère ses déplacements/collisions proprement
#         self.player.advance_state(next_move, current_platforms)
#         self.seuil = max(self.seuil + Gameconfig.D_SEUIL, Gameconfig.seuil_max)
    
#     def draw(self, window):
#         self.bg.draw(window, self.seuil)
#         self.player.draw(window, self.seuil)
#         self.cle.draw(window, self.seuil)
#         pygame.draw.rect(window, (0, 255, 0), (self.bg.rectcle.x, self.bg.rectcle.y, self.bg.rectcle.width, self.bg.rectcle.height), 2) 
#         pygame.draw.rect(window, (0, 0, 255), (self.bg.rectporte[self.bg.counter_niveau].x + self.seuil, self.bg.rectporte[self.bg.counter_niveau].y, self.bg.rectporte[self.bg.counter_niveau].width, self.bg.rectporte[self.bg.counter_niveau].height), 2) 
#         pygame.draw.rect(window, (0, 255, 0), (self.bg.rectvie.x, self.bg.rectvie.y,  self.bg.rectvie.width, self.bg.rectvie.height), 2)
        
#         # Débogage visuel des niveaux
#         if self.bg.counter_niveau == 0:
#             for platform in self.platforms.platforms_niv1:
#                 pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
#             for key in self.cle.cles_niv1:
#                 pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
#             for position in self.ennemi.position_level1:
#                 pygame.draw.rect(window, (255, 255, 0), (position.x + self.seuil, position.y, position.width, position.height), 0)

#         if self.bg.counter_niveau == 1:
#             for platform in self.platforms.platforms_niv2:
#                 pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
#             for key in self.cle.cles_niv2:
#                 pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)
        
#         if self.bg.counter_niveau == 2:
#             for platform in self.platforms.platforms_niv3:
#                 pygame.draw.rect(window, (255, 0, 0), (platform.x + self.seuil, platform.y, platform.width, platform.height), 2)
#             for key in self.cle.cles_niv3:
#                 pygame.draw.rect(window, (0, 0, 255), (key.x + self.seuil, key.y, key.width, key.height), 2)

#         if self.bg.counter_niveau == 3 :
#            window.blit(self.bg.image[8], (0, 0))
#            self.prince.draw(window, self.seuil)
#            if self.player.rect.colliderect(self.prince.rect) :
#                 self.fin_atteinte = True 
#                 self.bg.counter_niveau = 4

#         if self.bg.counter_niveau == 4 :
#             self.prince.draw(window, self.seuil)
#             if self.fin_atteinte :
#                 self.dessiner_fin(window)
                
#     def move_ennemi(self):
#         if self.bg.counter_niveau == 0:
#             for positions in self.ennemi.position_level1:
#                 seuil_bas = positions.x - 20
#                 seuil_haut = positions.x + 20
#                 if positions.x <= seuil_haut:
#                     positions.x = positions.x + 5
#                 elif min(positions.x, seuil_bas) != positions.x :
#                     positions.x = positions.x - 5
        
#     def collision(self):
#         # Les collisions de plateformes sont maintenant gérées directement lors du déplacement.
#         # Cette méthode reste là pour ne pas casser le main.py, tu pourras y mettre les collisions avec les ennemis plus tard.
#         pass
        
#     def collision_cle(self):
#         if self.cle.counter_clelevel == 0:
#             for cle in self.cle.cles_niv1:
#                 if cle.colliderect(self.player.rect):
#                     self.cle.cles_niv1.remove(cle)
#                     self.bg.counter += 1
        
#         if self.cle.counter_clelevel == 1:
#             for cle in self.cle.cles_niv2:
#                 if cle.colliderect(self.player.rect):
#                     self.cle.cles_niv2.remove(cle)
#                     self.bg.counter += 1
        
#         if self.cle.counter_clelevel == 2:
#             for cle in self.cle.cles_niv3:
#                 if cle.colliderect(self.player.rect):
#                     self.cle.cles_niv3.remove(cle)
#                     self.bg.counter += 1
                    
#         if self.bg.rectporte[self.bg.counter_niveau].colliderect(self.player.rect) and self.bg.counter == 3:
#                 self.bg.counter_niveau += 1
#                 self.cle.counter_clelevel += 1
#                 self.bg.counter = 0
#                 self.seuil = 0
#                 self.player = Player(50)
        
#     def fin_jeu(self):
#         if -self.seuil >= self.player.rect.x:
#             return True
    
#     def ecran_fin_jeu(self, window):
#         self.bg.draw_end(window)
#         pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[0].x, self.bg.rectbutton[0].y, self.bg.rectbutton[0].width, self.bg.rectbutton[0].height), 2)
#         if self.bg.click >= 1:
#             self.player = Player(80)
#             self.cle = Cle() 
#             self.bg.counter_niveau = 0
#             self.bg.counter = 0
#             self.bg.start = 0
#             self.cle.counter_clelevel = 0
#             self.seuil = 0
#             self.bg.click = 0
    
#     def debut_jeu(self, window):
#         if self.bg.counter_niveau == 5:
#             self.bg.draw_start(window)
#             if self.bg.start_click >= 1:
#                 self.player = Player(80)
#                 self.cle = Cle() 
#                 self.bg.counter_niveau = 2
#                 self.bg.counter = 0
#                 self.bg.start = 0
#                 self.cle.counter_clelevel = 2
#                 self.seuil = 0
#                 self.bg.click = 0
#             pygame.draw.rect(window, (0, 0, 255), (self.bg.rectbutton[1].x, self.bg.rectbutton[1].y, self.bg.rectbutton[1].width, self.bg.rectbutton[1].height), 2)
        
#     def dessiner_fin(self, window) :
#         overlay = pygame.Surface((Gameconfig.WINDOW_W, Gameconfig.WINDOW_H), pygame.SRCALPHA)
#         overlay.fill((0,0,0,150))
#         window.blit(overlay, (0,0))

#         texte_victoire = Gameconfig.FONT_FIN.render("Le Prince est délivré !", True, (255,215,0))
#         texte_sous_titre = Gameconfig.FONT_PETITE.render ("Félicitation, vous avez gagné !", True, (255,255,255))

#         rect_victoire = texte_victoire.get_rect(center=(Gameconfig.WINDOW_W//2, Gameconfig.WINDOW_H//2-40))
#         rect_sous_titre = texte_sous_titre.get_rect(center=(Gameconfig.WINDOW_W//2, Gameconfig.WINDOW_H//20+20))

#         window.blit(texte_victoire, rect_victoire)
#         window.blit(texte_sous_titre, rect_sous_titre)

#         bouton_rect = pygame.Rect(Gameconfig.WINDOW_W//2-100, Gameconfig.WINDOW_H//2+60, 200, 50)
#         pygame.draw.rect(window, (255,255,255), bouton_rect, 2)

#         texte_rejouer = Gameconfig.FONT_PETITE.render("Cliquez pour Rejouer", True, (255,255,255))
#         rect_texte_btn = texte_rejouer.get_rect(center=bouton_rect.center)
#         window.blit(texte_rejouer, rect_texte_btn)

#         souris = pygame.mouse.get_pos()
#         if bouton_rect.collidepoint(souris) :
#             pygame.draw.rect(window, (255,255,255), bouton_rect)
#             window.blit(Gameconfig.FONT_PETITE.render("Cliquez pour Rejouer", True, (0,0,0)), rect_texte_btn)
#             if pygame.mouse.get_pressed()[0] :
#                 self.__init__()