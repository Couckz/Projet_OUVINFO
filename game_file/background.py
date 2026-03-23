""" 
contient la classe qui gère le joueur"""
import pygame
from gameconfig import Gameconfig

class Background(pygame.sprite.Sprite):
    LEFT = -1
    RIGHT = 1
    NONE = 0
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, Gameconfig.Y_PLATEFORM, Gameconfig.PLAYER_H, Gameconfig.PLAYER_W)
        self.sprite_count = 0
        self.direction = Player.NONE
        self.image = Player.image[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.mask[self.direction][self.sprite_count//Gameconfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.vx = 0
        self.vy = 0
        
    def draw(self, window):
        window.blit(self.image, self.rect.topleft)
    
    def advance_state(self, next_move):
        fx = 0
        fy = 0
        if next_move.left:
            fx = Gameconfig.FORCE_LEFT
            BACKGROUND_LEVEL1.direction = Player.LEFT
        elif next_move.right:
            fx = Gameconfig.FORCE_RIGHT    
            BACKGROUND_LEVEL1.direction = Player.RIGHT 
            
        x,y = self.rect.topleft
        vx_min = -x/Gameconfig.DT
        vx_max = (Gameconfig.WINDOW_W-Gameconfig.PLAYER_W-x)/Gameconfig.DT
        self.vx = fx*Gameconfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
