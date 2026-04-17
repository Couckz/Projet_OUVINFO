import pygame

class Cle:
    def __init__(self):
        self.cles = [
            pygame.Rect(840, 150, 50, 20), #cle1
            pygame.Rect(1600, 260, 50, 20), #cle2
            pygame.Rect(2050, 130, 50, 20) #cle3
        ]
        self.img = pygame.image.load("../img_file/clered.png")
    
    #surface.blit(image, (x,y))
    def draw(self, window, seuil):
        for cle in self.cles:
            window.blit(self.img, (cle.x + seuil, cle.y))