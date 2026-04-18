import pygame

class Cle:
    def __init__(self):
        self.counter_clelevel = 0
        
        self.cles_niv1 = [
            pygame.Rect(840, 150, 50, 20), #cle1
            pygame.Rect(1600, 260, 50, 20), #cle2
            pygame.Rect(2050, 130, 50, 20) #cle3
        ]
        
        self.cles_niv2 = [
            pygame.Rect(250, 50, 50, 20), #cle1
            pygame.Rect(1110, 240, 50, 20), #cle2
            pygame.Rect(2030, 150, 50, 20) #cle3
        ]
        
        self.cles_niv3 = [
            pygame.Rect(840, 150, 50, 20), #cle1
            pygame.Rect(1550, 260, 50, 20), #cle2
            pygame.Rect(2050, 130, 50, 20) #cle3
        ]
        self.img = pygame.image.load("../img_file/clered.png")
    
    #surface.blit(image, (x,y))
    def draw(self, window, seuil):
        if self.counter_clelevel == 0:
            for cle in self.cles_niv1:
                window.blit(self.img, (cle.x + seuil, cle.y))
        
        if self.counter_clelevel == 1:
            for cle in self.cles_niv2:
                window.blit(self.img, (cle.x + seuil, cle.y))
        
        if self.counter_clelevel == 2:
            for cle in self.cles_niv3:
                window.blit(self.img, (cle.x + seuil, cle.y))